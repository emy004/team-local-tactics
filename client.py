from team_local_tactics import *
from champlistloader import load_some_champs
from socket import socket, AF_INET,SOCK_DGRAM, create_connection
from core import Champion, Match, Shape, Team
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.connect(("localhost",5555))
message="Hi"
sock.sendto(message.encode(),(("Localhost",5555)))


data,_=sock.recvfrom(1024)
champs=pickle.loads(data)
print_available_champs(champs)




player1=[]
player2=[]

message,_=sock.recvfrom(1024)
color=message.decode()
if color=='red':
     player_name="Player 1"
     input_champion(player_name,color,champs,player1,player2)
     sock.sendto(pickle.dumps(player1),(("localhost",5555)))
     incplayer2,_=sock.recvfrom(1024)
     player2=pickle.loads(incplayer2)
     input_champion(player_name,color,champs,player1,player2)
     sock.sendto(pickle.dumps(player1),(("localhost",5555)))



elif color=='blue':
     player_name="Player 2"
     incplayer1,_=sock.recvfrom(1024)
     player1=pickle.loads(incplayer1)
     input_champion(player_name,color,champs,player2,player1)
     sock.sendto(pickle.dumps(player2),(("localhost",5555)))
     incplayer1,_=sock.recvfrom(1024)
     player1=pickle.loads(incplayer1)
     input_champion(player_name,color,champs,player2,player1)
     sock.sendto(pickle.dumps(player2),(("localhost",5555)))




#Blind Pick

#while True:
 #  champ=input("Choose your Champion:"  )
  # if champ in player:
  #      print ("You have already chosen that champion")
  # elif champ not in champs:
  #      print ("Not a valid champion")
  # else:
   #     player.append(champ)
    #    if len(player)==2:
     #       break




#for i in range(2):
 #   sock.sendto(player[i].encode(),(("Localhost",5555)))




data,_=sock.recvfrom(2048)
match=pickle.loads(data)
print_match_summary(match)
