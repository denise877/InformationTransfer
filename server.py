#Author Name:Yaoqi Li
#StudentID:20222990

#This is a server file which bind to client file to send and recieve data
import socket

from pathlib import Path

#Create a socket and bind to client
def create_socket():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host=socket.gethostname()
    port=8000
    serversocket.bind((host,port))
    serversocket.listen(5)
#Recieve file name and location from client
#Read data from given directory and file
#Send data back to client
    while True:
        clientsocket,addr = serversocket.accept()
        recieveData = clientsocket.recv(4096)
        info=recieveData.decode('utf-8')
        file_name=info.split()[0]
        file_location=info.split()[1]
        p=CreatePath(file_location)
        fp=p/Path(file_name)
        file=fp.open('r')
        file_info=file.readlines()
        for line in file_info:
            line1=line.encode(encoding='utf-8')
            clientsocket.send(line1)
        clientsocket.send(b'None')
        file.close()

#Create a directory, if the directory does not exist, create a new dierctory
def CreatePath(file_location):
    p=Path(file_location)
    if p.exists():
        return p
    else:
        p.mkdir()
        return p


    
if __name__ == '__main__':
    create_socket()
    
