from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/user/<name>')
def user(name):
    return render_template('profile.html', name=name.title())

if __name__ == '__main__':
    app.run()