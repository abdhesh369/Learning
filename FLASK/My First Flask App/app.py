from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     user_name = "Abdhesh"
#     return render_template('home.html', name=user_name)


@app.route('/fruits')
def fruits():
    fruit_list = ["Apple", "Banana", "Mango", "Orange"]  # Python list (you know this!)
    return render_template('fruits.html', fruits=fruit_list)


if __name__ == '__main__':
    app.run(debug=True)