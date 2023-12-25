let app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            skillsList: [],
            testimonialList: [],
            projectList: [],
            educationList: [],
            serviceList:[],
            socialList:[],
            portfolioItem: {},

            // Client Inquire
            formData: {
                full_name: '',
                phone: '',
                email: '',
                subject: '',
                budget: null,
                text: ''
            },
            message: null,
            messageClass: null,
            isBlock: false,
            sending: false,
        }
    },
    mounted() {
        this.fetchSkills()
        this.fetchPortfolio()
        this.fetchProject()
        this.fetchTestimonial()
        this.fetchEducation()
        this.fetchService()   
        this.fetchSocials()     
    },
    methods: {

        fetchSkills(){
            fetch('/api/skills/')
            .then(response => response.json())
            .then(data => {
                this.skillsList = data.results
            // console.log('this skill list: ', this.skillsList)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        fetchSocials(){
            fetch('/api/socials/')
            .then(response => response.json())
            .then(data => {
                this.socialList = data.results
            // console.log('this social list: ', this.socialList)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        fetchPortfolio(){
            fetch('/api/profileitems/')
            .then(response => response.json())
            .then(data => {
                this.portfolioItem = data.results[0]
            // console.log('this portfolio item: ', this.portfolioItem)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        fetchEducation(){
            fetch('/api/educations/')
            .then(response => response.json())
            .then(data => {
                this.educationList = data.results
            // console.log('this education list: ', this.educationList)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },
        // Date Format
        dateFormat(v){
            var date = new Date(v);
            var options = {
                year: "numeric",
                month: "short",
                day: "numeric"
            };
            const cur = date.toLocaleDateString( "en", options,  )
            return cur
        },


        fetchTestimonial(){
            fetch('/api/testimonials/')
            .then(response => response.json())
            .then(data => {
                this.testimonialList = data.results
                // console.log('this testimonial list: ', this.testimonialList)
                // Testimonial Owl Carusel
                this.$nextTick(() => {
                    if ($('.testimonial-slider').length) {
                    var testimonial = $('.testimonial-slider').owlCarousel({
                        items: 1,
                        margin: 30,
                        stagePadding: 0,
                        smartSpeed: 450,
                        autoHeight: true,
                        loop: false,
                        nav: false,
                        dots: false,
                        onInitialized: this.counter, // When the plugin has initialized.
                        onTranslated: this.counter, // When the translation of the stage has finished.
                    });
            
                    $('.testimonial-nav .next').on('click', function () {
                        testimonial.trigger('next.owl.carousel');
                    });
            
                    $('.testimonial-nav .prev').on('click', function () {
                        testimonial.trigger('prev.owl.carousel', [300]);
                    });
                    
                    }
                });
                
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },
        // Counter for Testimonials
        counter(event) {
            var element = event.target; // DOM element, in this example .owl-carousel
            var items = event.item.count; // Number of items
            var item = event.item.index + 1; // Position of the current item
      
            // Reset counter from 1 if it loops
            if (item > items) {
              item = item - items;
            }
      
            $('#testimonial-slide-count').html("<span class='left'>" + item + "</span> / " + items);
        },


        fetchProject(){
            fetch('/api/projects/')
            .then(response => response.json())
            .then(data => {
                this.projectList = data.results
            // console.log('this project list: ', this.projectList)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },
        // Project tags (string to list)
        tagsArray(tagString) {
            // Split the string and return an array
            return tagString.split(',').map(tag => tag.trim());
        },


        // Service Fetch
        fetchService(){
            fetch('/api/services/')
            .then(response => response.json())
            .then(data => {
                this.serviceList = data.results
            // console.log('this service list: ', this.serviceList)
            })
            .catch(error => {
            // console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        // Contact Form Submition
        submitForm() {
            this.sending = true;
            if (!this.validateForm()) {
                return;
            }
            // Send the data to your Django REST Framework endpoint

            // console.log('form data before fetch: ', this.formData)
            fetch('/api/contacts/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.formData),
            })
            .then(response => response.json())
            .then(data => {
                // console.log('Contact created:', data);
                if (data) {
                    const budgetError = Array.isArray(data.budget) ? data.budget.join(', ') : '';
                    const phoneError = Array.isArray(data.phone) ? data.phone.join(', ') : '';
                
                    if (budgetError || phoneError) {
                        this.message = budgetError + phoneError;
                        this.messageClass = 'alert-danger';
                    } else {
                        this.message = 'Contact created successfully.';
                        this.messageClass = 'alert-success';
                        this.resetForm()
                    }
                } 
                this.showMessage();
            })
            .catch(error => {
                // console.error('There was an error creating the contact:', error);
                this.message = 'Error creating contact.';
                this.messageClass = 'alert-danger';
                this.showMessage()
            })
            .finally(() => {
                // Enable the send button after response (success or error)
                this.sending = false;
            });
        },
        validateForm() {
            const { full_name, email, text, subject } = this.formData;
            const messageRequired = document.getElementById('required-msg');
            if (!full_name || !email || !text || !subject) {
                this.message = 'Please fill in the required fields.';
                this.messageClass = 'alert-danger';
                messageRequired.classList.add('show');
                this.showMessage();
                return false;
            }
            messageRequired.classList.remove('show')
            // Performing additional validations based on requirements
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                this.message = 'Please enter a valid email address.';
                this.messageClass = 'alert-danger';
                this.showMessage();
                return false;
            }

            return true;
        },
        showMessage() {
            messageDiv = $('.messenger-box-contact__msg'),
            this.isBlock = true;
            // Set a timeout to hide the message after a certain duration (e.g., 3000 milliseconds)
            setTimeout(() => {
                this.isBlock = false;
                this.message = null;
                this.messageClass = null;
            }, 10000);
        },
        resetForm() {
            // Reset form data to initial values or an empty object
            this.formData = {
                full_name: '',
                phone: '',
                email: '',
                subject: '',
                budget: null,
                text: ''
            };
        },
    }    
});
app.mount('#index');