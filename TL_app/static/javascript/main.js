const sidebar = document.getElementById("sidebar");

document.addEventListener('click', (e) => {
	if (sidebar.style.display=="block"){
		if(!e.target.closest('sidebar')) {
			sidebar.style.display="none";
		}
	}else{
		document.getElementById("sidebar").style.display="block";
		var element = document.getElementById( "tab2" ) ;
		element.checked = true ;

	}

		
})