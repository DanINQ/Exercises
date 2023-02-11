from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms_alchemy import ModelForm
from datetime import date

# Задача: 
# написать сервер на фласке, который бы реализовывал функциональность гостевой книги
# 
# Детализация:
# + по адресу '/' он должен выдавать html страницу с 
#   установленной на ней библиотекой jQuery и Bootstrap
#   
# + на странице должна быть красивая формочка с двумя полями: 
#   "имя" и "сообщение" и кнопкой "отправить"
# 
# + при нажатии на "отправить": 
#   - происходит асинхронный запрос по адресу '/comment'
#   - запрос валидируется, что у него есть оба 
#     обязательных поля и если он валиден, 
#     то результат сохраняется в базу данных
#   
# + возвращаем пользователю уведомление: "все прошло успешно"
#   если возникли проблемы, то возвращаем пользователю ошибку 
#   в новом всплывающем окошке (смотри документацию Bootstrap)

app = Flask(__name__)
app.config.update(
    template_folder='templates',
    SECRET_KEY='Some key nevermind at now',
    DEBUG=True,
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///task_14.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

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
        print(post.date)
        return {'post_id':post.id, 'date':str(post.date)}
    else:
        return 'fail', 500


@app.route('/comment', methods=['POST'])
def new_comment():
    form = CommentForm(request.form)
    if form.validate() and Posts.query.filter_by(id=request.form['post_id']).first():
        comment = Comments(**request.form)
        Posts.query.filter_by(id=comment.post_id).first()
        db.session.add(comment)
        db.session.commit()
        return {
        'date':str(comment.date),
        'comment_id':comment.id,
        }
    else:
        return "fail", 500


@app.route('/get_post/<int:post_id>')
def get_post(post_id):
    post = Posts.query.filter_by(id=post_id).first()
    comments = Comments.query.filter_by(post_id=post_id).all()
    return render_template('post.html', post=post, comments=comments)


@app.route('/get_all_posts')
def get_all_posts():
    posts = Posts.query.all()
    return render_template('main.html', posts=posts)


with app.app_context():
    db.create_all()

app.run()
