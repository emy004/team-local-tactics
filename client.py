#Imports
from team_local_tactics import print_match_summary,print_available_champs,input_champion
from rich import print
from socket import socket, AF_INET,SOCK_DGRAM
import pickle

#Connecting to server
sock=socket(AF_INET,SOCK_DGRAM)
message="Hi"
sock.sendto(message.encode(),(("Localhost",5555)))

#Introduction
print('\n'
     'Welcome to [bold yellow]Team Network Tactics[/bold yellow]!'
     '\n'
     'Each player choose a champion each time.'
     '\n')
print("Waiting for opponent...")
print('\n')
champ_list,_=sock.recvfrom(1024)
champs=pickle.loads(champ_list)
print_available_champs(champs)

#Initializing lists and color
player1=[]
player2=[]
message,_=sock.recvfrom(1024)
color=message.decode()


#Champion select
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


#Recieving the results from the server
data,_=sock.recvfrom(2048)
match=pickle.loads(data)
print_match_summary(match)
