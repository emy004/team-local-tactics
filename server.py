from team_local_tactics import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from socket import socket, AF_INET,SOCK_DGRAM
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",5555))

player1=[]
player2=[]
for i in range(2):
    player1.append(sock.recvfrom(1024)[0].decode())
    player2.append(sock.recvfrom(1024)[0].decode())
#player1, _ =sock.recvfrom(1024)
#player1champs=player1.decode()
#player2, _ =sock.recvfrom(1024)
#player2champs=player2.decode()
print ("Player one chose:" + player1[0] + " and " + player1 [1])
print ("Player two chose:" + player2 [0] + " and " + player2[1])


