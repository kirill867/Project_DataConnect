from flask import Blueprint, render_template, session, request
from sql_provider import SQLProvider
from database import work_with_db

auth_app = Blueprint('authorization', __name__, template_folder='templates')

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '7210109',
    'db': 'ships_in_ports'
}

provider = SQLProvider('blueprints/authorization/sql/')

@auth_app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login = request.form.get('login', '')
        password = request.form.get('password', '')
        sql = provider.get('sql.sql', login=login, password=password)
        user_group = str(work_with_db(db_config, sql))[17:-3]

        if user_group != '':
            session['group_name'] = user_group
            return render_template('confirm.html', str='Вы успешно авторизовались!')
        else:
            return render_template('confirm.html', str='Вы не авторизовались!')

