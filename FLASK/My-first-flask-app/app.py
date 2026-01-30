from flask import Flask, render_template  # Add render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # Use the template instead of HTML string!

if __name__ == '__main__':
    app.run(debug=True)