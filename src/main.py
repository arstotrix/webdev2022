from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/telegrams')
def telegrams():
    return render_template('telegrams.html')


@app.route('/longread', methods=['GET'])
def longread():
    return render_template('longread.html')


@app.route('/thank-you', methods=['GET'])
def thankyou():
    return render_template('thankyou.html')


@app.route('/add', methods = ['POST', 'GET'])
def add():
#    if request.method == 'POST':
#        name = request.form['link']
#        mail = request.form['word']
#        plott(getsearcher(link, word))
#        #fin_form = link+'\n'+word
    return render_template('add.html')
