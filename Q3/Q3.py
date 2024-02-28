#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.
