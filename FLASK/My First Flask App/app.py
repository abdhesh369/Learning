from flask import Flask, render_template, request  # Add 'request'

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')  # Route to SHOW the form
def show_form():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])  # Route to RECEIVE form data
def greet():
    user_name = request.form.get('name')  # Get the data from form!
    return f"<h1>Hello, {user_name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)