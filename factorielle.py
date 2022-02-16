from cgi import print_form
from os import system
from socket import SO_DONTROUTE, SO_ERROR
from winsound import MessageBeep

def factorielle() :
    
    TITRE= "FACTORIEL".center(50,"-")
    print(TITRE)
    print("\n")

    try : 
     factoriel=int (input("veuiller entrer un nombre\n>-->".title()))
     resul_fact = 1
     for i in range (1,factoriel + 1) : 
         resul_fact=resul_fact*i
     print("LE FACTORIEL DE CE NOMBRE EST "+ str(resul_fact))
    except ValueError :
      MessageBeep(SO_DONTROUTE)
      print("ERREUR DE SAISE")
      print("--->veuiller entrer un nombre\n".title())
      factorielle()
      

def continuer() :
 try:
   rep=int(input("voulez vous continuer ? \n>--> 1.OUI\n>--> 2.NON\n>-->\t".title()))
   if rep == 1 :
       system("cls")
       factorielle()
       continuer()
   elif rep == 2 :
        exit()
   elif rep!=1 and rep!=2 :
       print ("ERREUR DE SAISE\n")
       continuer()
 except ValueError : 
     MessageBeep(SO_ERROR)
     print("erreur de saisie\n".capitalize)
     print("veuiller entrer des nombres".title())
     continuer()
       
factorielle()
continuer ()   
   
   
    

