from team_local_tactics import *
from champlistloader import load_some_champs
from socket import socket, AF_INET,SOCK_DGRAM, create_connection
import pickle

sock=socket(AF_INET,SOCK_DGRAM)
sock.connect(("localhost",5555))
message="Hi"
sock.sendto(message.encode(),(("Localhost",5555)))


data,_=sock.recvfrom(1024)
champs=pickle.loads(data)
print_available_champs(pickle.loads(data))

#data,_=sock2.recvfrom(2048)
#champs=pickle.loads(data)
#champs=load_some_champs()
#print_available_champs(champs)


player=[]

while True:
   champ=input("Choose your Champion:"  )
   if champ in player:
        print ("You have already chosen that champion")
   elif champ not in champs:
        print ("Not a valid champion")
   else:
        player.append(champ)
        if len(player)==2:
            break




for i in range(2):
    sock.sendto(player[i].encode(),(("Localhost",5555)))




data,_=sock.recvfrom(2048)
match=pickle.loads(data)
print_match_summary(match)
