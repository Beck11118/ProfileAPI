let app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            skillsList: [],
            testimonialList: [],
            projectList: [],
            educationList: [],
            serviceList:[],
            portfolioItem: {},
        }
    },
    mounted() {
        this.fetchSkills()
        this.fetchPortfolio()
        this.fetchProject()
        this.fetchTestimonial()
        this.fetchEducation()
        this.fetchService()        
    },
    methods: {

        fetchSkills(){
            fetch('/api/skills/')
            .then(response => response.json())
            .then(data => {
                this.skillsList = data.results
            console.log('this skill list: ', this.skillsList)
            })
            .catch(error => {
            console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        fetchPortfolio(){
            fetch('/api/profileitems/')
            .then(response => response.json())
            .then(data => {
                this.portfolioItem = data.results[0]
            console.log('this portfolio item: ', this.portfolioItem)
            })
            .catch(error => {
            console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },


        fetchEducation(){
            fetch('/api/educations/')
            .then(response => response.json())
            .then(data => {
                this.educationList = data.results
            console.log('this education list: ', this.educationList)
            })
            .catch(error => {
            console.error('Error fetching data:', error);
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
                console.log('this testimonial list: ', this.testimonialList)
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
            console.error('Error fetching data:', error);
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
            console.log('this project list: ', this.projectList)
            })
            .catch(error => {
            console.error('Error fetching data:', error);
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
            console.log('this service list: ', this.serviceList)
            })
            .catch(error => {
            console.error('Error fetching data:', error);
            this.message = 'Error fetching data';
            });
        },
    }    
});
app.mount('#index');