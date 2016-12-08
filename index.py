# init app
from flask import Flask
app = Flask(__name__)

# allows for rendering of templates
from flask import render_template

# CRUD opperations
from flask import request

# creates DB
import sqlite3
conn = sqlite3.connect('badidea.db', check_same_thread=False)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/ideas', methods=['GET', 'POST'])
def idea():
    if request.method == 'POST':
        i = request.form['idea']
        print i
        c = conn.cursor()
        c.execute('INSERT INTO bad_ideas (ideas) VALUES (?)', (i,))
        conn.commit()
        return render_template('ideas.html')

    elif request.method == 'GET':
        get_idea()


@app.route('/ideas/1', methods=['POST'])
def idea1():
    print request.form
    if request.method == 'POST':
        return render_template('ideas1.html')


@app.route('/ideas/2', methods=['POST'])
def idea2():
    print request.form
    if request.method == 'POST':
            return render_template('ideas2.html')


@app.route('/ideas/3', methods=['POST'])
def idea3():
    print request.form
    if request.method == 'POST':
        return render_template('ideas3.html')


@app.route('/ideas/4', methods=['POST'])
def idea4():
    print request.form
    if request.method == 'POST':
        return render_template('ideas4.html')


@app.route('/ideas/5', methods=['POST'])
def idea5():
    print request.form
    if request.method == 'POST':
        return render_template('ideas5.html')


@app.route('/ideas/6', methods=['POST'])
def idea6():
    print request.form
    if request.method == 'POST':
        return render_template('ideas6.html')


@app.route('/ideas/7', methods=['POST'])
def idea7():
    print request.form
    if request.method == 'POST':
        return render_template('ideas7.html')


@app.route('/ideas/8', methods=['POST'])
def idea8():
    print request.form
    if request.method == 'POST':
        return render_template('ideas8.html')


@app.route('/ideas/9', methods=['POST'])
def idea9():
    print request.form
    if request.method == 'POST':
        return render_template('ideas9.html')


@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        return render_template('result.html')

@app.route('/tree', methods=['POST'])
def tree():
    if request.method == 'POST':
        return render_template('tree.html')
