import socket               # Import socket module
i=1;                        # Will be used in received file's name
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    f = open('received files/file'+str(i)+'.png','wb')
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from '+ str(addr));
    print ('c = ' + str(c) + '; addr = ' + str(addr));
    print ("Receiving...");
    l = c.recv(1024)        ## Receive data from socket (buffer size 1024)
    while (l):
        print ("Receiving...");
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Done Receiving");
    c.send(b'Thank you for connecting');
    c.close()                # Close the connection
    i+=1                     # For unique file naming