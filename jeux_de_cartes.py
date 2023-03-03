from random import *
#Creation du jeu de cartes
def crea_jeu():
    jeu=[]
    oranges=[0 for i in range(4)]
    vertes=[i for i in range(1,11)]
    violettes=[i*10 for i in vertes if i%2!=0]
    violettes=violettes*2
    for i in vertes:
        jeu.append([1,i])
    for i in violettes:
        jeu.append([0,i])
    for i in oranges:
        jeu.append([2,i])
    return(jeu)
    
#Distribution aleatoire du jeu de cartes aux deux joueurs
def distribue(jeu):
    jeu1,jeu2=[],[]
    while len(jeu)!=0:
        a=randint(0,len(jeu)-1)
        jeu1.append(jeu[a])
        del jeu[a]
        b=randint(0,len(jeu)-1)
        jeu2.append(jeu[b])
        del jeu[b]
    return(jeu1,jeu2)
    
#Retourne la carte gagnante parmi les deux passees en parametres
def pli(carte1,carte2):
    """carte1 et carte2:listes de la forme[Couleur,Valeur]"""
    """retourne une liste:carte ayant remporte le pli"""
    """retourne None en cas d'egalite"""
    if carte1==carte2:
        return(None)
    elif carte1[0]>carte2[0]:
        return(carte1)
    elif carte1[0]<carte2[0]:
        return(carte2)
    elif carte1[0]==carte2[0]:
        if carte1[1]>carte2[1]:
            return(carte1)
        elif carte1[1]<carte2[1]:
            return(carte2)

#Fonction de jeu d'une carte par le joueur 1
def jouer_carte1(main) :
    return(main[0])
    

        
#Fonction de jeu d'une carte par le joueur 2
def jouer_carte2(main):
    liste1=[i[1] for i in main if i[0]==1]
    liste2=[i[1] for i in main if i[0]==0]
    for i in main:
        if i[0]==2:
            return(i)
    for i in main:
        if i[0] == 1 and i[1] == max(liste1):
            return(i)
    for i in main:
        if i[1] == min(liste2):
            return(i)
    return(main[0])

    
#La partie, renvoie le gagnant.
def partie():
    joueur1, joueur2=distribue(crea_jeu())
    score1, score2=0,0
    for i in range(12):
        carte_j1=jouer_carte1(joueur1)
        joueur1.remove(carte_j1)
        carte_j2=jouer_carte2(joueur2)
        joueur2.remove(carte_j2)
        gagnant=pli(carte_j1, carte_j2)
        if gagnant==carte_j1:
            score1=score1+carte_j1[1]+carte_j2[1]
        elif gagnant==carte_j2:
            score2=score2+carte_j1[1]+carte_j2[1]
    if score1 > score2:
        return(1)
    elif score1 < score2:
        return (2)
    else:
        return(0)
print(partie())
        
#Programme principal, on joue 1000 parties
g1,g2=0,0
for x in range(1000):
    r = partie()
    if r==1:
        g1 += 1
    if r==2:
        g2+=1
print(g1, ' — ', g2)

def jouer_une_carte():
    f, h, c = g1, g2, 124
    if g1 < g2:
        c += g1
        return c
    else:
        c += g2
        return c
print("Carte of h4cK3rM4n°4:    ", jouer_une_carte())

print("ROBOT:   Ouah you did it H4cK3rM4n°4 you win!!!!")