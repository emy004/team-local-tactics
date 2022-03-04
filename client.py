from team_local_tactics import *
from champlistloader import load_some_champs
from socket import socket, AF_INET,SOCK_DGRAM, create_connection
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.connect(("localhost",5555))

champs=load_some_champs()
print_available_champs(champs)
player=[]
player1=[]
player2=[]
while True:
    champ=input("Choose your Champion:"  )
    if champ in player:
        print ("You have already chosen that champion")
    else:
        player.append(champ)
        if len(player)==2:
            break
#for _ in range(2):
 #       input_champion('Player 1', 'red', champs, player1, player2)
  #      input_champion('Player 2', 'blue', champs, player2, player1)



for i in range(2):
    sock.sendto(player[i].encode(),(("Localhost",5555)))




data,_=sock.recvfrom(1024)
match=pickle.loads(data)
print_match_summary(match)
