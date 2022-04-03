from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import ARRAY

app = Flask(__name__)
db_name = "incubyte"  # USE YOUR OWN DB NAME
user_name = "postgres" # USE YOUR OWN USER NAME
password = "1234" # USE YOUR PASSWORD
host = "localhost" # USE YOUR HOST
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_name}:{password}@{host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Words(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    list_words = db.Column(ARRAY(db.String(80)))

    def __init__(self, words):
        self.list_words = words

    def __repr__(self):
        return f"Words : {self.list_words}"

    def get_list_words(self):
        return self.list_words


@app.route('/', methods=['GET'])
def get_all_words():
    all_words = Words.query.all()
    if all_words:
        return f"{all_words[0]}"
    return f"Not Found any Words"


@app.route('/add', methods=['POST'])
def add_words():
    single_word = request.json.get('word')
    all_words = Words.query.first()
    if all_words.get_list_words() is not None:
        one_record = Words.query.first()
        new_record = one_record.get_list_words()
        if single_word in new_record:
            return f"{single_word} this word already exist"
        db.session.delete(one_record)
        new_record.append(single_word)
        obj = Words(words=new_record)
        db.session.add(obj)
        db.session.commit()
        return f"added new word to {Words.query.first()}"
    else:
        list_word = [single_word]
        new_word = Words(words=list_word)
        db.session.add(new_word)
        db.session.commit()
        return "added single word to the list"


@app.route('/update', methods=['POST'])
def update_words():
    old_word = request.json.get('old_word')
    new_word = request.json.get('new_word')
    # self.Word = list(map(lambda x: x.replace(find_a_word, change_to), self.Word))
    all_words = Words.query.first()
    new_record = all_words.get_list_words()
    if old_word in new_record:
        db.session.delete(all_words)
        new_record = list(map(lambda x: x.replace(old_word, new_word), new_record))
        obj = Words(words=new_record)
        db.session.add(obj)
        db.session.commit()
        return f"update from {old_word} to {new_word}"
    else:
        return f"didn't find to update {old_word} word"


@app.route('/delete', methods=['POST'])
def delete_words():
    delete_word = request.json.get('delete_word')
    all_words = Words.query.first()
    new_record = all_words.get_list_words()
    if delete_word in new_record:
        db.session.delete(all_words)
        new_record.remove(delete_word)
        obj = Words(words=new_record)
        db.session.add(obj)
        db.session.commit()
        return f"{delete_word} is deleted from list"
    else:
        return f"didn't find to delete {delete_word} word"


if __name__ == "__main__":
    app.run(debug=True)
