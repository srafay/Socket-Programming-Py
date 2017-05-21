import socket               # Import socket module
i=0;                        # for segment counts
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP connection
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

#s.connect((host, port))

fileName = input("Enter the name of file you want to send(with extension) : ");
                  
f = open(fileName,'rb')
print ("Sending File name");
s.sendto(fileName.encode('latin-1'), (host,port));
l = f.read(1024*50)            # Read into buffer for sending
while (l):
    i+=1
    print ('Sending...'+str(i));
    s.sendto(l,(host,port))
    l = f.read(1024*50)
s.sendto("$$$0$$$".encode('latin-1'), (host,port)) # Custom EOF
f.close()
print ("Done Sending");
s.shutdown(socket.SHUT_WR)
s.close()
