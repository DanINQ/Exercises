'use strict';

	(function (window, document, $) {
		function GetText() {
			var message = $('.main')
			var id = Math.round(Math.random() * 100)
			var request = $.ajax({
				url:'https://jsonplaceholder.typicode.com/posts/' + id,
				crossDomain: true,
				dataType: 'json',
			});

			request.done(function (data, textStatus, jqXHR) {
				console.log('adding...')
				var title = $('<p>').addClass('title').text(request.responseJSON['title']);
				var text = $('<p>').addClass('text').text(request.responseJSON['body']);
				message.append(title, text);
				console.log('added!')
			});

			request.fail(function (jqXHR, textStatus, errorThrown) {
				message.append($('<p>').addClass('text').text('Something went wrong'))
			});
		}
		$(document).ready(function () {
			GetText()
		})
	})(window, document, jQuery)