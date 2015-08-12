#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
argent= 0
questions = [
    ["Quel mammifère pond des oeufs ?","la girafe","la chauve-souris","l'ornithorynque" ,"la poule","C" ],
    ["en quelle année est mort Nelson Mandela" ,"2011","2013","2012","2014","B"],
    ["Qui était le Dieu suprême de la Grèce Antique ", " zeus", "poseidon" ,"hermes","neptune","A" ],
    ["Que signifie pterodactyle ", "aile munie de doigts","animal sanguinaire","séparé du monde"," oiseau sans plume","C"],
    [" Combien y a-t-il d'étoiles dans notre galaxie ?","300 millions","300 trillions","300 milliards","300 milles","C"],
    [" quel est le seul organe du corps humain où le sang ne coule pas ", "les ongles", "les dents", "les cheveux","l'œil","C"],
    ["quelle est la couleur de la langue de la girafe "," bleue" ,"orange" , "rose" ,"noire" , "A"],
    ["combien l'oeil humain peut il capter d'images par seconde", "64", "24","45" ,"100" ,"B"],
    ["quel drapeau contient 6 étoiles ","américain" ,"australien" ,"brésillien" ,"indien" ,"B"],
    ["le quel de ces animaux n'est pas présent en afrique", "le lion","la panthère","l'éléphant","le tigre","D"],
  ]
pointeur = ["<==" ,"", "","","","","","","","",""]
#_________________________________________fonction d'affichage____________________________________________
def affichage(question, e , pointeur):
    print "        ________________________________________________________________________"
    print "1000$",pointeur[10]," |                                                                      "
    print "900 $",pointeur[9]," |                                                                      "
    print "800 $",pointeur[8]," |                                                                      "
    print "700 $",pointeur[7]," | ",question[e][0],"                                    "
    print "600 $",pointeur[6]," |                                                                      "
    print "500 $",pointeur[5]," |                                                                      "
    print "400 $",pointeur[4]," |_______________________________________________________________________"
    print "300 $",pointeur[3]," | a)",question[e][1],"                b)",question[e][2],"          "
    print "200 $",pointeur[2]," |_______________________________________________________________________"
    print "100 $",pointeur[1]," | c)",question[e][3],"         d )",question[e][4],"                "
    print "0$ ",pointeur[0],"|________________________________________________________________________"
    
#______________________________________________programme principal_____________________________________________
while 1==1: 
    print"                _                                             "
    print"               (_)                                            "
    print"   __ _  _   _  _                                             "
    print"  / _` || | | || |                                            "
    print" | (_| || |_| || |                                            "
    print"  \__, | \__,_||_|                                            "
    print"     | |             _                                        "
    print"     |_|            | |                                       "
    print" __   __ ___  _   _ | |_                                      "
    print" \ \ / // _ \| | | || __|                                     "
    print"  \ V /|  __/| |_| || |_                                      "
    print"   \_/  \___| \__,_| \__|                                     "
    print"   __ _   __ _   __ _  _ __    ___  _ __                      "
    print"  / _` | / _` | / _` || '_ \  / _ \| '__|                     "
    print" | (_| || (_| || (_| || | | ||  __/| |                        "
    print"  \__, | \__,_| \__, ||_| |_| \___||_|                        "
    print"   __/ |         __/ |                                        "
    print"  |___/         |___/                                         "
    print"      _                         _  _  _  _                    "
    print"     | |                       (_)| || |(_)                   "
    print"   __| |  ___  ___   _ __ ___   _ | || | _   ___   _ __   ___ "
    print"  / _` | / _ \/ __| | '_ ` _ \ | || || || | / _ \ | '_ \ / __| "
    print" | (_| ||  __/\__ \ | | | | | || || || || || (_) || | | |\__ \ " 
    print"  \__,_| \___||___/ |_| |_| |_||_||_||_||_| \___/ |_| |_||___/ "

    n=raw_input("commencer ?")
    pt=0

    if n == "non":
                exit()
    else:
        n == "oui"
    os.system("cls")
    g=0
    argent=0
    i=0
    pointeur = ["<==" ,"", "","","","","","","","",""]
    while (i < 10) and (g==0):
        affichage(questions,i,pointeur)
        rep = raw_input ( "Votre réponse :")
        
        while (rep.upper() not
               in ['A','B','C','D']):
            rep = raw_input ( "La réponse est de la forme a, b, c ou d :")
        os.system("cls")
        if rep.upper() == questions[i][5]:
            argent+= 100
            print" bonne réponse tu as ",argent," $"
            pointeur[i+1] = pointeur[i]
            pointeur[i] = ""
        else :
            print " tu as perdu!! bye bye !! "
            pointeur = ["<==" ,"", "","","","","","","","",""]
            argent = 0
            l= raw_input("tape Q to exit or enter to continue")
            if l.upper() == "Q" : 
                exit ()
            else:
                g=1
            os.system("cls")
        i+=1
    if g==0:    
        print " mabrouk !! 3al faza koul chalbou9 hehe :D"
              

        l= raw_input("tape Q to exit or enter to continue")
        if l.upper() == "Q" : 
            exit ()
