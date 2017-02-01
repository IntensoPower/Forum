from flask import Flask
from flask import render_template

#import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

### Forum 

@app.route('/forum', methods=['GET'])
def forum():
  auteurs = [
    "Mathis",
    "Florian",
    "Gregory"
  ]
  return render_template('forum.html', auteurs = auteurs)


if __name__ == "__main__":
    app.run()
