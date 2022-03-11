#Imports
from socket import socket,AF_INET, SOCK_DGRAM
from core import  Match, Team
import pickle

#Socket
sock=socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",5555))


#Initializing lists
player1=[]
player2=[]
adresses=[]

#Handling available champions
champ_list,adress_to_db=sock.recvfrom(1024)
champs=pickle.loads(champ_list)

#Connecting with clients
while len(adresses)<2:
   _,adress_to_client=sock.recvfrom(1024)

   if adress_to_client not in adresses:
     adresses.append(adress_to_client)

#Sending available champtions to clients
for i in range(len(adresses)):
   sock.sendto(pickle.dumps(champs),(adresses[i]))

#Champion selection
toplayer1="red"
toplayer2="blue"
sock.sendto(toplayer1.encode(),(adresses[0]))
p1,_=sock.recvfrom(1024)
player1=pickle.loads(p1)
sock.sendto(toplayer2.encode(),(adresses[1]))
sock.sendto(p1,(adresses[1]))
p2,_=sock.recvfrom(1024)
player2=pickle.loads(p2)
sock.sendto(p2,(adresses[0]))
p1,_=sock.recvfrom(1024)
player1=pickle.loads(p1)
sock.sendto(p1,(adresses[1]))
p2,_=sock.recvfrom(1024)
player2=pickle.loads(p2)


#Playing the mach
match = Match(
    Team([champs[name] for name in player1]),
    Team([champs[name] for name in player2]))

match.play()

#Sending the results to the clients and DB
for i in range(2):
   sock.sendto(pickle.dumps(match),(adresses[i]))

sock.sendto(pickle.dumps(match),adress_to_db)


