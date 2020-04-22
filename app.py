from uuid import uuid4
from flask import Flask, request, session
from flask.templating import render_template
from centeridentity.api import CenterIdentity


app = Flask(__name__)

ci = CenterIdentity('YOUR_CENTER_IDENTITY_API_KEY', 'YOUR_CENTER_IDENTITY_USERNAME')

@app.route('/')
def index():
    if not session.get('uuid'):
        session['uuid'] = str(uuid4())
    return render_template(
        'index.html',
        session_id=session['uuid']
    )

@app.route('/create-customer', methods=["POST"])
def create_customer():
    result = ci.add_user(request.json)
    return result

@app.route('/sign-in', methods=["POST"])
def sign_in():
    user = ci.authenticate(
        session['uuid'],
        request.json
    )
    session['user'] = user.to_dict
    return session['user']


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'