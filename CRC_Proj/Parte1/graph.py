import networkx as nx
import matplotlib.pyplot as plt
from itertools import count

def init_node(graph, id):
	graph.add_node(id)

def add_node_attr(graph, id, dictionary):
	info = {id: dictionary}
	nx.set_node_attributes(graph, info)

def print_info(graph):
	print("\nNumber of nodes: " + str(graph.number_of_nodes()))
	print("\nNumber of edges: " + str(graph.number_of_edges()))

def draw_graph(graph):
	plt.title("Graph Architecture", loc="center")
	pos = nx.spring_layout(graph)
	nodes = nx.draw_networkx_nodes(graph, pos)
	nodes.set_edgecolor('#000000')
	nx.draw_networkx_edges(graph, pos)
	plt.show()

def draw_nodes_by_color(graph, attribute_name):

	groups = set(nx.get_node_attributes(graph, attribute_name).values())
	mapping = dict(zip(sorted(groups),count()))
	nodes = graph.nodes()
	colors = [mapping[graph.node[n][attribute_name]] for n in nodes]

	pos = nx.spring_layout(graph)
	ec = nx.draw_networkx_edges(graph, pos, alpha=0.2)
	nc = nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color=colors, with_labels=False, node_size=100, cmap=plt.cm.jet)
	plt.colorbar(nc)
	plt.title(attribute_name+" centrality", loc="center")
	plt.axis('off')
	plt.show()

def draw_communities(graph):
	groups = set(nx.get_node_attributes(graph, "community").values())
	mapping = dict(zip(sorted(groups),count()))
	nodes = graph.nodes()
	colors = [mapping[graph.node[n]["community"]] for n in nodes]

	pos = nx.spring_layout(graph)
	nx.draw_networkx_edges(graph, pos, alpha=0.2)
	nx.draw_networkx_nodes(graph, pos, nodelist=nodes, node_color=colors, with_labels=False, node_size=100, cmap=plt.cm.jet)
	plt.axis('off')
	plt.show()