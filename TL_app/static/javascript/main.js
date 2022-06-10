const sidebar = document.getElementById("sidebar");

function TLEClick(){
	document.getElementById("sidebar").style.display="block";
	const tab2 = document.getElementById( "tab2" ) ;
	tab2.checked = true ;
}

function TLClick(){
	document.getElementById("sidebar").style.display="block";
	const tab1 = document.getElementById( "tab1" ) ;
	tab1.checked = true ;
}

function sidebarhide(){
	document.getElementById("sidebar").style.display="none";
}

const App = {
	data() {
	  return {
	    tle: {title: ''},
	    tasks: ['test'],
	    tles:[''],
	  }
	  },
	compilerOptions: {
	    delimiters: ['[[', ']]'],
	},
	methods: {
		sendRequest(url, method, data){
			const csrftoken = Cookies.get('csrftoken');
			const myHeaders = new Headers({
			    'Content-Type': 'application/json',
			});
			if(method !== 'get'){
			    myHeaders.set('X-CSRFToken', csrftoken)
			};
	    
			fetch(url, {
			    method: method,
			    headers: myHeaders,
			    body: data,
			})
			.then((response) => {
			    return response.json();
			})
			.then((response) => {
			    if (method == 'get') {
				this.Tles = response;
			    };
			    if (method == 'post') {
				this.tle.title = ''
				this.tle.year = ''
				this.getTles();
			    };
			    if (method == 'put') {
				this.getTles();
			    };
			    if (method == 'put' || method == 'delete') {
				this.getTles();
			    };
			})
			.catch(error => {
			    console.error('There has been a problem with your fetch operation:', error);
			});
		},
		getTles(){
			this.sendRequest(URL, 'get');
		},
		createTle(){
			this.getTles();
			this.sendRequest(URL, 'post',JSON.stringify(this.tle));
		},
		updateTle(tle){
			this.getTles();
			this.sendRequest(URL, 'put',JSON.stringify(tle));
		},
		deleteTle(tle){
			this.getTles();
			this.sendRequest(URL, 'delete',JSON.stringify(tle));
		},
	created() {
	  	this.getTles();
	},
      },
}
Vue.createApp(App).mount('#app');