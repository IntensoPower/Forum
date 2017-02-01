from flask import Flask
from flask import render_template, request, redirect, url_for

#import utils
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


### Forum 
subjects = [
    {'title': 'Les chiens et chats', 'author': 'Mathis', 'date': '30/01/17', 'contenu': 'blabla', 'id':'sujet1' },
    {'title': 'Les chevaux et poneys', 'author': 'Florian', 'date': '31/01/17', 'contenu': 'blablabla', 'id':'sujet2'},
    {'title': "Les hamsters et cochons d'Inde", 'author': 'Sam', 'date': '01/02/17', 'contenu': 'bla', 'id':'sujet3'},
    {'title': 'Les poissons et requins', 'author': 'Gregory', 'date': '02/02/17', 'contenu': 'blablablabla', 'id':'sujet4'}
]

@app.route('/forums', methods=['GET'])
def forum():
    return render_template('forum.html', subjects = subjects)

@app.route('/forums/add', methods=['GET', 'POST'])
def add_subject():
    print request.form

    # Appel de la fonction en POST
    if request.method == 'POST':
        print "Appel POST"

        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        subjects.append(
            {'title': title, 
             'author': author, 
             'date': "01/02/17", 
             'contenu': content, 
             'id': "sujet %d" % (len(subjects))
            }
        )
        return redirect(url_for('forum'))

    # Appel de la fonction en GET
    else:
        print "Appel GET"
        return render_template('formulaire.html')



if __name__ == "__main__":
    app.run()
