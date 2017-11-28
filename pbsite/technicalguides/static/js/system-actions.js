$(document).ready(function() {
	$( "li.dropdown" ).hover(function() {
				$(this).dropdown('toggle');
			}, function() {
				$(this).parent().removeClass("show");
				$(this).removeAttr("aria-expanded");
				$(this).find('div.dropdown-menu').removeClass("show");
		});
});