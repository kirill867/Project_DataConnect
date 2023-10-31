from flask import Blueprint, render_template, request, redirect
from sql_provider import SQLProvider
from database import make_request, make_update

edit_app = Blueprint('edit', __name__, template_folder='templates')

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '7210109',
    'db': 'ships_in_ports'
}

provider = SQLProvider('blueprints/edit/sql/')

@edit_app.route('/', methods=['GET', 'POST'])
def list_goods():
    if request.method == 'GET':
        items = make_request(db_config, provider.get('edit_list.sql'))
        print(items)
        return render_template('edit.html', items=items, heads=['Название', 'Объём'])
    else:
        item_id = request.form.get('box_id')
        print('box_id=', item_id)
        sql = provider.get('delete_item.sql', box_id=item_id)
        response = make_update(db_config, sql)
        print('response=', response)
        return redirect('/edit')


@edit_app.route('/insert', methods=['GET', 'POST'])
def insert_item():
    if request.method == 'GET':
        return render_template('insert_item.html')
    else:
        item_name = request.form.get('box_name')
        volume = request.form.get('volume')
        sql = provider.get('insert_item.sql', box_name=item_name, volume=volume)
        response = make_update(db_config, sql)
        print('res=', response)
        return redirect('/edit')
