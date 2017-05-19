import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

while True:
    data, addr = s.recvfrom(1024)     # Establish connection with client.
    
    print ('Got connection from '+ str(addr));
    print ('data = ' + str(data));
    print ("Receiving...");
#    fileName = s.recvfrom(1024)
    f = open('received files/'+str(data.strip().decode('utf-8')),'wb')
    data, addr = s.recvfrom(1024)        ## Receive data from socket (buffer size 1024)
    while (data):
        if (data.decode('utf-8') == "$$$0$$$"):
            break
        print ("Receiving...");
        f.write(data)
        data, addr = s.recvfrom(1024)
    f.close()
    print ("Done Receiving");
    s.sendto(b'Thank you for connecting', (host,port));
    s.close()                # Close the connection
