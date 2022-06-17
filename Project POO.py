# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:08:53 2022

@author: Hp
"""

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os 
import sqlite3

root=Tk()
tree=tk.ttk.Treeview(root, columns=(1,2,3,4), height=5, show="headings")
tree.place(x=5,y=175,width=600,height=300)

def Ajouter_contact():
    PRENOM = entryPrenom.get()
    NOM = entryNom.get()
    NUM = entryNum.get()
    MAIL = entryMail.get()
    conn=sqlite3.connect('ContactsProject.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO Contact (`Nom`,`Prenom`, `Numero`,`Mail`) values (?,?,?,?)",
                (NOM, PRENOM,NUM, MAIL)), conn.commit()
    conn.close()
    
    # Affichage auto sur Treeview
    connection = sqlite3.connect("ContactsProject.db")
    curseur = connection.cursor()
    select = curseur.execute("SELECT*FROM Contact order by N° desc")
    select = list(select)
    tree.insert("", END, values = select[0])
    connection.close()
def RechNom(event):
    for x in tree.get_children():
        tree.delete(x)
    name=entryRechNom.get()
    conn=sqlite3.connect("ContactsProject.db")
    cur=conn.cursor()
    select=cur.execute("SELECT*FROM Contact where NOM=(?)",(name,))
    conn.commit()
    for row in select:
        tree.insert('',END,values=row)
    conn.close()
def RechPren(event):
    for x in tree.get_children():
        tree.delete(x)
    surn=entryRechPren.get()
    conn=sqlite3.connect("ContactsProject.db")
    cur=conn.cursor()
    select=cur.execute("SELECT*FROM Contact where PRENOM=(?)",(surn,))
    conn.commit()
    for row in select:
        tree.insert('',END,values=row)
    conn.close()
    
    
    
root=Tk()
root.title("Carnet Adresse")
root.geometry("600x500")
root.config(bg="#eaeaea")

lblTitre = tk.Label(root, text= "Carnet d'adresse", font=("Arial",21), bg="darkblue", fg="white")
lblTitre.place(x=0,y=0,width=320,height=41)

lbRechercheNom=tk.Label(root, text="Recherche par nom:", bg ="darkblue", fg="white")
lbRechercheNom.place(x=270, y=0 , width=160)
entryRechNom=Entry(root)
entryRechNom.bind("<Return>",RechNom )
entryRechNom.place(x=450, y=0 ,width=160)

lblRecherchePrenom=tk.Label(root, text="Recherche par Prenom:", bg="darkblue",fg= "white")
lblRecherchePrenom.place(x=270,y=20,width =160)
entryRechPren=Entry(root)
entryRechPren.bind("<Return>",RechPren)
entryRechPren.place(x=450,y=20,width=160)

lblNom=tk.Label(root, text="Nom ", bg="grey", fg="black")
lblNom.place(x=5,y=50,width=125)
entryNom=Entry(root)
entryNom.place(x=130 ,y=50, width=175)

lblPrenom=tk.Label(root, text=" Prenom", bg="grey", fg="black")
lblPrenom.place(x=5,y=75,width=125)
entryPrenom=Entry(root)
entryPrenom.place(x=130 ,y=75, width=175)

lblNum=tk.Label(root, text=" Numero", bg="grey", fg="black")
lblNum.place(x=5,y=100,width=125)
entryNum=Entry(root)
entryNum.place(x=130 ,y=100, width=175)

lblMail=tk.Label(root, text=" Mail", bg="grey", fg="black")
lblMail.place(x=5,y=125,width=125)
entryMail=Entry(root)
entryMail.place(x=130 ,y=125, width=175)

bAdd= tk.Button(root, text="Ajouter Contact" ,bg="darkblue",fg="white",command=Ajouter_contact)
bAdd.place(x=175, y=145,width=125)

bRechn=tk.Button(root, text="Rechercher par nom" ,bg="darkblue", fg="black",command=RechNom(entryRechNom))
bRechn.place(x=475,y=40,width=125)
bRechp=tk.Button(root,text="Recherche par prenom", bg="darkblue",fg="black",command=RechPren(entryRechPren))
bRechp.place(x=475,y=60,width=125)


tree=tk.ttk.Treeview(root, columns=(1,2,3,4), height=5, show="headings")
tree.place(x=5,y=175,width=600,height=300)

tree.heading(1, text="NOM")
tree.heading(2, text="PRENOM")
tree.heading(3, text="NUMERO")
tree.heading(4, text="MAIL")

tree.column(1,width=75)
tree.column(2,width=100)
tree.column(3,width=100)

# Affichage des infos sur L'ecran
connection = sqlite3.connect("Contactsproject.db")
curseur = connection.cursor()
select = curseur.execute("select*from Contact")
for ligne in select:
    tree.insert("", END, value = ligne)
connection.close()


root.mainloop()



