from flask import Flask, render_template, request
import urllib.request
import json
import collections



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/telegrams', methods = ['POST', 'GET'])
def telegrams():
#    if request.method == 'POST':
#        link = request.form['link']
#        word = request.form['word']
#        plott(getsearcher(link, word))
#        #fin_form = link+'\n'+word
    return render_template('telegrams.html')

@app.route('/longread', methods = ['POST', 'GET'])
def longread():
#    if request.method == 'POST':
#        link = request.form['link']
#        word = request.form['word']
#        plott(getsearcher(link, word))
#        #fin_form = link+'\n'+word
    return render_template('longread.html')

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



