import tkinter as tk
import random as rd
import time

colors=["blue","red","orange","black","brown","green","white","yellow"]

def choixcomputer():
    Tcomputer=[0]*5
    for i in range(5):
        choice=rd.randint(0,7)
        Tcomputer[i]=colors[choice]
    return(Tcomputer)

class Jeu(tk.Tk):
    def __init__(self,difficulte):
        tk.Tk.__init__(self)
        self.size=610
        self.diametre=40
        self.x=10
        self.y=10
        self.pion=0
        self.tour=1
        self.couleur='none'
        self.difficulte=difficulte
        self.ordinateur=choixcomputer()
        self.depart=time.time()
        self.Tcouleur=['Rien']*60
        self.scene_principale()

    def scene_principale(self):
        self.canv=tk.Canvas(self,bg='beige',height=self.size, width=self.size)
        self.canv.pack(side=tk.LEFT)
        self.rouge=tk.Button(self,bg='red',height=3,width=7,command=self.cercle_rouge)
        self.rouge.pack()
        self.bleu=tk.Button(self,height=3,width=7,bg='blue',command=self.cercle_bleu)
        self.bleu.pack()
        self.orange=tk.Button(self,height=3,width=7,bg='orange',command=self.cercle_orange)
        self.orange.pack()
        self.noir=tk.Button(self,height=3,width=7,bg='black',command=self.cercle_noir)
        self.noir.pack()
        self.marron=tk.Button(self,height=3,width=7,bg='brown',command=self.cercle_marron)
        self.marron.pack()
        self.vert=tk.Button(self,height=3,width=7,bg='green',command=self.cercle_vert)
        self.vert.pack()
        self.blanc=tk.Button(self,height=3,width=7,bg='white',command=self.cercle_blanc)
        self.blanc.pack()
        self.jaune=tk.Button(self,height=3,width=7,bg='yellow',command=self.cercle_jaune)
        self.jaune.pack()
        self.annuler=tk.Button(self,height=4,width=7,text='Annuler',bg='light grey',font='Times 10 bold',command=self.annuler)
        self.annuler.pack()
        self.quitter=tk.Button(self,height=5,width=7,text='Quitter',bg='black',fg='white',font='Times 10 bold',command=self.retour)
        self.quitter.pack()

    def cercle_couleur(self):
        self.canv.create_oval(self.x, self.y,self.x+self.diametre,self.y+self.diametre,fill=self.couleur)
        self.x+=50
        tour_tableau=self.tour-1
        self.Tcouleur[tour_tableau*5+self.pion]=self.couleur
        self.pion+=1
        if self.pion==5:
            self.dessin_test(50,self.Tcouleur,self.tour-1,self.ordinateur,self.canv)
            self.tour+=1
            self.pion=0
        
            
    def cercle_rouge(self):
        self.couleur='red'
        self.cercle_couleur()
        
    def cercle_bleu(self):
        self.couleur='blue'
        self.cercle_couleur()

    def cercle_orange(self):
        self.couleur='orange'
        self.cercle_couleur()

    def cercle_noir(self):
        self.couleur='black'
        self.cercle_couleur()

    def cercle_marron(self):
        self.couleur='brown'
        self.cercle_couleur()

    def cercle_vert(self):
        self.couleur='green'
        self.cercle_couleur()

    def cercle_blanc(self):
        self.couleur='white'
        self.cercle_couleur()

    def cercle_jaune(self):
        self.couleur='yellow'
        self.cercle_couleur()

        
    def test_couleurs(self,T1,posT1,T2):
        T1bis=[0]*5
        posT1=posT1*5
        c=0
        for i in range (posT1,posT1+5):
            T1bis[c]=T1[i]
            c+=1
        
        Ttest=["Rien"]*5
        for i in range(5):
            if T1bis[i]==T2[i]:
                Ttest[i]="black"
            else:
                for j in range(5):
                    if T1bis[i]==T2[j]:
                        Ttest[i]="white"
        return(Ttest)
        
    def dessin_test(self,taille,T1,posT1,T2,canv):
        if self.difficulte=='Facile':
            self.Ttest=self.test_couleurs(T1,posT1,T2)
        elif self.difficulte=='Moyen':
            self.Ttest=self.Mode_moyen(self.test_couleurs(T1,posT1,T2))
        elif self.difficulte=='Difficile':
            self.Ttest=self.Mode_difficile(self.test_couleurs(T1,posT1,T2))
        self.x+=taille*2
        self.canv=canv
        for i in range(5):
            if self.Ttest[i]=="Rien" and self.difficulte=='Difficile':
                self.x+=taille
            elif self.Ttest[i]=="Rien":
                self.canv.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill='white')
                self.canv.create_line(self.x,self.y,self.x+self.diametre, self.y+self.diametre,fill='red',width=10)
                self.canv.create_line(self.x,self.y+self.diametre,self.x+self.diametre,self.y,fill='red',width=10)
                self.x+=taille
            else:
                self.canv.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill=self.Ttest[i])
                self.x+=taille
        if self.Ttest==['black']*5:
            self.chrono=time.time()-self.depart
            self.victoire()
        elif self.tour==12:
            self.defaite()
        self.x=10
        self.y+=taille
        
    def annuler(self):
        if self.pion!=0:
            self.x-=50
            self.pion-=1
            self.canv.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill='beige',outline='beige')
        
    def victoire(self):
        self.canv.destroy()
        self.rouge.destroy()
        self.bleu.destroy()
        self.orange.destroy()
        self.vert.destroy()
        self.jaune.destroy()
        self.marron.destroy()
        self.noir.destroy()
        self.blanc.destroy()
        self.annuler.destroy()
        self.quitter.destroy()
        self.canvvictoire=tk.Canvas(self,bg='beige',height=500, width=self.size)
        self.canvvictoire.pack()
        self.textevictoire=self.canvvictoire.create_text(305,250,text='Bravo, tu as gagné !!!',font='Papyrus 40 bold')
        self.textestat=self.canvvictoire.create_text(80,320,text='Victoire en',font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(170,320,text=self.tour,font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(220,320,text='tours',font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(290,320,text='et en',font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(335,320,text=round(self.chrono//60),font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(400,320,text='minute(s)',font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(475,320,text=round(self.chrono%60),font='Papyrus 20')
        self.textestat=self.canvvictoire.create_text(550,320,text='secondes',font='Papyrus 20')
        self.retour=tk.Button(self, text='Retour au menu principal',font='Papyrus 15 bold', bg='light grey',height=1,width=40,command=self.retour)
        self.retour.pack()

    def defaite(self):
        self.canv.destroy()
        self.rouge.destroy()
        self.bleu.destroy()
        self.orange.destroy()
        self.vert.destroy()
        self.jaune.destroy()
        self.marron.destroy()
        self.noir.destroy()
        self.blanc.destroy()
        self.annuler.destroy()
        self.quitter.destroy()
        self.canvdefaite=tk.Canvas(self,bg='beige',height=500, width=self.size)
        self.retour=tk.Button(self, text='Retour au menu principal',font='Papyrus 15 bold', bg='light grey',height=1,width=40,command=self.retour)
        self.detail=tk.Button(self, text='Details de la partie',font='Papyrus 15 bold', bg='light blue',height=1,width=40,command=self.detail_partie)
        self.canvdefaite.pack()
        self.detail.pack()
        self.retour.pack()
        self.textedefaite=self.canvdefaite.create_text(305,200,text='Tu as perdu ...',font='Papyrus 40 bold')
        self.textestat=self.canvdefaite.create_text(305,300,text="Tu n'as malheureusement pas trouvé le\ncode en 12 tours, il s'affiche actuellement :",font='Papyrus 20')    
        self.x=60
        self.y=370
        self.diametre=80
        for i in range(5):
            self.canvdefaite.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill=self.ordinateur[i])
            self.x+=100
            
        
    def detail_partie(self):
        self.canvdefaite.destroy()
        self.detail.destroy()
        self.retour.destroy()
        self.canvdetail=tk.Canvas(self,bg='beige',height=570, width=self.size)
        self.bouton=tk.Button(self, text='Retour au menu principal',font='Papyrus 15 bold', bg='light grey',height=1,width=40,command=self.retourdetail)
        self.canvdetail.pack()
        self.bouton.pack()
        self.x=110
        self.y=60
        self.diametre=60
        for i in range(5):
            self.canvdetail.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill=self.ordinateur[i])
            self.x+=80
        self.canvdetail.create_text(305,30,text='Code à trouver :',font='Papyrus 20 bold underline')
        self.x=140
        self.y=150
        self.diametre=25
        for i in range(12):
            if self.Tcouleur[i*5]=='Rien':
                    break
            self.canvdetail.create_text(70,self.y+12,text='Tour n°',font='Papyrus 10')
            self.canvdetail.create_text(100,self.y+12,text=i+1,font='Papyrus 10')
            self.canvdetail.create_text(110,self.y+12,text=':',font='Papyrus 10')
            for j in range(5):
                self.canvdetail.create_oval(self.x,self.y,self.x+self.diametre,self.y+self.diametre,fill=self.Tcouleur[i*5+j])
                self.x+=35
            self.dessin_test(35,self.Tcouleur,i,self.ordinateur,self.canvdetail)
            self.x=140
            
        
    def retour(self):
        self.destroy()
        app=Mdj()
        app.title("Mastermind")
        app.mainloop()
        

    def retourdetail(self):
        self.destroy()
        app=Mdj()
        app.title("Mastermind")
        app.mainloop()
    
    def Mode_moyen(self,testcouleur):
        Tmoyen=['Rien']*5
        c=0
        for i in range(5):
            if testcouleur[i]=="black":
                Tmoyen[c]='black'
                c+=1
        for i in range(5):
            if testcouleur[i]=="white":
                Tmoyen[c]='white'
                c+=1    
        return(Tmoyen)

    def Mode_difficile(self,testcouleur):
        Tdifficile=['Rien']*5
        c=0
        for i in range(5):
            if testcouleur[i]=="black":
                Tdifficile[c]='black'
                c+=1
        return(Tdifficile)
        
class Mdj(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.size=610
        self.menu_principal()

    def menu_principal(self):
        self.canv=tk.Canvas(self, bg="beige", height=400, width=self.size)
        self.canv.pack()
        self.titre=self.canv.create_text(305,60,text='Mastermind',font='Papyrus 40 bold underline')
        self.mode_de_jeu=self.canv.create_text(305,225,text='Choisis ta difficulté :',font='Papyrus 25 bold')
        self.Bregles=tk.Button(self, text='Règles',font='Papyrus 15 bold', bg='light blue',fg='black',height=2,width=9,command=self.regles)
        self.Bregles.pack(side=tk.LEFT)
        self.difficile=tk.Button(self,text='Difficile',font='Papyrus 15 bold',fg='white', bg='black',height=2,width=9,command=self.Difficile)
        self.difficile.pack(side=tk.RIGHT)
        self.moyen=tk.Button(self,text='Moyen',font='Papyrus 15 bold',fg='white', bg='grey',height=2,width=9, command=self.Moyen)
        self.moyen.pack(side=tk.RIGHT)
        self.facile=tk.Button(self,text='Facile',font='Papyrus 15 bold',fg='black', bg='white',height=2,width=9,command=self.Facile)
        self.facile.pack(side=tk.RIGHT)

    def regles(self):
        self.Detruire_menu()
        self.canv=tk.Canvas(self, bg="beige", height=560, width=800)
        self.canv.pack(side=tk.LEFT)
        self.titre=self.canv.create_text(400,25,text='Règles',font='Papyrus 30 bold underline')
        self.regles=self.canv.create_text(400,310,text="Mastermind est un jeu de société pour deux joueurs dont le but est de trouver un code secret.\nDans le Mastermind numérique, l’ordinateur détermine aléatoirement le code secret composé\nde 5 pions de 8 couleurs différentes (blanc, noir, orange, bleu, vert, rouge, marron, jaune).\nVous devez trouver la combinaison composée de 5 pions de couleur, dans le même ordre.\n\nUne fois une rangée de 5 pions placés, l’ordinateur vous indiquera:\n-les pions de la bonne couleur et bien placés avec des pions noirs\n-les pions de la bonne couleur mais mal placés avec des pions blancs\n-les pions d’une couleur qui n’est pas dans le code en laissant une case vide sans pion\n\nLe joueur gagne s’il trouve la bonne combinaison en 12 tours ou moins et perd sinon. \n\nLe mode facile de notre jeu vous indique si les pions sont de la bonne couleur et\nbien placés en mettant les pions noirs et blancs dans l’ordre.\nQuant au mode moyen, il vous indique le nombre de pions noirs et de pions blancs.\nEnfin, le mode difficile vous indique seulement le nombre de pions noirs.",font='Papyrus 15')        
        self.retour=tk.Button(self, text='Retour',font='Times 10 bold', bg='light grey',height=37,width=5,command=self.Fretour)
        self.retour.pack()

    def Detruire_menu(self):
        self.canv.destroy()
        self.Bregles.destroy()
        self.facile.destroy()
        self.moyen.destroy()
        self.difficile.destroy()
        
    def Fretour(self):
        self.destroy()
        Mdj()

    def Facile(self):
        self.destroy()
        app=Jeu('Facile')
        app.title("Mastermind")
        app.mainloop()

    def Moyen(self):
        self.destroy()
        app=Jeu('Moyen')
        app.title("Mastermind")
        app.mainloop()

    def Difficile(self):
        self.destroy()
        app=Jeu('Difficile')
        app.title("Mastermind")
        app.mainloop()
        
if __name__=="__main__":
    app=Mdj()
    app.title("Mastermind")
    app.mainloop()
