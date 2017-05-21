import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
    c, addr = s.accept()     # Establish connection with client.
    
    print ('Got connection from '+ str(addr));
    print ('c = ' + str(c));
    print ("Receiving...");
    fileName = c.recv(1024)
    f = open('received files/'+str(fileName.decode('utf-8')),'wb')

    startTime = time.time();
    l = c.recv(1024*50)        ## Receive data from socket (buffer size 1024)
    while (l):
        print ("Receiving...");
        f.write(l)
        l = c.recv(1024*50)
        
    endTime = time.time();
    tTime = endTime - startTime;
    f.close()
    print ("Done Receiving");
    print ("total time: " + str(tTime));
    c.send(b'Thank you for connecting');
    c.close()                # Close the connection
