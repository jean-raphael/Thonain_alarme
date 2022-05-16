import serial
import time
import win32com.client

#====Partie Parametres
#=====Parametres Arduino
BaudRate = 9600                 # vitesse de transefert Rs232, identique a celle mis dans le code arduino
Port = "COM1"                   # A Verifier sur arduino Ide et a changer si nécéssaire

#=====Outlook settings
Destinataire = "test@test.com"  # destinataire de l'email

#====Setup part

ser = serial.Serial(Port, BaudRate)  # Ouverture du Port série

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = Destinataire
mail.subject = "Alerte Intrusion"
mail.Body = " Intrusion détéctée"
#mail.Attachment.Add("c:\\fichier.txt")
#mail.CC = "test@test.com"


#==== Loop Part
while(True):

    # Lecture du port série de l'arduino
    Data = ser.readLine()

    # Envoi du mail si le systeme a détécté une intrusion
    if(Data == "AI0"):
        mail.Body = " Intrusion détéctée du capteur 0"
        mail.send()
    elif(Data == "AI1"):
        mail.Body = " Intrusion détéctée du capteur 1"
        mail.send()
    
    Data = ""

    time.sleep(1)   # attendre 1 seconde 



