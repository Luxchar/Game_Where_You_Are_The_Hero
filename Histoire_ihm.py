from tkinter import*
from PIL import ImageTk, Image
import os

# On crée la fenêtre tkinter
fen= Tk()
dirpath = os.getcwd()
fen.title('Histoire')
fen.geometry("1100x700")

# Images du jeu
desert_nuit= ImageTk.PhotoImage(Image.open(dirpath+"/nuit.png").resize((1100, 600),Image.ANTIALIAS))
desert_jour= ImageTk.PhotoImage(Image.open(dirpath+"/jour.png").resize((1100, 600),Image.ANTIALIAS))

class Text:
    def __init__(self,t,q):
        self.question=q
        self.texte=t

class Recit: # classe à modifier avec un attribut 'texte' pour pouvoir faire mieux le calcul taille
    def __init__(self,texte):
        self.gauche=None
        self.droite=None
        self.texte=texte

#1 er étage
abr=Recit(Text("Vous êtes seul sur une île présumée déserte et livré à vous même","Vous trouvez une gourde étrange par terre, La buvez-vous ?"))
abr.gauche=Recit(Text("Vous continuez donc à marcher en cherchant une oasis","Vous trouvez une fontaine d'eau, décidez-vous de vous en approcher ?"))
abr.droite=Recit(Text("Vous avez bu le contenu de la gourde et vous vous écroulez par terre","Vous vous réveillez quelques heures plus tard et êtes tombé nez à nez avec une sorte de taureau, Restez-vous figé sur place ?"))

# 2 ème étage
abr_temp=abr.gauche
abr_temp.gauche=Recit(Text("Vous rebroussez chemin et voyez une voiture abandonnée au loin","Vous en approchez-vous ?"))
abr_temp.droite=Recit(Text("Vous tombez dans une faille, c'était en fait un mirage !","Vous êtes blessé et saignez beaucoup, décidez-vous de criez à l'aide ?"))
abr_temp2=abr.droite
abr_temp2.gauche=Recit(Text("Le taureau vous a coursé et vous a largement blessé la jambe","Vous êtes conscient de vos blessures décidez-vous de passer la nuit à marcher tout de même ?"))
abr_temp2.droite=Recit(Text("Votre charisme a fait fuir la bête vous pouvez être fier de vous","Vous avez maintenant faim, vous voyez des vers de sable au sol, les mangez-vous ?"))

# 3 ème étage
abr_temp3=abr_temp.gauche
abr_temp3.gauche=Recit(Text("Vous avez fait le choix de ne pas allez voir du côté de la voiture","La chaleur est trop intense, devez-vous vous reposer ?"))
abr_temp3.droite=Recit(Text("Quelle chance ! la voiture n'est en fait pas abandonnée et un charmand fermier vous propose de monter avec lui pour allez chez lui","Acceptez-vous ?"))
abr_temp4=abr_temp.droite
abr_temp4.gauche=Recit(Text("Vous ne criez pas à l'aide","Vous avez un caillou à proximité, décidez-vous de le jeter pour permettre à quelqu'un de vous repérer ?"))
abr_temp4.droite=Recit(Text("Vos cris ont alerté des créatures sauvages, vous avez malheureusement été dévoré",'fin'))
abr_temp5=abr_temp2.gauche
abr_temp5.gauche=Recit(Text("Au lever du jour, une odeur nauséabonde vous réveille, vous regardez au-dessus de votre épaule, vous en déduisez que c'est une odeur de volaille boueuse ","Après un moment d'hésitation vous vous demander si vous avez vraiment le choix de vous nourrir de ces pauvres animaux ?"))
abr_temp5.droite=Recit(Text("Vous avez passé la nuit à marcher vous êtes exténué, mais vous voyez une coulée d'eau à vos pieds","Suivez-vous le cours d'eau ?"))
abr_temp6=abr_temp2.droite
abr_temp6.gauche=Recit(Text("Vous avez fait une impasse sur votre seule source de nourriture, les forces vous manque, vous tombez dans les pommes s'en est finit de vous","fin"))
abr_temp6.droite=Recit(Text("Les vers vous ont bien rassasié mais il vous faut un abris pour la nuit prochaine"," Vous voyez une grotte au loin, y allez-vous ?"))

# 4 ème étage
abr_temp7=abr_temp3.gauche
abr_temp7.gauche=Recit(Text("Vos jambes vous lâchent, vous vous endormissez sur le sol ardent et mourrez paisiblement","fin"))
abr_temp7.droite=Recit(Text("Pendant votre sommeil des cannibales se sont régalé de votre chair, pas de chance !","fin"))
abr_temp8=abr_temp3.droite
abr_temp8.gauche=Recit(Text("Vous avez laissé la voiture filer, vous avez résisté à la déshydratation quelque temps mais la chaleur a eu raison de vous !","fin"))
abr_temp8.droite=Recit(Text("Vous arrivez au pied d'une grange, le fermier vous invite à entrer","Vous y allez ?"))
abr_temp9=abr_temp4.gauche
abr_temp9.gauche=Recit(Text("Personne n'a pu soigner vos blessures vous êtes mort au fond de cette faille","fin"))
abr_temp9.droite=Recit(Text("Le caillou lancé est a heurté un gros rocher qui vous a transformé en crêpe, paix à votre âme","fin"))
abr_temp10=abr_temp5.gauche
abr_temp10.gauche=Recit(Text("Vous épargnez les volailles mais vous mourrez de faim quelque jours plus tard, vous êtes bien la première personne à refuser un kfc","fin"))
abr_temp10.droite=Recit(Text("Les volailles vous régalent mais vous mourrez d'une infection de l'intestin, je savais que le kfc était pas healthy mais à ce point là non","fin"))
abr_temp11=abr_temp5.droite
abr_temp11.gauche=Recit(Text("L'eau vient à vous manquer et mourrez d'épuisement, vous regrettez de ne pas voir regarder kirikou étant petit, vous auriez pu savoir que l'eau était revenue...","fin"))
abr_temp11.droite=Recit(Text("Vous suivez le long du cours d'eau et des sortes de tippies captent votre attention, une sorte d'indigène vous aborde",'Vous lui dites "bonjour" ?'))
abr_temp12=abr_temp6.droite
abr_temp12.gauche=Recit(Text("Vous n'allez pas dans la grotte et faites une escapade à la l'aveuglette, vous vous enlisez dans des sables mouvant et périssez en silence","fin"))
abr_temp12.droite=Recit(Text("Votre escapade dans la grotte est promptement interrompue par un coup de patte d'un ours affamé, il vous a certainement pris pour du miel, une mort sucrée...","fin"))
# 5 ème étage
abr_temp13=abr_temp8.droite
abr_temp13.gauche=Recit(Text("Vous avez offensé le fermier, pour se venger il vous assène un grand coup de fourche sur le haut du crâne, vous succombez...","fin"))
abr_temp13.droite=Recit(Text("Vous partagez un moment de relaxiation et de gaîté avec votre nouvel et ami et dormez comme un bébé","Le lendemain matin le fermier vous propose de vous raccompagner chez vous, acceptez-vous ?"))
abr_temp14=abr_temp11.droite
abr_temp14.gauche=Recit(Text("L'indigène ne vous a pas trouvé poli, il se servira de votre enveloppe charnelle pour un sacrifice vaudou","fin"))
abr_temp14.droite=Recit(Text("L'indigène a pris votre salutation pour une déclaration de guerre, il vous tue.","fin"))

# 6 ème étage
abr_temp15=abr_temp13.droite
abr_temp15.gauche=Recit(Text("Vous refusez, le fermier comprend tout à fait, vous repartez en France en avion vivre votre meilleure vie ","fin"))
abr_temp15.droite=Recit(Text("Vous indiquez d'où vous venez au fermier, il perd espoir au vu de la distance entre votre localisation et votre domicile et décide de vous mettre à la porte","Vous explorez les environs et trouvez une côte avec un bateau à moteur dans l'eau, essayez vous de le conduire ?"))
abr_temp16=abr_temp14.droite

#7 ème étage
abr_temp17=abr_temp15.droite
abr_temp17.gauche=Recit(Text("Vous ne prenez pas le bateau et tentez de rejoindre votre région natale à la nage et mourrez noyé","fin"))
abr_temp17.droite=Recit(Text("Le bateau est doté d'un gps vous permettant de rejoindre les côtes françaises vous êtes sain et sauf !","fin"))

# Fonctions

def recommencer():
    global choix,alterner_image,abr
    choix = []
    alterner_image= 'jour'
    affiche_texte.config(text= abr.texte.texte)
    affiche_question.config(text= abr.texte.question)
    affiche_texte.grid(row=1,column=0)
    affiche_question.grid(row=2,column=0)
    bouton_non.grid(row=3,column=0)
    bouton_oui.grid(row=4,column=0)
    bouton_recommencer.grid_forget()
    img.config(image=desert_jour)

def rep_negative():
    lancer(0,abr)

def rep_positive():
    lancer(1,abr)

def lancer(rep,abr):
    global choix,alterner_image
    if alterner_image == 'jour':
        img.config(image=desert_nuit)
        alterner_image='nuit'
    else:
        img.config(image=desert_jour)
        alterner_image='jour'

    phrase_question=abr
    choix.append(rep)
    temp_choix=choix
    phrase_question= histoire_recur(temp_choix,abr)
    affiche_texte.config(text=phrase_question.texte.texte)
    if phrase_question.texte.question == 'fin':
        affiche_question.grid_forget()
        bouton_non.grid_forget()
        bouton_oui.grid_forget()
        bouton_recommencer.grid(row=2,column=0)
        return
    affiche_question.config(text=phrase_question.texte.question)


def histoire_iter(choix,abr):
    phrase_question,temp_choix=abr,choix
    while temp_choix != []:
        if temp_choix[0] == 0:
            phrase_question = phrase_question.gauche
        else:
            phrase_question = phrase_question.droite
        temp_choix = temp_choix[1:]
    return phrase_question


def histoire_recur(choix,abr):
    if choix == []:
        return abr
    if choix[0] == 0:
        return histoire_recur(choix[1:],abr.gauche)
    else:
        return histoire_recur(choix[1:],abr.droite)

# Hauteur
def hauteur(abr):
    if abr:
        return 1 + max(hauteur(abr.gauche),hauteur(abr.droite))
    return 0

# Taille
def taille(abr):
    if abr:
        return 1 + taille(abr.gauche) + taille(abr.droite)
    return 0

assert hauteur(abr) == 8
assert taille(abr) == 35

# Programme principal
img=Label(image= desert_jour)
img.grid(row=0,column=0)
affiche_texte=Label(fen,text=abr.texte.texte,font='arial 10 bold')
affiche_texte.grid(row=1,column=0)
affiche_question=Label(fen,text=abr.texte.question,font='arial 10 bold')
affiche_question.grid(row=2,column=0)
bouton_non= Button(fen,text='Non',command = rep_negative)
bouton_oui= Button(fen,text='Oui',command = rep_positive)
bouton_non.grid(row=3,column=0)
bouton_oui.grid(row=4,column=0)
bouton_non.config(bg='red')
bouton_oui.config(bg='green')
choix=[]
alterner_image='jour'
bouton_recommencer=Button(fen,text='Recommencer',command= recommencer)
bouton_recommencer.config(bg='green')
fen.mainloop()