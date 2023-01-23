from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms_alchemy import ModelForm
from datetime import date


# 1. Она(*База) должна содержать модуль: GuestBookItem
# 1.1 Поле автор: любое значение
# 1.2 Текст сообщения, может быть любой текст длинее 5 символов
# 1.3 Дата и время публикации
# 1.4 Булевое поле: Удалено или нет

# 2. Вы должны иметь возмложность получить все записи по адресу "/"
# 3. Вы должны иметь возможность добавить запись по адресу "/create"
# 3.1 Должна работать валидация при помощи формы модели


app = Flask(__name__)

app.config.update(
    SECRET_KEY='Some key nevermind at now',
    DEBUG=True,
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI='sqlite:task_13.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

database = SQLAlchemy(app)


class GuessBookItem(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)

    author = database.Column(database.String, nullable=False)
    message = database.Column(database.String(5), nullable=False)
    date = database.Column(database.Date,
                           default=date.today(), nullable=False)
    is_deleten = database.Column(database.Boolean,
                                 default=False, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'message': self.message,
            'date': self.date
        }


class BookForm(ModelForm):
    class Meta:
        model = GuessBookItem


@app.route('/', methods=['GET'])
def get_book():
    messages = GuessBookItem.query.all()
    return jsonify([p.to_dict() for p in messages])


@app.route('/create', methods=['POST'])
def create_message():
    form = BookForm(request.form)

    if form.validate():
        new_message = GuessBookItem(**request.form)
        database.session.add(new_message)
        database.session.commit()
        print(GuessBookItem.query.all())
        messages = GuessBookItem.query.all()
        return jsonify([p.to_dict() for p in messages])


with app.app_context():
    database.create_all()
app.run()
