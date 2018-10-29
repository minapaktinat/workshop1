from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
guesses = ['python', 'java', 'c#', 'c++']
questions = ['1) is it easy to learn!?', '2) does it run on mac!?']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/question/<int:id>' , methods=['GET','POST'])
def question(id):
    if request.method == 'POST':
        if request.form['answer'] == 'yes':
            return redirect(url_for('question', id=id+1))
    return render_template('question.html', question=questions[id])
 

@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


if __name__ == '__main__':
    app.run(debug=True)
