import sqlite3

#Fertig
def addAccount(cursor, name):
    user = f"""INSERT INTO accounts (user_id, name, credits) VALUES (NULL, '{name}', 100)"""
    print(user)
    cursor.execute(user)

#Fertig
def addFrage(cursor, frage, antwort1, antwort2, antwort3, antwort4):
    frage = f"""INSERT INTO fragen(id, frage, antworteins, antwortzwei, antwortdrei, antwortvier) VALUES (NULL, '{frage}', '{antwort1}', '{antwort2}', '{antwort3}', '{antwort4}');"""
    print(frage)
    cursor.execute(frage)

#Fertig
def existsid(cursor, user_id):
    userexists = f"""SELECT COUNT(*) FROM accounts WHERE user_id = '{user_id}'"""
    print(userexists)
    for row in cursor.execute(userexists):
        benutzer = row[0]

    if benutzer == 1: #Falls Benutzer = 1 ist, ist die ID vorhanden
        return True
    else:
        return False

#Fertig
def getName(cursor, user_id):
    getname = f"""SELECT name FROM accounts WHERE user_id = '{user_id}'"""
    print(getname)

    for row in cursor.execute(getname):
        username = row[0]
    return username       

#Fertig
def getCredits(cursor, user_id):
    getcredits = f"""SELECT credits FROM accounts WHERE user_id = {user_id}"""
    print(getcredits)

    for row in cursor.execute(getcredits):
        credits = row[0]

    return credits

#Fertig
def addCredits(cursor, user_id, credits):
    setCredits(cursor, user_id, getCredits(cursor, user_id) + credits)
#Fertig
def removeCredits(cursor, user_id, credits):
    setCredits(cursor, user_id, getCredits(cursor, user_id) - credits)

#Fertig
def setCredits(cursor, user_id, credits):
    setcredits = f"""UPDATE accounts SET credits = {credits} WHERE user_id = '{user_id}';"""
    cursor.execute(setcredits)

def usernameindb(cursor, name):
    userexists = f"""SELECT COUNT(*) FROM accounts WHERE name = '{name}'"""
    useravaible = ""
    for row in cursor.execute(userexists):
        useravaible = row[0]
    if useravaible >= 1: #Falls Benutzer = 1 ist, ist der Benutzername mehr als einmal vorhanden
        return True
    else:
        return False


def getrightAnswer(cursor, frageid):
    getanswer = f"""SELECT richtigeantwort FROM fragen WHERE id = '{frageid}'"""
    print(getanswer)

    for row in cursor.execute(getanswer):
        antwort = row[0]

    return antwort

connection = sqlite3.connect("wwm.db")

cursor = connection.cursor()

tabelle_accounts = """
CREATE TABLE IF NOT EXISTS accounts ( 
user_id INTEGER PRIMARY KEY, 
name VARCHAR(30), credits INTEGER);"""
cursor.execute(tabelle_accounts)

tabelle_accounts = """
CREATE TABLE IF NOT EXISTS fragen(
id INTEGER PRIMARY KEY, frage VARCHAR(255),
richtigeantwort VARCHAR(255), antwortzwei VARCHAR(255),
antwortdrei VARCHAR(255), antwortvier VARCHAR(255));"""
cursor.execute(tabelle_accounts)

if usernameindb(cursor, "adsasdsd"):
    print(123)
else:
    print("abc")

connection.commit()

frageid = int(input("Frage ID? > "))

print(getrightAnswer(cursor, frageid))


print("db updated...")
connection.close()