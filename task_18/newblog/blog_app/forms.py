from django.forms import ModelForm
from blog_app.models import Posts, Comments

class PostForm(ModelForm):
	class Meta:
		model = Posts
		fields = ['title', 'message']

class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['post_id', 'message']