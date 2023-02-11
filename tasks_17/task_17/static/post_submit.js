'use strict';

(function (window, document, $) {
	$(document).ready(function () {
		var form = document.forms[0];
		form.addEventListener('submit', function (event) {
			event.preventDefault();
	
			var SendForm = {
					'title':form['title']['value'],
					'message':form['message']['value']
				};
	
			var request = $.ajax({
				url:'http://127.0.0.1:5000/newpost',
				method:'POST',
				data:SendForm,
				dataType:'json'
			});
	
			request.done(function (data, textStatus, jqXHR) {
				var main = document.getElementsByClassName('main')[0];
	
				var post = document.createElement('div');
				post.className = 'post';
	
				var header = document.createElement('h3');
				header.className = 'post_id';
	
				var PostIDButton = document.createElement('a');
				PostIDButton.className = 'button';
				PostIDButton.setAttribute('href', 'http://127.0.0.1:5000/get_post/' + data['post_id']);
				PostIDButton.innerText = 'Post ID: ' + data['post_id'];
	
				var title = document.createElement('div');
				title.className = 'title';
				title.innerText = SendForm['title'];
	
				var message = document.createElement('div');
				message.className = 'message';
				message.innerText = SendForm['message'];
	
				var PostDate = document.createElement('div');
				PostDate.className = 'date';
				PostDate.innerText = data['date'];
	
				header.appendChild(PostIDButton);
				post.appendChild(header);
				post.appendChild(title);
				post.appendChild(message);
				post.appendChild(PostDate);
				main.appendChild(post);
	
				document.getElementsByClassName('posts')[0].innerText += ' (+1)';
	
				var InputBlock = document.getElementsByClassName('post_input')[0];
	
				var SuccessMessage = document.createElement('div');
				SuccessMessage.className = 'successful';
				SuccessMessage.innerText = 'Succesful!!';
				InputBlock.appendChild(SuccessMessage);
	
			})
	
			request.fail(function (jqXHR, textStatus, errorThrown) {
				var modal = $('#modal');
				modal.show();
				$('.close-button').click(function () {
					modal.hide();
				})
			})
		})
	})
})(window, document, jQuery)