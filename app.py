from flask import Flask, render_template, session
from blueprints.profile.routes import profile_app
from blueprints.authorization.routes import auth_app
from blueprints.authorization.access import login_required
from blueprints.edit.routes import edit_app
from sql_provider import SQLProvider
from database import work_with_db

app = Flask(__name__)
app.register_blueprint(profile_app, url_prefix='/profile')#1 - приложение, которое к этому app привязать, 2 - то, как его идентифицировать
app.register_blueprint(auth_app, url_prefix='/authorization')
app.register_blueprint(edit_app, url_prefix='/edit')
#все url, начинающиеся с profile, будут передаваться в routes - nfv ,eltn
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '7210109',
    'db': 'ships_in_ports'
}

provider = SQLProvider('blueprints/profile/sql/')
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/counter')
def count_visits():
    counter = session.get('count', None)
    if counter is None:
        session['count'] = 0
    else:
        session['count'] = session['count'] + 1
    return f"Your count: {session['count']}"

@app.route('/session-clear')
def clear_session():
    session.clear()
    return ''

@app.route('/get-name')
@login_required
def select_version():
    sql = provider.get('task1.sql', i='100')
    result = work_with_db(db_config, sql)
    return str(result)

@app.route('/exit')
def exit_handler():
    session.clear()
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
