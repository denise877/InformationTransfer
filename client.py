#Author Name: Yaoqi Li
#StudentID:20222990

#This is a client file which connect to the server file to send and recieve data

import socket
import os
from pathlib import Path

#Ask the name of file and directory of file.
def getfile_info():
    file_name=input("What is the file's name:")
    file_location=input("What is the file's location:")
    return file_name,file_location

#Create a socket and connect to the server and send data to server
def create_socket(file_name,file_location):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    host=socket.gethostname()
    port=8000
    mysocket.connect((host,port))
    message_send=(file_name+'\n'+file_location).encode(encoding='utf-8')
    mysocket.send(message_send)
    list1=[]
#Use while loop to keep recieve data from server
#Append recieved data to a list
    while True:
        recieveData = mysocket.recv(4096)
        if recieveData == b'None':
            break
        else:
            data=recieveData.decode('utf-8')
            list1.append(data)
    return list1

#Create a Client Folder and write recieved data into a new txt file
def write_file(file_name,file_location,filelist):
    p1=os.getcwd()
    p2=Path(p1)
    p=p2/Path('ClientFolder')
    if not p.exists():
        p.mkdir()
    new_file=p/Path(file_name)
    file=new_file.open('w+')
    for line in filelist:
        file.write(line)
    file.close()
   
if __name__ == '__main__':
    file_name,file_location=getfile_info()
    data_list=create_socket(file_name,file_location)
    write_file(file_name,file_location,data_list)

