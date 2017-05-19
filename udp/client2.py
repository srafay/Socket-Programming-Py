import socket               # Import socket module
i=0;
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))

fileName = input("Enter the name of file you want to send(with extension) : ");
                  
f = open(fileName,'rb')
print ("Sending...");
s.send(fileName.encode('utf-8'));
l = f.read(1024*1000)            # Read into buffer for sending
while (l):
    i+=1
    print ('Sending...'+str(i));
    s.send(l)
    l = f.read(1024*1000)

f.close()
print ("Done Sending");
s.shutdown(socket.SHUT_WR)
s.close()
