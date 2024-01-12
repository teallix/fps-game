import sys
import select
import socket
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)
I = select.POLLERR
# Listen for incoming connections
server.listen(5)
# Sockets from which we expect to read
inputs = [ server ]

# Sockets to which we expect to write
outputs = [ ]

message_queues = {}

while inputs:
    
    # Wait for at least one of the sockets to be ready for processing
    print(sys.stderr, '\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
 # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print(sys.stderr, 'new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = queue.Queue()
            
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()))
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
                    
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print(sys.stderr, 'output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print(sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
            
        for s in exceptional:
            print(sys.stderr, 'handling exceptional condition for', s.getpeername())
            # Stop listening for input on the connection
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
                s.close()
            
            # Remove message queue
            del message_queues[s]