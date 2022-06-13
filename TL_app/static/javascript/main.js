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