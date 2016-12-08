import json
import random
import markovify
from snark_selects import snark1
from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, jsonify


app = Flask(__name__)

# bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/generate/<int:number>')
def generateWords(number):
    sentences = generate(number)
    
    return jsonify({
        'data': ' '.join(sentences)
    })


@app.route('/generateTweet/')
def generateATwit():
    twit = generateTwit()
    
    return jsonify({
        'data': twit
    })

@app.route('/generateSnark/')
def generateASnark():
    snork = generateSnork()
    
    return jsonify({
        'data': snork
    })




@app.route('/richBot/')
def rich():
    words = generate(5)
    return render_template("richBot.html", sentences=words)

def generateTwit():
    # Get raw text as string.
    with open("data/richbot.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    return text_model.make_short_sentence(140)


def generateSnork():
    snarkyness = snark1

    return random.choice(snarkyness)



def generate(numberOfSentences=3):

# Get raw text as string.
    with open("data/richbot.txt") as f:
    	text = f.read()

# Build the model.
    text_model = markovify.Text(text)

# Print five randomly-generated sentences
    words = []
    for i in range(numberOfSentences):
        words.append(text_model.make_sentence())
    return words


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
