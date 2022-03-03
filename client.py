from team_local_tactics import *
from champlistloader import load_some_champs
from socket import socket, AF_INET,SOCK_DGRAM
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock2=socket(AF_INET,SOCK_DGRAM)
sock2.bind(('localhost',5556))
champs=load_some_champs()
print_available_champs(champs)
player1=[]
player2=[]
for _ in range(2):
        input_champion('Player 1', 'red', champs, player1, player2)
        input_champion('Player 2', 'blue', champs, player2, player1)
for i in range(2):
    sock.sendto(player1[i].encode(),("localhost",5555))
    sock.sendto(player2[i].encode(),("localhost",5555))



data,_=sock2.recvfrom(1024)
match=pickle.loads(data)
print_match_summary(match)
