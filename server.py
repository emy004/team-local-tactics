from team_local_tactics import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from socket import socket,AF_INET, SOCK_DGRAM
from core import Champion, Match, Shape, Team
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock2=socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",5555))
sock2.bind(("localhost",5556))
#champs=load_some_champs()
#for i in range(2):
 #  test,fadress=sock.recvfrom(1024)
  # print(fadress)
  # sock.sendto(pickle.dumps(champs),(fadress))


player1=[]
player2=[]
adresses=[]
adressbook=[]
data,adress=sock2.recvfrom(1024)
champs=pickle.loads(data)
print_available_champs(champs)

while len(adresses)<2:
   test,fadress=sock.recvfrom(1024)
   #print("Recieved"+test.decode())
   #print("from",  fadress[1])
   if adress not in adresses:
     adresses.append(fadress)


for i in range(len(adresses)):
   sock.sendto(pickle.dumps(champs),(adresses[i]))

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
#sock.sendto(toplayer2.encode(),(adresses[1]))
#sock.sendto(pickle.dump(player1),(adresses[1]))

#while  (len(player2)<2):

 #data,adress=sock.recvfrom(1024)


 #if adress==adresses[0]:
  #  player1.append(data.decode())


 #elif adress!=adresses[0]:

  #  player2.append(data.decode())
    




match = Match(
    Team([champs[name] for name in player1]),
    Team([champs[name] for name in player2]))

match.play()

for i in range(2):
   sock.sendto(pickle.dumps(match),(adresses[i]))


