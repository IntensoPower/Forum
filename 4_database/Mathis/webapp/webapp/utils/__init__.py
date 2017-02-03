
import MySQLdb

mysql_host = '192.168.55.55'
mysql_user = 'mathis'
mysql_passwd = ''
mysql_db = 'forum'

db = MySQLdb.connect(host=mysql_host,
      user=mysql_user,
      passwd=mysql_passwd,
      db=mysql_db,
      charset='utf8')

cursor = db.cursor()

def insert_database(new_subject):
    print new_subject
    cursor.execute("""insert into subjects (title, author, content, writeDate) values(%(title)s, %(author)s, %(content)s, %(writeDate)s)""", new_subject)
    db.commit()

def select_database():
    cursor.execute("select * from subjects")
    lignes = cursor.fetchall()

    subjects = []
    
    # TODO
    for ligne in lignes:
        #print ligne

        subjects.append(
            {'title': ligne[1], 
             'author': ligne[2], 
             'date': ligne[3], 
             'contenu': ligne[4], 
             'id': "sujet %d" % ligne[0]
            }
        )

    return subjects

def delete_database():
    pass

def update_database():
    pass

if __name__ == '__main__':
    new_subject = {
        'title': 'salut', 
        'author': 'moi', 
        'writeDate': "01/02/17", 
        'content': 'content'
    }
    insert_database(new_subject)