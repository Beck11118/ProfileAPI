let app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            skillsList: [],
            portfolioItem: {},
        }
    },
    mounted() {
        console.log('error')
        this.fetchSkills()
        this.fetchPortfolio()
        // Make a fetch request
        
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
        }
    }    
});
app.mount('#index');