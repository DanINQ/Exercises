from django.shortcuts import render, redirect
from django.http import HttpResponse
import json


from blog_app.forms import PostForm, CommentForm
from blog_app.models import Posts, Comments

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			data = {'post_id':post.id, 'date':str(post.date)}
			return HttpResponse(json.dumps(data))
		else:
			return HttpResponse('fail')
	else:
		return HttpResponse(status=405)

def new_comment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save()
			data = {
			'date':str(comment.date),
			'comment_id':comment.id,
			}
			return HttpResponse(json.dumps(data))
		else:
			return HttpResponse('fail')
	else:
		return HttpResponse(status=405)

def get_all_posts(request):
	if request.method == 'GET':
		posts = Posts.objects.all()
		return render(request, 'main.html', {'posts':posts})
	else:
		return HttpResponse(status=405)

def get_post(request, post_id):
	if request.method == 'GET':
		comments = Comments.objects.filter(post_id=post_id)
		post = Posts.objects.filter(id=post_id)[0]
		return render(request, 'post.html', {'comments':comments, 'post':post})
	else:
		return HttpResponse(status=405)