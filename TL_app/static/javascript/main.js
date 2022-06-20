const sidebar = document.getElementById("sidebar");

function TLClick(){
	document.getElementById("sidebar").style.display="block";
	const tab1 = document.getElementById( "tab1" ) ;
	document.getElementById("menu-btn-check").checked = false;
	tab1.checked = true ;
}
function TLEClick(){
	document.getElementById("sidebar").style.display="block";
	const tab2 = document.getElementById( "tab2" ) ;
	document.getElementById("menu-btn-check").checked = false;
	tab2.checked = true ;
}
function addTLEClick(){
	document.getElementById("sidebar").style.display="block";
	const tab3 = document.getElementById( "tab3" ) ;
	document.getElementById("menu-btn-check").checked = false;
	tab3.checked = true ;
}

function sidebarhide(){
	document.getElementById("sidebar").style.display="none";
}

