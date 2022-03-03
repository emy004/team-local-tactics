from team_local_tactics import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from socket import socket, AF_INET,SOCK_DGRAM
from core import Champion, Match, Shape, Team
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",5555))

sock2=socket(AF_INET,SOCK_DGRAM)

player1=[]
player2=[]
champs=load_some_champs()
for i in range(2):
    player1.append(sock.recvfrom(1024)[0].decode())
    player2.append(sock.recvfrom(1024)[0].decode())

print ("Player one chose:" + player1[0] + " and " + player1 [1])
print ("Player two chose:" + player2 [0] + " and " + player2[1])

match = Match(
    Team([champs[name] for name in player1]),
    Team([champs[name] for name in player2]))

match.play()

sock2.sendto(pickle.dumps(match),(("localhost",5556)))

