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
>> python main.py "0.txt"

In the terminal it will appear the "Network Report" that concerns some characteristics of the network constructed.

When the images show up, the code will continue runing after the images windows are closed

To change the visualization of the metrics centrality:
>> Go to file main.py 
>> Change the attribute "attr_name" to one of the possible strings ("degree", "eigenvector", "closeness" and "betweenness")

In main.py, we make the verification of the input in the terminal, and call the function to create the graph from the txt file and the function that will compute all the metrics

In parse_to_graph.py, we read the dataset of the txt file and we convert each instance in nodes and associate their information.

In graph.py are the functions used to manipulate the graph.

In metrics.py are the functions to compute all the metrics and the information that we retreived.