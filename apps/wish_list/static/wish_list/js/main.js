$(function(){
	$('input').on('focusin', function(){
		$(this).siblings('.errMsg').hide();
	})
})