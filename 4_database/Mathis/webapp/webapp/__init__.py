#
from flask import Flask
from flask import render_template, request, redirect, url_for

from utils import select_database, insert_database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


### Forum 

@app.route('/forums', methods=['GET'])
def forum():
    return render_template('forum.html', subjects = select_database())

@app.route('/forums/add', methods=['GET', 'POST'])
def add_subject():
    print request.form

    # Appel de la fonction en POST
    if request.method == 'POST':
        print "Appel POST"

        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        new_subject = {
            'title': title, 
            'author': author, 
            'writeDate': "01/02/17", 
            'content': content, 
            'id': "sujet %d" % (len(select_database()))
        }
        
        insert_database(new_subject)

        return redirect(url_for('forum'))

    # Appel de la fonction en GET
    else:
        print "Appel GET"
        return render_template('formulaire.html')



if __name__ == "__main__":
    app.run()
