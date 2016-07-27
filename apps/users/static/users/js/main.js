$(function(){
	$("#datepicker").datepicker();
	function passwordMatch(pw, pwConf, submit) {
		var password;
		pw.on('focusout', function(){
			password = $(this).val();
			return password;
		})
		pwConf.on('keyup', function(){
			var passwordConf = $(this).val();
			if (passwordConf !== password) {
				$(this).css({'color':'red'});
				submit.prop("disabled",true);
			}else {
				$(this).css({'color': 'black'});
				submit.removeAttr("disabled");
			}
		})
	}
	passwordMatch($('#regPassword'), $('#regPasswordConf'), $('#regSubmit'));
	
	$('input').on('focusin', function(){
		$(this).siblings('.errMsg').hide();
	})
})