import socket               # Import socket module
import time

i=0;
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4, UDP connection
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

#while True:
data, addr = s.recvfrom(1024)     # Receive File name
s.sendto(('***Server*** Received File name: ' + str(data)).encode(), addr); # Send Acknowledge

print ('Got connection from '+ str(addr));
print ('File name = ' + str(data));
print ("Receiving...");
f = open('received files/'+str(data.strip().decode('latin-1')),'wb')
startTime = time.time();
data, addr = s.recvfrom(1024*50) # Receive data from whoever is sending
while (data):
    if (data.decode('latin-1') == "$$$0$$$"): #close connection if EOF
        break

    elif (data):
        s.sendto(str(i).encode(), addr)
        print ("Receiving..."+str(i));
        f.write(data)
        data, addr = s.recvfrom(1024*50)
        i+=1


endTime = time.time();
tTime = endTime - startTime;
f.close()
print ("Done Receiving");
print ("total time: " + str(tTime) + " seconds");
s.sendto(b'Thank you for connecting', (host,port));
s.close()                # Close the connection
