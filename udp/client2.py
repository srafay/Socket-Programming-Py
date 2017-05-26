import socket               # Import socket module
i=0;                        # for segment counts
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP connection
host = socket.gethostname() # Get local machine name
port = 12345                 # Server's port number

fileName = input("Enter the name of file you want to send(with extension) : ");
                  
f = open(fileName,'rb')
print ("Sending File name");
s.sendto(fileName.encode('latin-1'), (host,port)); # Sending File name

data, addr = s.recvfrom(1024)     # Receive acknowledge
print(data.decode());

l = f.read(1024*50)            # Read into buffer for sending
while (l):
    print ('Sending...'+str(i));
    s.sendto(l,(host,port))
    data, addr = s.recvfrom(1024)
    if (data.decode() == str(i)):   # If server acknowledges the segment number, then continue sending Else send again
        i+=1
        l = f.read(1024*50)
s.sendto("$$$0$$$".encode('latin-1'), (host,port)); # Send custom EOF
f.close()
print ("Done Sending");
s.shutdown(socket.SHUT_WR)
s.close()
