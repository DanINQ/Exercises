from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms_alchemy import ModelForm
from datetime import date

# • Делаем анонимный блог (имиджборду)
# • Пользователь может написать пост: с заголовком и
# содержанием
# • Пользователи могут оставлять комментарии под
# записью
# • Пользователи отправляют POST запросы к серверу,
# чтобы оставлять записи и комментарии
# • Необходимо использовать текстовые шаблоны для
# вывода блога


# self instruction
# /get_post/*id поста* чтоб получить пост и комментарии
# /get_all_posts чтоб получить список постов
# /newpost чтоб создать новый пост, поля - title и message
# /comment чтоб добавить комментарий, поля - post_id и message


app = Flask(__name__)
app.config.update(
    template_folder='templates',
    SECRET_KEY='Some key nevermind at now',
    DEBUG=True,
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///task_14.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, autoincrement=True,
                   nullable=False, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today())


class Comments(db.Model):
    id = db.Column(db.Integer, autoincrement=True,
                   nullable=False, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),
                        nullable=False, index=True, )
    post = db.relationship(Posts, foreign_keys=[post_id])

    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today())


class PostForm(ModelForm):
    class Meta:
        model = Posts


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        include = ['post_id']


@app.route('/newpost', methods=['POST'])
def new_post():
    form = PostForm(request.form)
    if form.validate():
        post = Posts(**request.form)
        db.session.add(post)
        db.session.commit()
        return get_post(post.id)
    else:
        return "Invalid info"


@app.route('/comment', methods=['POST'])
def new_comment():
    form = CommentForm(request.form)
    if form.validate() and Posts.query.filter_by(id=request.form['post_id']).first():
        comment = Comments(**request.form)
        Posts.query.filter_by(id=comment.post_id).first()
        db.session.add(comment)
        db.session.commit()
        return get_post(comment.post_id)
    else:
        return "Invalid info"


@app.route('/get_post/<int:post_id>')
def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    comments = Comments.query.filter_by(post_id=post_id).all()
    return render_template('post_render.txt', post=post, comments=comments)


@app.route('/get_all_posts')
def get_all_posts():
    posts = Posts.query.all()
    return render_template('all_posts_render.txt', posts=posts)


with app.app_context():
    db.create_all()

app.run()
