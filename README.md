# Thonain_alarme

voici une petite démo de ce qu'il serait possible de faire avec un script python.

C'est fait rapidememnt et j'ai pas testé la partie arduino

## Partie arduino 

Rien de spécial ici ,
Un petit progrmmme de démo.

deux bouttons son connecté entre la masse et les pins 0 et 1 de l'arduino

l'arduno envoi "AI0" et "AI1" sur sont port série.
on peut vérifier que ca fonctionne en ouvrant arduino ide et en ouvrant le terminal série.


## Script python
### Installation de python

Si tu n'as pas déja installé python, le plus simple est de passer par windows store et d'installer la derniere vesion de python 3.10
Dans le temps il était possible d'installer depuis le windows store sans compte microsoft , il suffiseait de refuser les tres nombreuses demandes de connections.

Sinon Il faut télécharger le setup de python sur internet, 
Désacer tout les alias python qui renvoient vers le windows store ( checher alias dans cortana )
Puis installer python sans oublier de cocher la case "ajouter au path" ou "ajouter python dans les variables d'environnement.

Si python s'est correctement installer, si on écrit "python" dans un cmd , un terminal python devrait s'ouvrir (>>>)

### Installation des Libraries

Le Script utilise deux librairies, une pour géréer la communication série, un autre pour les mail.

Dans un cmd (pas dans python) il faut ecrire :
pip install pyserial smtplib

python affichera peut etre une erreur comme quoi il faut petre a jour pip, c'est pas important.
selon les version il semble qu'il n'y ai pas forcément besoins d'installer smtplib

### configuration du script

Avant de lancer le systeme il est nécéssaire de configurer les script pyhton.

1 - connecter l'arduino via usb a l'ordinateur
2 - Dans arduino Ide dans outil/port mémoriser le port pris par l'arduino.
(ce port peut changer c'est donc la premiere chose a verifier si ca fonctionne plus)
3 - dans le script metre le port COMx dans les réglages 
4 - finalement régler les parametres sur les variables de mail (source, destination, mot de passe, ...)

### Execution du script

Normalement un double click sur le fichier python suffit a le démarer
Sinon dans l'explorateur de fichier, a l'emplacement ou se situe le script
taper cmd dans la barre du chemin.
une fois le terminal ouvert il ne reste plus qu'a écrire 
python script.py
et executer 