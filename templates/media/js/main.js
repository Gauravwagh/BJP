;(function(){

			// Menu settings
			$('#menuToggle, .menu-close').on('click', function(){
				$('#menuToggle').toggleClass('active');
				$('body').toggleClass('body-push-toleft');
				$('#theMenu').toggleClass('menu-open');
			});
			

})(jQuery)

$(function()
{
	
	window.setTimeout(closeMessages, 3000, true);
});


function closeMessages()
{

	$('#messages').children('.messages').each(function()
	{
		$(this).fadeOut();
	});	
	window.setTimeout(removeMessages, 1000, true);
}

function removeMessages()
{
	
	$('#messages').html('');
}