from flask import Flask, request, abort
import json
import config

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            f = open(config.DATA_USER)
            all_users = json.load(f)['user']
            req_dct = request.get_json()

            # Login by username or email
            login_by = ''
            for key in ['username', 'email']:
                if req_dct.get(key):
                    login_by = key
                    break
            if not login_by:
                return 'Login unsuccessful without username or email.', 200

            # Login user
            for user in all_users:
                if req_dct.get(login_by) == user.get(login_by):
                    if req_dct.get('password') == user.get('password'):
                        # Redirect
                        return 'Login successful for \'{}\': \'{}\'.'.format(login_by, req_dct.get(login_by)), 200
                    elif req_dct.get('password'):
                        return 'Wrong password entered for \'{}\': \'{}\'.'.format(login_by, req_dct.get(login_by)), 200
                    else:
                        return 'No password entered for \'{}\': \'{}\'.'.format(login_by, req_dct.get(login_by)), 200

            return 'Login unsuccessful for \'{}\': \'{}\'.'.format(login_by, req_dct.get(login_by)), 200
        except IOError:
            return 'Failed to connect to Db. Please contact admin.', 500
        except ValueError as e:
            return 'Failed to read Users Db. Please contact admin.', 500
        finally:
            f.close()
    else:
        abort(405)


@app.route('/newsignup', methods=['POST'])
def newsignup():
    pass
