import requests
import config
import re


def login(username, email, password):
    req_dct = {}
    # Validate username or email
    if username:
        if not re.search("^[a-zA-Z0-9_]*$", username):
            return "Username '{}' should contain only alphanumeric.\n".format(username)
        else:
            req_dct['username'] = username
    elif email:
        if not re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
            return "Email format '{}' is invalid.\n".format(email)
        else:
            req_dct['email'] = email
    else:
        return "Please provide either username or email.\n"

    # Validate password
    if not password:
        return "Password cannot be empty.\n"
    else:
        req_dct['password'] = password

    url = "http://{0}:{1}/{2}".format(config.HOST, config.PORT, "login")
    res = requests.post(url, json=req_dct)
    return res.content


def newsignup():
    print('empty new sign up def\n')


if __name__ == '__main__':
    while True:
        choice = '[1] Login\n[2] New Sign Up\n[3] Quit'
        x = input('Welcome to Xiapi Leave Management System.\nPlease enter your choice: \n{}\n>>>'.format(choice)).strip()
        if x == '1':
            print('Please enter your login username or password')
            username = input('username:\n>>>').strip()
            email = input('email:\n>>>').strip()
            password = input('Please enter your password:\n>>>').strip()
            print(login(username, email, password))
        elif x == '2':
            newsignup()
        elif x == '3':
            break
        else:
            print('You have entered an invalid input.')
