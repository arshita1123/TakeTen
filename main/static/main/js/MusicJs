const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener('readystatechange', function () {
	if (this.readyState === this.DONE) {
		console.log(this.responseText);
	}
});

xhr.open('GET', 'https://spotify23.p.rapidapi.com/search/?q=%3CREQUIRED%3E&type=multi&offset=0&limit=10&numberOfTopResults=5');
xhr.setRequestHeader('X-RapidAPI-Key', '087794b943msh9faab7259f1350dp1c5cb2jsn96db58221932');
xhr.setRequestHeader('X-RapidAPI-Host', 'spotify23.p.rapidapi.com');

xhr.send(data);