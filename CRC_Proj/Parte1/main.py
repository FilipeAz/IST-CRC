import networkx as nx
import sys
from graph import print_info, draw_graph
from parse_to_graph import parsing_to_graph
from metrics import network_report

if __name__ == '__main__':

	G = nx.Graph()

	if len(sys.argv)<2:
		print("ERROR: No filename was given")

	else:
		filename = sys.argv[1]
		parsing_to_graph(G,filename)
		print_info(G)
		
		#To draw the graph of Degree Centrality, Eigenvector Centrality, Closeness Centralty and Betweenness Centrality where the nodes are coroled
		#depending on they values of the measures
		#Change this varialbe according to the measure to be observed.
		#Possible attribute names: "degree", "eigenvector", "closeness", "betweenness"
		attr_name = "degree"
		network_report(G, attr_name)

		#Just draw the network structure
		#draw_graph(G)
		G.clear()