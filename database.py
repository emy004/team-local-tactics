#Imports
from socket import socket,AF_INET, SOCK_DGRAM
from champlistloader import load_some_champs
import pickle

#Sending available champions to the server
sock=socket(AF_INET,SOCK_DGRAM)
message=load_some_champs()
sock.sendto(pickle.dumps(message),(("localhost"),5555))

#Recieving the match results
incmatch,_=sock.recvfrom(1024)
match=pickle.loads(incmatch)

#Write the match results in binary format to a txt file
f=open("match_history.txt","ab")
pickle.dump(match,f)
f.close()

