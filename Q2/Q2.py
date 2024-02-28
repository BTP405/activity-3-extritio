#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.
