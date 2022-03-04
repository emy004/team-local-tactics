from socket import socket,AF_INET, SOCK_DGRAM
from champlistloader import load_some_champs
import pickle
sock=socket(AF_INET,SOCK_DGRAM)
sock.connect(("localhost",5555))
message=load_some_champs()
sock.sendto(pickle.dumps(message),(("localhost"),5556))
