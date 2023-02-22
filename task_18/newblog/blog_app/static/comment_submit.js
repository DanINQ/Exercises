'use strict';

(function (window, document, $) {
	$(document).ready(function() {
		$('.button.success').click(function (event) {
			event.preventDefault();

			var form = $('form')[0];

			var SendData = {
				'post_id':form['post_id']['value'],
				'message':form['message']['value'],
				'csrfmiddlewaretoken':form['csrfmiddlewaretoken']['value'],
			};

			var request = $.ajax({
				url:'http://127.0.0.1:8000/comment/',
				method:'POST',
				data:SendData,
				dataType:'json',
			});

			request.done(function (data, textStatus, jqXHR) {
				var comments = $('.comments');

				var commentId = $('<div>').addClass('comment_id').text('Comment ID:' + data['comment_id']);
				var commentMessage = $('<div>').addClass('comment_message').text(form['message']['value']);
				var commentDate = $('<div>').addClass('comment_date').text(data['date']);
				var comment = $('<div>').addClass('comment').append(commentId).append(commentMessage).append(commentDate);

				comments.append(comment);

				$('.comments_num').text($('.comments_num').text() + ' (+1)');
			});

			request.fail(function(jqXHR, textStatus, errorThrown) {
				var modal = $('#modal');
				modal.show();
				$('.close-button').click(function () {
					modal.hide();
				})
			})
		})
	})
})(window, document, jQuery)