from flask import Flask
from flask import render_template

import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

### Forum 

@app.route('/forum', methods=['GET'])
def forum():
  return render_template('forum.html', forums)


if __name__ == "__main__":
    app.run()
