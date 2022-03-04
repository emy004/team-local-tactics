from team_local_tactics import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from socket import socket,AF_INET, SOCK_DGRAM
from core import Champion, Match, Shape, Team
from threading import Thread
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",5555))



player1=[]
player2=[]
adresses=[]
adressbook=[]
champs=load_some_champs()

while  (len(player2)<2):

 data,adress=sock.recvfrom(1024)
 if len(adresses)==0:
    adresses.append(adress[1])
    adressbook.append(adress)
    player1.append(data.decode())

 elif adress==adresses:
    player1.append(data.decode())

 elif adress!=adresses:
    if adress not in adressbook:
     adressbook.append(adress)
    player2.append(data.decode())
    


            



print ("Player one chose:" + player1[0] + " and " + player1 [1])

print ("Player two chose:" + player2 [0] + " and " + player2[1])

match = Match(
    Team([champs[name] for name in player1]),
    Team([champs[name] for name in player2]))

match.play()
for i in range(2):
   sock.sendto(pickle.dumps(match),(adressbook[i]))


