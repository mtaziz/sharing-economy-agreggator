$(document).ready(function() {

	// Initialisation de variables
  	$('[data-toggle="popover"]').popover();

	
	$("#loginpopup").bind("click", function() {
		$('#login').modal('toggle');
	});
	
	 $('#signup-link').bind("click", function() {
	    $('#login').modal('hide');
	     $('#signup').modal('toggle');
	 });
	 $('#login-link').bind("click", function() {
	    $('#signup').modal('hide');
	     $('#login').modal('toggle');
	 });


});