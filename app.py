from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_user_id', methods=['POST'])
def show_user_id():
    user_id = request.form['user_id']
    user_clue = {
        "CT001":"Clue 1",
        "CT002":"Clue 2",
        "CT003":"Clue 3",
        "CT004":"Clue 4",
    }
    if user_id in user_clue:
        clue = user_clue[user_id]
    else:
        clue = "Check the User ID"
    return render_template('show_user_id.html', clue=clue)

if __name__ == '__main__':
    app.run(debug=True)
