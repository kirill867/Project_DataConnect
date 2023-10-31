import json
from flask import session, request, render_template
from functools import wraps
config = json.load(open('blueprints/authorization/configs/access.json'))

def group_validation(config:dict, session: session) -> bool:
    group = session.get('group_name', 'unauthorized')
    book = {
        1: "",
        2: request.endpoint
    }
    target_app = book[len(request.endpoint.split('.'))]
    if group in config and target_app in config[group]:
        return True
    return False

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if group_validation(config, session):
            return f(*args, **kwargs)
        return render_template('confirm.html', str='У вас нет доступа.')
    return wrapper