from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 가짜 데이터베이스
users = [
    {'id': 1, 'username': 'user1', 'password': 'pass1'},
    {'id': 2, 'username': 'user2', 'password': 'pass2'},
    {'id': 3, 'username': 'user3', 'password': 'pass3'}
]

@app.route('/')
def index():
    return redirect('/login')
    # return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate(username, password)
        if user:
            return redirect(url_for('dashboard', username=username))
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

def authenticate(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userid',None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
