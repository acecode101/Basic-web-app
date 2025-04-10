from flask import Flask, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = 'x'

@app.route('/')
def home():
    return f"Hi {session['u']}! <a href='/lo'>Logout</a>" if 'u' in session else "<form method=post action='/li'><input name=u><input name=p type=password><input type=submit></form>"

@app.route('/li', methods=['POST'])
def li():
    if request.form['u'] == 'a' and request.form['p'] == '1': session['u'] = 'a'
    return redirect('/')

@app.route('/lo')
def lo():
    session.pop('u', 0)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
