import serial
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#====Partie Parametres
#=====Parametres Arduino
BaudRate = 9600                 # vitesse de transefert Rs232, identique a celle mis dans le code arduino
Port = "COM1"                   # A Verifier sur arduino Ide et a changer si nécéssaire

#====Setup part

mail_content = "Alerte Intrusion"
#The mail addresses and password
sender_address = 'sender123@gmail.com'
sender_pass = 'xxxxxxxx'
receiver_address = 'receiver567@gmail.com'

ser = serial.Serial(Port, BaudRate)  # Ouverture du Port série

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address


#==== Loop Part
while(True):

    # Lecture du port série de l'arduino
    Data = ser.readLine()

    # Envoi du mail si le systeme a détécté une intrusion
    if(Data == "AI0"):
        message['Subject'] = "Intrusion on device 1 "
    elif(Data == "AI1"):
        message['Subject'] = "Intrusion on device 1 "

    
    if(Data == "AI0" or Data == "AI1"):
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    
    Data = ""

    time.sleep(1)   # attendre 1 seconde avant de relire le port série



