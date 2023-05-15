from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name.title())

if __name__ == '__main__':
    app.run()