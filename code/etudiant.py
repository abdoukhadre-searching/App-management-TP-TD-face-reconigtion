from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import cv2
import base as connection
import os
import numpy as np
from datetime import datetime
import datetime as dt
import time


class pagePrincipal:
    def __init__(self,root):
        self.root = root
        self.root.title("ETUDIANT")
        self.root.geometry("1295x728+120+25")

        self.tabControl = ttk.Notebook(root)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tab6 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Authentification')
        self.tabControl.add(self.tab2, text ='Gestion enseignant')
        self.tabControl.add(self.tab3, text ="Gestion etudiant + traitements d'image")
        self.tabControl.add(self.tab4, text ="Gestion des comptes d'utilisateur")
        self.tabControl.add(self.tab5, text ="Gestion liste de présences")
        self.tabControl.add(self.tab6, text ="Gestion des séances et marquage")

        self.tabControl.pack(expand = 1, fill ="both")

        # ==================tab3 gestion etudiants
        titre_page = Label(self.tab3, text="Page de gestion des informations des Etudiants",font=("time new roman",16, "bold"),fg="black")
        titre_page.place(x=40, y=20)

        #--Formulaire de seances de td  ou tp 
        self.var_id_enseignant = IntVar()
        self.var_matiere = StringVar()
        self.var_classe = StringVar()
        self.var_salle  = StringVar()
        self.var_heure_debut = StringVar()
        self.var_heure_fin = StringVar()
        self.var_type_seance = StringVar()




        self.afficher_infos_table()



        
        lbl_debut = Label(self.tab6, font=("time new roman",12,"bold"),text="Heure de début",fg='black')
        lbl_debut.place(x=330,y=90)        
        h_debut_cbo = Combobox(self.tab6, textvariable=self.var_heure_debut,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_debut_cbo["values"]=("Debut","08:00:00","08:15:00","08:30:00","08:45:00","09:00:00","09:15:00","09:30:00","09:45:00","10:00:00","10:15:00","10:30:00","10:45:00")
        h_debut_cbo.current(0)
        h_debut_cbo.place(x=480,y=90,width=80)

        lbl_fin = Label(self.tab6, font=("time new roman",12,"bold"), text="Fin de séance",fg='black')
        lbl_fin.place(x=330,y=120)        
        h_fin_cbo = Combobox(self.tab6, textvariable=self.var_heure_fin,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_fin_cbo["values"]=("Fin","10:00:00","10:15:00","10:30:00","10:45:00","11:00:00","11:15:00","11:30:00","11:45:00","12:00:00","12:15:00","12:30:00","12:45:00","13:00:00")
        h_fin_cbo.current(0)
        h_fin_cbo.place(x=480,y=120,width=80)

        lbl_type_seance = Label(self.tab6,font=("time new roman",12,"bold"),text="Type de seance",fg='black')
        lbl_type_seance.place(x=20,y=90)
        type_seance_cbo = Combobox(self.tab6, textvariable=self.var_type_seance,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        type_seance_cbo.place(x=150,y=90,width=150)
        type_seance_cbo['values'] = ("Choisir","TD", "TP")
        type_seance_cbo.current(0)
        #contenu seance
        lbl_contenu_seance = Label(self.tab6,font=("time new roman",12,"bold"),text=" Rapport Contenu seance",fg='black')
        lbl_contenu_seance.place(x=20,y=120)
        contenu = Text(self.tab6,fg="black",font=("time new roman",12,"bold"),height=10,width=50,bg='white',relief=FLAT)
        contenu.place(x=25,y=160)

        lbl_matiere = Label(self.tab6, font=("time new roman",12,"bold"),text="Matière",fg='black')
        lbl_matiere.place(x=590,y=90)
        self.matiere_cbo = Combobox(self.tab6, textvariable=self.var_matiere,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        self.matiere_cbo["values"] = ('Java', 'Python', 'Algorithme', 'XML', 'Reseaux')
        self.matiere_cbo.current(0)
        # self.matiere_cbo.bind('<<ComboboxSelected>>',self.recup_matiere)
        self.matiere_cbo.place(x=680,y=90,width=300)

        lbl_classe = Label(self.tab6,font=("time new roman",12,"bold"),text="Classe",fg='black')
        lbl_classe.place(x=590,y=120)
        classe_cbo = Combobox(self.tab6, textvariable=self.var_classe,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        classe_cbo.place(x=680,y=120,width=300)
        classe_cbo['values'] = ("Sélectionner la classe","L1 SRT", "Licence 2", "Licence 3", "Master 1", "Master 2")
        classe_cbo.current(0)

        #--bouton engistrer 
        btn_save_seance = Button(self.tab6,bg="#174577",text="Enregister", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_save_seance.place(x=500,y=160,width=180,height=33)
        btn_modifier_seance = Button(self.tab6,bg="#174577",text="Modifier", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_modifier_seance.place(x=500,y=200,width=180,height=33)
        btn_marquage_seance = Button(self.tab6,bg="green",text="Lancer la reconnaissance", foreground="white", command=self.lancer_reconnaissance_seance,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_marquage_seance.place(x=500,y=240,width=180,height=33)



        

        #===================================================================

        # tabControl_tab1.add(self.tab1_secondaire1, text="Connexion enseignant")
        # tabControl_tab1.add(self.tab1_secondaire2, text="Connexion admin")
        # tabControl_tab1.place(x=0, y=0, height=800, width=1300)

        #--------parametre image bg ---------------------

        # bg = Image.open(r"images/background_login.png")

        # self.photo_bg = ImageTk.PhotoImage(bg)
        # lable_login = Label(self.tab1, image=self.photo_bg ,bg ='#290951')
        # lable_login.place(x=0,y=0,width=1024,height=770)

        #------- champs formulaire ---------------------
        self.var_login = StringVar()
        self.var_password = StringVar()
        self.var_id_etudiant = IntVar() #integer in db
        self.var_nom_etudiant = StringVar()
        self.var_niveau_etudiant = StringVar()
        self.var_prenom_etudiant = StringVar()
        self.var_sexe_etudiant = StringVar()
        self.var_date_naissance_etudiant = StringVar()
        self.var_lieu_naissance_etudiant = StringVar()
        self.var_tel_etudiant = StringVar()

        champ_username = Entry(self.tab1, textvariable=self.var_login ,relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_username.place(x=370, y=431)   
        champ_password = Entry(self.tab1, textvariable=self.var_password, relief="flat", font=("Arial", 12)) #flat, groove, raised, ridge, solid, or sunken
        champ_password.place(x=370, y=508)      

        
        #-------------tab 3
        identifiant_etudiant_lbl = Label(self.tab3, text="Numero d'identification",font=("time new roman",12, "bold"),fg="black")
        identifiant_etudiant_lbl.place(x=20, y=100)
        lbl = Label(self.tab3,textvariable=self.var_id_etudiant,  fg="black",font=("time new roman",12, "bold"))
        lbl.place(x=230,y=100)

        nom_etudiant_lbl = Label(self.tab3, text="Nom etudiant",font=("time new roman",12, "bold"),fg="black")
        nom_etudiant_lbl.place(x=20, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=135,height=33,width=220)
        nom_etudiant = Entry(self.tab3, fg="#174577",textvariable=self.var_nom_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        nom_etudiant.place(x=170,y=140)

        prenom_etudiant_lbl = Label(self.tab3, text="Prenom etudiant",font=("time new roman",12, "bold"),fg="black")
        prenom_etudiant_lbl.place(x=20, y=180)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=175,height=33,width=220)
        prenom_etudiant = Entry(self.tab3, fg ="#174577",textvariable=self.var_prenom_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        prenom_etudiant.place(x=170,y=180)

        niveau_etudiant_lbl = Label(self.tab3, text="Niveau",font=("time new roman",12, "bold"),fg="black")
        niveau_etudiant_lbl.place(x=400, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=480,y=135,height=33,width=220)
        niveau_combo= ttk.Combobox(self.tab3,foreground='#174577',textvariable=self.var_niveau_etudiant ,font=("time new roman",12, "bold"), state="readonly")
        niveau_combo.place(x=490,y=140)
        niveau_combo["values"] = ("Sélectionner le niveau","Licence 1", "Licence 2", "Licence 3", "Master 1", "Master 2")
        niveau_combo.current(0)

        sexe_etudiant_lbl = Label(self.tab3, text="Genre",font=("time new roman",12, "bold"),fg="black")
        sexe_etudiant_lbl.place(x=400, y=180)
        # lbl = Label(self.tab3,image=self.img, bg='#174577')
        # lbl.place(x=480,y=175,height=33,width=220)
        sexe_combo= ttk.Combobox(self.tab3,foreground='#174577',textvariable=self.var_sexe_etudiant ,font=("time new roman",12, "bold"), state="readonly")
        sexe_combo["values"]=("Selectionner le sexe","Homme","Femme")
        sexe_combo.current(0)
        sexe_combo.place(x=490,y=180)

        dateNaissance_etudiant_lbl = Label(self.tab3, text="Date Naissance",font=("time new roman",12, "bold"),fg="black")
        dateNaissance_etudiant_lbl.place(x=20, y=220)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=160,y=215,height=33,width=220)
        date_naissance=DateEntry(self.tab3,selectmode='day',textvariable=self.var_date_naissance_etudiant)
        date_naissance.place(x=170,y=222,width=200)

        lieuNaissance_etudiant_lbl = Label(self.tab3, text="Lieu de naissance",font=("time new roman",12, "bold"),fg="black")
        lieuNaissance_etudiant_lbl.place(x=400, y=220)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=550,y=215,height=33,width=220)
        lieuNaissance_etudiant = Entry(self.tab3, fg ="#174577",textvariable=self.var_lieu_naissance_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        lieuNaissance_etudiant.place(x=560,y=220)

        contactEtudiant_lbl = Label(self.tab3, text="Numero telephone",font=("time new roman",12, "bold"),fg="black")
        contactEtudiant_lbl.place(x=725, y=140)
        # lbl = Label(self.tab3,image=img, bg='#174577')
        # lbl.place(x=840,y=135,height=33,width=220)
        contactEtudiant_entry = Entry(self.tab3, fg ="#174577",textvariable=self.var_tel_etudiant,relief=FLAT,font=("time new roman",12, "bold"))
        contactEtudiant_entry.place(x=875,y=140)

        #-----boutons
        btn_sv_p = Button(self.tab3,bg="#174577",text="Enregister", foreground="white", command=self.insert_etudiant,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_sv_p.place(x=50,y=290,width=140,height=33)
        btn_update_p = Button(self.tab3,bg="#174577",text="Modifier", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_update_p.place(x=200,y=290,width=140,height=33)
        btn_delete_p = Button(self.tab3,bg="#174577", text="Supprimer", foreground="white", command= "",bd=0,cursor="hand2",activebackground="red")
        btn_delete_p.place(x=350,y=290,width=140,height=33)
        btn_effacer_p = Button(self.tab3,bg="#174577",text="Annuler", foreground="white", command=self.reset_formulaire,bd=0,cursor="hand2",activebackground="grey")
        btn_effacer_p.place(x=500,y=290,width=140,height=33)
        btn_photo_visage_etudiant = Button(self.tab3,bg="#174577",text="Prendre photo", foreground="white", command=self.lancer_camera,bd=0,cursor="hand2",activebackground="#174577")
        btn_photo_visage_etudiant.place(x=650,y=290,width=140,height=33)
        btn_code_etudiant = Button(self.tab3,bg="green",text="Actualiser le systeme de reconnaissance", foreground="white", command=self.actualiser_fichier_reconnaissance,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_code_etudiant.place(x=820,y=290,width=250,height=33)
        btn_supprime_image_etudiant = Button(self.tab3,bg="#174577",text="Supprimer photos", foreground="white", command="",bd=0,cursor="hand2",activebackground="black")
        btn_supprime_image_etudiant.place(x=1100,y=290,width=110,height=33)

        #--Formulaire de seances de td  ou tp 
        self.var_id_enseignant = IntVar()
        self.var_matiere = StringVar()
        self.var_classe = StringVar()
        self.var_salle  = StringVar()
        self.var_heure_debut = StringVar()
        self.var_heure_fin = StringVar()
        self.var_type_seance = StringVar()

        

        lbl_debut = Label(self.tab6, font=("time new roman",12,"bold"),text="Heure de début",fg='black')
        lbl_debut.place(x=330,y=90)        
        h_debut_cbo = Combobox(self.tab6, textvariable=self.var_heure_debut,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_debut_cbo["values"]=("Debut","08:00:00","08:15:00","08:30:00","08:45:00","09:00:00","09:15:00","09:30:00","09:45:00","10:00:00","10:15:00","10:30:00","10:45:00")
        h_debut_cbo.current(0)
        h_debut_cbo.place(x=480,y=90,width=80)

        lbl_fin = Label(self.tab6, font=("time new roman",12,"bold"), text="Fin de séance",fg='black')
        lbl_fin.place(x=330,y=120)        
        h_fin_cbo = Combobox(self.tab6, textvariable=self.var_heure_fin,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        h_fin_cbo["values"]=("Fin","10:00:00","10:15:00","10:30:00","10:45:00","11:00:00","11:15:00","11:30:00","11:45:00","12:00:00","12:15:00","12:30:00","12:45:00","13:00:00")
        h_fin_cbo.current(0)
        h_fin_cbo.place(x=480,y=120,width=80)

        lbl_type_seance = Label(self.tab6,font=("time new roman",12,"bold"),text="Type de seance",fg='black')
        lbl_type_seance.place(x=20,y=90)
        type_seance_cbo = Combobox(self.tab6, textvariable=self.var_type_seance,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        type_seance_cbo.place(x=150,y=90,width=150)
        type_seance_cbo['values'] = ("Choisir","TD", "TP")
        type_seance_cbo.current(0)
        #contenu seance
        lbl_contenu_seance = Label(self.tab6,font=("time new roman",12,"bold"),text=" Rapport Contenu seance",fg='black')
        lbl_contenu_seance.place(x=20,y=120)
        contenu = Text(self.tab6,fg="black",font=("time new roman",12,"bold"),height=10,width=50,bg='white',relief=FLAT)
        contenu.place(x=25,y=160)

        lbl_matiere = Label(self.tab6, font=("time new roman",12,"bold"),text="Matière",fg='black')
        lbl_matiere.place(x=590,y=90)
        self.matiere_cbo = Combobox(self.tab6, textvariable=self.var_matiere,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        self.matiere_cbo["values"] = ('Java', 'Python', 'Algorithme', 'XML', 'Reseaux')
        self.matiere_cbo.current(0)
        # self.matiere_cbo.bind('<<ComboboxSelected>>',self.recup_matiere)
        self.matiere_cbo.place(x=680,y=90,width=300)

        lbl_classe = Label(self.tab6,font=("time new roman",12,"bold"),text="Classe",fg='black')
        lbl_classe.place(x=590,y=120)
        classe_cbo = Combobox(self.tab6, textvariable=self.var_classe,foreground="black" ,font=("time new roman",12, "bold"), state="readonly")
        classe_cbo.place(x=680,y=120,width=300)
        classe_cbo['values'] = ("Sélectionner la classe","L1 SRT", "Licence 2", "Licence 3", "Master 1", "Master 2")
        classe_cbo.current(0)

        #--bouton engistrer 
        btn_save_seance = Button(self.tab6,bg="#174577",text="Enregister", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_save_seance.place(x=500,y=160,width=180,height=33)
        btn_modifier_seance = Button(self.tab6,bg="#174577",text="Modifier", foreground="white", command="",bd=0,cursor="hand2",activebackground="#174577")
        btn_modifier_seance.place(x=500,y=200,width=180,height=33)
        btn_marquage_seance = Button(self.tab6,bg="green",text="Lancer la reconnaissance", foreground="white", command=self.lancer_reconnaissance_seance,bd=0,cursor="hand2",activebackground="lightgreen")
        btn_marquage_seance.place(x=500,y=240,width=180,height=33)




        #-------- Tableau Liste Etudiant ---------------
        table_frame=Frame(self.tab3, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=355, width=1230, height=370) #w=1226

        scroll_x= ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient= VERTICAL)


        self.student_table= ttk.Treeview(table_frame, columns=("id","prenom","nom","niveau","sexe","dateNaissance","lieuNaissance","telephoneEtudiant","absence_semestre"),xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set)
        s = ttk.Style()
        s.configure('Treeview', rowheight= 40)
        s.configure("Treeview.Heading", font=("time new roman", 10, "bold"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Numero Etudiant")
        self.student_table.heading("prenom",text="Prenom")
        self.student_table.heading("nom",text="Nom")
        self.student_table.heading("niveau",text="Niveau")
        self.student_table.heading("sexe",text="Sexe")
        self.student_table.heading("dateNaissance",text="Date de Naissance")
        self.student_table.heading("lieuNaissance",text="Lieu de Naissance")
        self.student_table.heading("telephoneEtudiant",text="Telephone")
        self.student_table.heading("absence_semestre",text="Absence semestrielle")        
        #self.student_table.heading("photo",text="Photo Profil")

        #`id_eleve`, `nom`, `adresse`, `dateNaissance`, `niveau`, `niveau`, `sexe`, `domaine`, `annee`, `contactParent`, `enseignant`, `semestre`, `photo`

        self.student_table.column("id",width=100,stretch=0)
        self.student_table.column("prenom",width=100,stretch=0)
        self.student_table.column("nom",width=100,stretch=0)
        self.student_table.column("niveau",width=100,stretch=0)
        self.student_table.column("sexe",width=100,stretch=0)
        self.student_table.column("dateNaissance",width=135,stretch=0)
        self.student_table.column("lieuNaissance",width=135,stretch=0)
        self.student_table.column("telephoneEtudiant",width=120,stretch=0)
        self.student_table.column("absence_semestre",width=140,stretch=0)
        #self.student_table.column("photo",width=100)


        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.joindre_tab_form)
        self.afficher_infos_table()

    def joindre_tab_form(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        donnees = content["values"]
        print("Donnee tableau etudiant:\n",donnees)
        self.var_id_etudiant.set(donnees[0]),
        self.var_prenom_etudiant.set(donnees[1]),
        self.var_nom_etudiant.set(donnees[2]),
        self.var_niveau_etudiant.set(donnees[3]),        
        self.var_sexe_etudiant.set(donnees[4]),
        self.var_date_naissance_etudiant.set(donnees[5]),
        self.var_lieu_naissance_etudiant.set(donnees[6]),
        self.var_tel_etudiant.set(donnees[7]), 

    
    def lancer_reconnaissance_seance(self):
        face_classifier=cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
        model_clf = cv2.face.LBPHFaceRecognizer_create()
        model_clf.read("model/model_VisagesAll.xml")
        cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        # Pour assurer une seule insertion dans le marquage
        variable = True

        # img_id=0
        while True:
            ret,img=cap.read() # Recupere video depuis Webcam
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            visages=face_classifier.detectMultiScale(img, 1.7, 5)#(img, 1.05, 6)
            visages=face_classifier.detectMultiScale(gray, 1.7, 5)
            #-------- Redimensionner l'Image ---------------
            minisize = (img.shape[1],img.shape[0])
            miniframe = cv2.resize(img, minisize)

            visages =  face_classifier.detectMultiScale(miniframe)
            couleur = (100,255,255)
            couleur_verte = (0,255,0)
            cv2.putText(img,"Reconnaissance faciale + Marquage ",(10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2) 
            cv2.putText(img,f"Date-Heure: {str(datetime.now())}",(10,60), cv2.FONT_HERSHEY_COMPLEX,0.6,(100,55,255),2)                        

            for (x,y,w,h) in visages:
                # on recupere l'id et le taux de precision [0:1]
                id,predict=model_clf.predict(gray[y:y+h,x:x+w])

                taux_de_precision = int((100 * (1-predict/300)))
                print(f"ID Etudiant: {id} ___ Taux de precision {taux_de_precision} %")

                try:
                    conn = connection.database_connection()
                    my_curseur = conn.cursor()
                    my_curseur.execute("SELECT id_etudiant,prenom,nom FROM `etudiant` WHERE id_etudiant="+str(id))
                    result=my_curseur.fetchone()
                    if result is not None:
                        id_etudiant = result[0]
                        prenom_etudiant = result[1]
                        nom_etudiant = result[2]
                        print("Informations étudiants:\n", prenom_etudiant, nom_etudiant)
                    else:
                        pass
                except Exception as ex:
                    print(f"Erreur: {str(ex)}")
                    messagebox.showinfo("Erreur",f"Attention une erreur est survenue lors d'une requette: \n{str(ex)}")

                if taux_de_precision > 75:  
                    cv2.rectangle(img, (x,y), (x+w,y+h), (couleur_verte),2) 
                    # cv2.rectangle(img,(x-2,y+h+65),(x+w,y+h+5),(0,150,0),-4)
                    cv2.putText(img,f"NOM : {prenom_etudiant} {nom_etudiant}",(x+5,y+h+20), cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2) 
                    cv2.putText(img,f"CODE ETUDIANT: {id}",(x+5,y+h+45), cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)   
                    
                    # -------------Insertion de cet etudiant dans la table presence pour le marquage...
                    
                    date_a_linstant = dt.date.today()
                    date_a_linstant = date_a_linstant.strftime("%y/%m/%d")
                    heure_actuelle = time.strftime("%H:%M:%S")

                    seance = "TD" # wala TP
                    matiere ="Telecoms"
                    status = "Présent"
                    enseignant = "Monsieur Abdoukhadre Diop"
                    idEtudiant =  id    
                    nomPrenomEtudiant = f"{prenom_etudiant} {nom_etudiant}"
                    heureDebut = "18:00"
                    heureFin = "19:00"

                    requette = "INSERT INTO `presence` (`id`, `date`, `seance`, `matiere`, `status`, `enseignant`, `idEtudiant`, `nomPrenomEtudiant`, `heureDebut`, `heureFin`) VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    
                    conn = connection.database_connection()
                    my_curseur = conn.cursor()
                    
                    if variable:
                        my_curseur.execute(requette, (date_a_linstant, seance, matiere, status, enseignant, idEtudiant, nomPrenomEtudiant, heureDebut, heureFin))
                        conn.commit()
                        conn.close()
                        variable = False                    
                        print("..marquage effectué avec succes !..")


                else:              
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255),2)                        
                    cv2.putText(img,"Reconnaissance en cours...",(x-5,y+h+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (couleur), 2)

            cv2.imshow("Enregistrement du visage", img)


            if cv2.waitKey(1)==27: #if cv2.waitKey(1) or int(img_id) == 100:
                # dire("Collecte d'image effectuées")
                break
        
        cap.release()
        cv2.destroyAllWindows()


    def afficher_infos_table(self):
        try:
            conn = connection.database_connection()
            my_curseur = conn.cursor()
            my_curseur.execute("SELECT * FROM `etudiant`")   
            etudiants = my_curseur.fetchall()

            if len(etudiants) != 0:
                self.student_table.delete(*self.student_table.get_children())  
                for etu in etudiants:
                    self.student_table.insert("", END,values=etu)
                    conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}")
            print(f"Erreur lors l'affichage :{str(ex)}")

    def reset_formulaire(self):
        self.var_id_etudiant.set(0)
        self.var_nom_etudiant.set("")
        self.var_prenom_etudiant.set("")
        self.var_date_naissance_etudiant.set("")
        self.var_niveau_etudiant.set("Selectionner le niveau")
        self.var_lieu_naissance_etudiant.set("")
        self.var_tel_etudiant.set("")
        self.var_sexe_etudiant.set("Selectionner le sexe")

    
    def insert_etudiant(self):
        if self.var_tel_etudiant.get() =="" or self.var_nom_etudiant.get()=="" or self.var_prenom_etudiant.get()=="" or self.var_niveau_etudiant.get()=="Selectionner la classe"  or self.var_sexe_etudiant.get() =="Selectionner le sexe" or self.var_date_naissance_etudiant.get()=="" or self.var_lieu_naissance_etudiant.get() =="":
            messagebox.showerror("Erreur","Attention tous les champs sont requises !",parent=root)
        else:
            try:
                conn = connection.database_connection()
                my_curseur = conn.cursor()
                my_curseur.execute(f"SELECT * FROM `etudiant` WHERE id_etudiant={self.var_id_etudiant.get()}")
                resultat = my_curseur.fetchone()
                if resultat is not None:
                    print(resultat)                    
                    messagebox.showerror("Attention","cet identifiant existe déjà)",parent=self.tab3)
                    print("Cet identifiant existe déjà")                                        
                else:
                    my_curseur.execute("INSERT INTO `etudiant` (`prenom`, `nom`, `niveau`, `sexe`, `dateNaissance`, `lieuNaissance`, `telephone`, `absence_semestre`) VALUES (%s,%s,%s,%s,%s,%s,%s,0)",
                        ( 
                            self.var_prenom_etudiant.get(),
                            self.var_nom_etudiant.get(),
                            self.var_niveau_etudiant.get(),
                            self.var_sexe_etudiant.get(),
                            self.var_date_naissance_etudiant.get(),
                            self.var_lieu_naissance_etudiant.get(),
                            self.var_tel_etudiant.get(),
                        )
                    )
                    conn.commit()
                    self.afficher_infos_table()
                    # self.fetch_data()
                    self.reset_formulaire()
                    conn.close()
                    messagebox.showinfo("Succés","Enregistrement effectué)",parent=self.tab3)
                    print("Etudiant ajouté dans le systeme")

            except Exception as ex:
                messagebox.showinfo("Erreur",f"Une erreur est survenue: {str(ex.args)}",parent=self.tab3)
                print(f"Erreur {str(ex)} ")


    def lancer_camera(self):
        id = self.var_id_etudiant.get()
        if id == 0:
            messagebox.showerror('Erreur', "Veuiller selectionner un Etudiant", parent=self.tab3)
        else:
            face_classifier=cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

            cap =cv2.VideoCapture(0, cv2.CAP_DSHOW)

            img_id=0
            while True:
                ret,img=cap.read()#recupere video depuis webcam
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                visages=face_classifier.detectMultiScale(img, 1.3, 5)#(img, 1.05, 6)
                visages=face_classifier.detectMultiScale(gray, 1.3, 5)
                #-------- Redimensionner l'Image ---------------
                minisize = (img.shape[1],img.shape[0])
                miniframe = cv2.resize(img, minisize)
                visages =  face_classifier.detectMultiScale(miniframe)
                for (x,y,w,h) in visages:
                    img_id+=1
                    #visage_recadre=img[y:y+h, x:x+w]
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)                        
                    cv2.putText(img,"Enregistrement de photo du visage...",(x-5,y+h+15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                    #Save just the rectangle faces in SubRecFaces
                    img_save = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    sub_face = img_save[y:y+h, x:x+w]                        
                    #face = cv2.resize(img[y:y+h, x:x+w](img),(450,450))
                    #face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
                    #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) 
                                          
                    file_name_path = "datafaces/etudiant."+str(id)+"."+str(img_id)+".jpg" 
                    file_name_path = "photos_etudiants/etudiant."+str(id)+"."+str(img_id)+".jpg"                        
                    cv2.imwrite(file_name_path,sub_face)
                    cv2.putText(img,"Captures:",(10,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,255), 2) #face en debut de fonction                        
                    cv2.putText(img,str(img_id),(10,90), cv2.FONT_HERSHEY_COMPLEX, 1.2, (255,0,255), 2)
                cv2.imshow("Enregistrement du visage", img)

                if cv2.waitKey(1)==27 or int(img_id) == 30: #if cv2.waitKey(1) or int(img_id) == 100:
                    # dire("Collecte d'image effectuées")
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo(f"Résultat","Image faciales de l'etudiant enregistrées", parent=self.tab3)

    def actualiser_fichier_reconnaissance(self):
        data_dir=("datafaces")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids  =[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Chargement des images enregistres",imageNp)
            cv2.waitKey(1)==13            
        ids=np.array(ids)

        #========== Train the classifier and save the results ===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("model/model_VisagesAll.xml")
        # dire("Actualiser du modeles de reconnaissance faciales")

        cv2.destroyAllWindows()
        messagebox.showinfo("Resultat","Modele actualisé avec succés !", parent=self.tab3)

if __name__ == "__main__":
    root=Tk()
    obj=pagePrincipal(root)
    root.mainloop()
