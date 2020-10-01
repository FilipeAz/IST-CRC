# CRC
Complex Network Course Project

Group number 90:
82033 - Ana Cardoso
82468 - Filipe Azevedo
82517 - Martim Zanatti

Requirements:
	Python 3
	Library Networkx 2.2

To run the code:
>> python main.py type_graph(sf or r) number_nodes infect_rate recovery_rate nodes_infected_at_the_beginning 


In main.py we run our simulations and the results will appear on a file.txt with the name results + infect_rate variable choosen at the beginning. It returns a set of information that we think is relevant to understand how networks behave. We print the type of graph (Scale-Free or Random), initial healthy nodes , initial infected nodes, final healthy nodes, final infected nodes, infect rate and recovery rate into the file.

In graph.py are the functions used to manipulate the graph.   

We use an auxiliary script to help us run our simulation more efficiently (script.py)
>> python script.py type_graph(sf or r) number_nodes infect_rate recovery_rate nodes_infected_at_the_beginning 








