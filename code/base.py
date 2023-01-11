import mysql.connector
from tkinter import messagebox

DATABASE = "face_student"
HOST = "localhost"
USER = "root"
PASSWORD =""

def database_connection():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            username=USER,
            password=PASSWORD,
            database=DATABASE
            )
        print("Connexion base de données réussi")
        return connection        
    except Exception as ex:
        messagebox.showerror("Erreur",f"Une erreur est survenue avec la base de donnes: {str(ex.args)}")
        print(f"Erreur depuis la base de données {str(ex)} ")
#Test
# database_connection()