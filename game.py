import random
import os
import sqlite3
import time
from os import system
import platform

#Fertig
def addAccount(cursor, name, connection):
    user = f"""INSERT INTO accounts (user_id, name, credits) VALUES (NULL, '{name}', 100)"""
    cursor.execute(user)
    connection.commit()

#Fertig
def addFrage(cursor, frage, antwort1, antwort2, antwort3, antwort4, connection):
    frage = f"""INSERT INTO fragen(id, frage, richtigeantwort, antwortzwei, antwortdrei, antwortvier) VALUES (NULL, '{frage}', '{antwort1}', '{antwort2}', '{antwort3}', '{antwort4}');"""
    cursor.execute(frage)
    connection.commit()

#Fertig
def existsid(cursor, user_id):
    userexists = f"""SELECT COUNT(*) FROM accounts WHERE user_id = '{user_id}'"""
    for row in cursor.execute(userexists):
        benutzer = row[0]

    if benutzer == 1: #Falls Benutzer = 1 ist, ist die ID vorhanden
        return True
    else:
        return False

#Fertig
def getName(cursor, user_id):
    getname = f"""SELECT name FROM accounts WHERE user_id = '{user_id}'"""

    for row in cursor.execute(getname):
        username = row[0]
    return username       

#Fertig
def getCredits(cursor, user_id):
    getcredits = f"""SELECT credits FROM accounts WHERE user_id = {user_id}"""

    for row in cursor.execute(getcredits):
        credits = row[0]
    return credits

#Fertig
def addCredits(cursor, user_id, credits, connection):
    setCredits(cursor, user_id, getCredits(cursor, user_id) + credits, connection)
    connection
#Fertig
def removeCredits(cursor, user_id, credits, connection):
    setCredits(cursor, user_id, getCredits(cursor, user_id) - credits, connection)
    connection

#Fertig
def setCredits(cursor, user_id, credits, connection):
    setcredits = f"""UPDATE accounts SET credits = {credits} WHERE user_id = '{user_id}';"""
    cursor.execute(setcredits)
    connection.commit()

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

    for row in cursor.execute(getanswer):
        antwort = row[0]

    return antwort

def getazwei(cursor, frageid):
    getanswer = f"""SELECT antwortzwei FROM fragen WHERE id = '{frageid}'"""
    for row in cursor.execute(getanswer):
        antwort = row[0]
    return antwort

def getadrei(cursor, frageid):
    getanswer = f"""SELECT antwortdrei FROM fragen WHERE id = '{frageid}'"""
    for row in cursor.execute(getanswer):
        antwort = row[0]
    return antwort

def getavier(cursor, frageid):
    getanswer = f"""SELECT antwortvier FROM fragen WHERE id = '{frageid}'"""
    for row in cursor.execute(getanswer):
        antwort = row[0]
    return antwort

def smtinfragen(cursor):
    userexists = f"""SELECT COUNT(*) FROM fragen"""
    fragenin = ""
    for row in cursor.execute(userexists):
        fragenin = row[0]
    if fragenin >= 1: #Falls Fragen = 1 ist, ist der Benutzername mehr als einmal vorhanden
        return True
    else:
        return False

def getFragenInt(cursor):
    userexists = f"""SELECT COUNT(*) FROM fragen"""
    fragenin = ""
    for row in cursor.execute(userexists):
        fragenin = row[0]
    
    return fragenin


def getFrage(cursor, wfrageid):
    getcredits = f"""SELECT frage FROM fragen WHERE id = {wfrageid}"""
    for row in cursor.execute(getcredits):
        frage = row[0]
    return frage


def initdb(cursor, connection):
    if not smtinfragen(cursor):
        #Admin User
        addAccount(cursor, "Admin", connection)
        #Alle Fragen einfügen mit Methoden
        addFrage(cursor, "Wenn das Wetter gut ist, wird der Bauer bestimmt den Eber, das Ferkel und …?", "die Sau rauslassen", "einen draufmachen", "die Nacht durchtechen", "auf die Kacke hauen", connection)
        addFrage(cursor, "Welche Gegenstände können in den Geschichten des Orient fliegen?", "Teppiche", "Tische", "Münzen", "Häuser", connection)
        addFrage(cursor, "Welches Tier kann seine Hautfarbe an seine Umgebung anpassen?", "Chamäleon", "Ringelnatter", "Waldkautz", "Ameisen", connection)
        addFrage(cursor, "Welche Figur wurde von Karl May erschaffen?", "Winnetou", "Asterix", "Pluto", "Pater Brown", connection)
        addFrage(cursor, "Wovor fürchtet sich der Autobesitzer?", "Kolbenfresser", "Ventiltrinker", "Reifenmümmler", "Schaltungsmampfer", connection)
        addFrage(cursor, "Wie nennt man die Mitte eines Tornados?", "Auge", "Nase", "Mund", "Ohr", connection)
        addFrage(cursor, "Was sägen Max und Moritz voller Tücke an, um dem Schneider Böck einen Streich zu spielen?", "Brücke", "Stuhlbein", "Leiter", "Krückstock", connection)
        addFrage(cursor, "Wen brauchen viele Parasiten zum Überleben?", "Wirt", "Kneipier", "Oberkellner", "Barkeeper", connection)
        addFrage(cursor, "Wie heißt eine religiöse Stätte des Judentums in Jerusalem?", "Klagemauer", "Trauermauer", "Tempelmauer", "Schlossmauer", connection)
        addFrage(cursor, "Ein berühmter Hurricane der in New Orleans wütete heißt…? ", "Catrina", "Melissa", "Josephine", "Mariah", connection)
        addFrage(cursor, "Wer verrät der Königin, dass Schneewitchen bei den sieben Zwegen lebt?", "Spiegel", "Focus", "Spiegel", "Bäckerblume", connection)
        addFrage(cursor, "Was kommt in den griechischen Salat", "Feta", "Töchta", "söne", "Mütta", connection)
        addFrage(cursor, "Wobei handelt es sich um ein Säugetier, das auch schlangen jagen kann?", "Mungo", "Mundorine", "Bunune", "Upfel", connection)
        addFrage(cursor, "Welcher dieser Vögel gibt es wirklich?", "Klunkerkranich", "Strasswachtel", "Brillantenschnepfe", "Opalsumpfhuhn", connection)
        addFrage(cursor, "Was gab es 1896 beiden ersten Olympischen Spielen der Neuzeit nicht", "Goldmedalien", "Gewinner", "Zuschauer", "Teilnehmer", connection)

        print("init complete...")
        connection.commit()

def start():
    global connection
    global cursor    
    connection = sqlite3.connect("wwm.db")
    cursor = connection.cursor()
    tabelle_accounts = "CREATE TABLE IF NOT EXISTS accounts (user_id INTEGER PRIMARY KEY, name TEXT, credits INTEGER);"
    cursor.execute(tabelle_accounts)
    tabelle_accounts = "CREATE TABLE IF NOT EXISTS fragen(id INTEGER PRIMARY KEY, frage TEXT,richtigeantwort TEXT, antwortzwei TEXT,antwortdrei TEXT, antwortvier TEXT);"
    cursor.execute(tabelle_accounts)
    connection.commit()
    initdb(cursor, connection)

def close():
    connection.close()




#
# Game start!
#

header = """
:::       ::: :::       ::: ::::    ::::  
:+:       :+: :+:       :+: +:+:+: :+:+:+ 
+:+       +:+ +:+       +:+ +:+ +:+:+ +:+ 
+#+  +:+  +#+ +#+  +:+  +#+ +#+  +:+  +#+ 
+#+ +#+#+ +#+ +#+ +#+#+ +#+ +#+       +#+ 
 #+#+# #+#+#   #+#+# #+#+#  #+#       #+# 
  ###   ###     ###   ###   ###       ### 

     Wer wird Millionär? | Version 1.0
"""
prompt = "» "


if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

hadfragen = []

def getrandomFrage(hadfragen):
    inproc = True
    while inproc:
        getrandomid = random.randint(1, getFragenInt(cursor))
        
        if getrandomid not in hadfragen:
            hadfragen.append(getrandomid)
            inproc = False
            return getrandomid


def checkwin():
    if fragecounter >= 12:
        return True

def game():
    global fragecounter
    global frageid
    global fragestr
    global aeins
    global azwei
    global adrei
    global avier
    global avaibleantwort

    avaibleantwort = []

    fragecounter = 1
    print("Das Spiel wird nun gestartet!")
    ingame = True
    while ingame:
        stepone = True
        while stepone:
            frageid = getrandomFrage(hadfragen)
            time.sleep(2)
            
            fragestr = getFrage(cursor, frageid)
            
            aeins = getrightAnswer(cursor, frageid)
            azwei = getazwei(cursor, frageid)
            adrei = getadrei(cursor, frageid)
            avier = getavier(cursor, frageid)

            avaibleantwort = [aeins, azwei, adrei, avier]
            random.shuffle(avaibleantwort)

            print(f"""
            Frage #{fragecounter}: {fragestr}

            A: {avaibleantwort[0]}
            B: {avaibleantwort[1]}
            C: {avaibleantwort[2]}
            D: {avaibleantwort[3]}
            
            """)
            stepone = False
        steptwo = True
        while steptwo:
            print("Welche antwort willst du einloggen? [A, B, C, D]")
            personalantwort = input(prompt)
            if personalantwort.lower() == "a":
                if avaibleantwort[0] == getrightAnswer(cursor, frageid):
                    if checkwin():
                        steptwo = False
                        stepone = False
                        ingame = False
                        print(header)
                        print("Du hast gewonnen!")
                        time.sleep(1000)
                        exit()
                    print("Du hast die Frage erfolgreich richtig beantwortet!")
                    fragecounter += 1
                    steptwo = False
                    ingame = True
                else:
                    print("Die Frage wurde leider Falsch geantwortet. Das Spiel ist nun vorbei!")
                    steptwo = False
                    ingame = False
                    time.sleep(10)
                    #exit()
            elif personalantwort.lower() == "b":
                if avaibleantwort[1] == getrightAnswer(cursor, frageid):
                    if checkwin():
                        steptwo = False
                        stepone = False
                        ingame = False
                        print(header)
                        print("Du hast gewonnen!")
                        time.sleep(1000)
                        exit()                    
                    print("Du hast die Frage erfolgreich richtig beantwortet!")
                    fragecounter += 1
                    steptwo = False
                    ingame = True
                else:
                    print("Die Frage wurde leider Falsch geantwortet. Das Spiel ist nun vorbei!")
                    steptwo = False
                    ingame = False
                    time.sleep(10)
                    #exit()
            elif personalantwort.lower() == "c":
                if avaibleantwort[2] == getrightAnswer(cursor, frageid):
                    if checkwin():
                        steptwo = False
                        stepone = False
                        ingame = False
                        print(header)
                        print("Du hast gewonnen!")                            
                        time.sleep(1000)
                        exit()                
                    print("Du hast die Frage erfolgreich richtig beantwortet!")
                    fragecounter += 1
                    steptwo = False
                    ingame = True
                else:
                    print("Die Frage wurde leider Falsch geantwortet. Das Spiel ist nun vorbei!")
                    steptwo = False
                    ingame = False
                    time.sleep(10)
                    #exit()
            elif personalantwort.lower() == "d":
                if avaibleantwort[3] == getrightAnswer(cursor, frageid):
                    if checkwin():
                        steptwo = False
                        stepone = False
                        ingame = False
                        print(header)
                        print("Du hast gewonnen!")                        
                        time.sleep(1000)
                        exit()                    
                    print("Du hast die Frage erfolgreich richtig beantwortet!")
                    fragecounter += 1
                    steptwo = False
                    ingame = True
                else:
                    print("Die Frage wurde leider Falsch geantwortet. Das Spiel ist nun vorbei!")
                    steptwo = False
                    ingame = False
                    time.sleep(10)
                    #exit()
            else:
                print("Upss da ist wohl ein Fehler aufgetreten")





start()
menu = True
while menu:
    print(header)
    print("""
    Was willst du machen?
    [1] Account erstellen
    [2] Spiel starten
    [3] Spiel beenden

    """)
    wasmachen = input(prompt)
    if wasmachen == "1":
        os.system(clear)
        print("Diese funktion wird erst später hinzugefügt!")
    elif wasmachen == "2":
        os.system(clear)
        menu = False
        print("Wie lautet dein Benutzer ID?")
        userid = input(prompt)
        time.sleep(0.5)
        print("Wie lautet dein Benutername?")
        username = input(prompt)
        time.sleep(0.5)
        print("Du wirst nun angemeldet...")
        if getName(cursor, userid) == username:
            print("Du hast dich erfolgreich angemeldet!")
            game()
        else:
            print("Deine Anmeldenamen sind leider falsch!")
            time.sleep(3)
            menu = True



    elif wasmachen == "3":
        os.system(clear)
        print("Tschüss!")
        exit()
