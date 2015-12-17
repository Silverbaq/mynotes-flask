# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash


# configuration
DATABASE = './db/notes.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    cur = g.db.execute('select Id, Title from Topic order by id desc')
    topics = [dict(id = row[0], title = row[1]) for row in cur.fetchall()]
    return render_template('select_topic.html', topics=topics)



### TEMP
@app.route('/test', methods = ['GET', 'POST'])
def show_notes():
    cur = g.db.execute('select Id, Title from Topic order by id desc')
    topics = [dict(id = row[0], title = row[1]) for row in cur.fetchall()]

    subjects = ''
    notes = ''
    if request.method == 'POST':
        topicid = request.form['topic']
        cur = g.db.execute('select Id, Title from Subject where TopicId = (?)', topicid)
        subjects = [dict(id = row[0], title = row[1]) for row in cur.fetchall()]

        if 'subject' in request.form:
            subjectId = request.form['subject']
            cur = g.db.execute('select Id, Value, Title from Note where SubjectId = (?)', subjectId)
            notes = [dict(id = row[0], value = row[1], title = row[2]) for row in cur.fetchall()]

    return render_template('show_notes.html', topics = topics, subjects = subjects, notes = notes)


@app.route('/selected_topic', methods=['POST'])
def selected_topic():
    topicid = [request.args.get('topicid')]
    cur = g.db.execute('select Id, Title from Subject where (?)', topicid)
    subjects = [dict(id = row[0], title = row[1]) for row in cur.fetchall()]
    return render_template('select_subject.html', subjects = subjects)


@app.route('/addTopic', methods=['GET','POST'])
def add_topic():
    try:
        top = request.form['topic']
        g.db.execute('insert into Topic (Title) values (?)',
                     [top])
        g.db.commit()
        flash('New topic was successfully added')
    except Exception as e:
        flash(e.message)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
