import networkx as nx
import numpy as np
import powerlaw
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

def add_node_attr(graph, id, dictionary):
	info = {id: dictionary}
	nx.set_node_attributes(graph, info)

def gamma_powerlaw(conn_prob):
	prob_degree_list = [i / sum(conn_prob) for i in conn_prob]
	gamma = powerlaw.Fit(prob_degree_list).power_law.alpha
	print(gamma)

def random_graph_init(d,n): #init random graph 
	graph = nx.random_regular_graph(d,n)

	for i in range(n):
		add_node_attr(graph, i, {"infected":0})
	
	return graph	

def graph_init(n, m0, m): #init scale-free graph
	graph = nx.Graph()

	for i in range(m0):
		graph.add_node(i)
		add_node_attr(graph, i, {"infected":0})

	conn_prob = [(1) for i in range(m0)]

	while m0 < n:
		id_choosen = np.random.choice(a=m0, size=m, p=[x / sum(conn_prob) for x in conn_prob], replace=False)
		graph.add_node(m0)
		add_node_attr(graph, m0, {"infected":0})
		
		conn_prob.append(m)
		for i in id_choosen:
			graph.add_edge(m0, i)
			conn_prob[i] += 1
		m0 += 1

	#gamma_powerlaw(conn_prob)

	return graph

def print_degree_graph(graph):
	for v in nx.nodes(graph):
		print(v, nx.degree(graph,v))

def get_healthy(graph):
	healthy_nodes = [node for node, attr in graph.nodes(data=True) if attr['infected']==0]
	return healthy_nodes

def get_infected(graph):
	infected_nodes = [node for node, attr in graph.nodes(data=True) if attr['infected']==1]
	return infected_nodes

def infect_begin(graph, n_nodes):
	graph_size = len(graph)
	to_infect = np.random.choice(a=graph_size, size=n_nodes, replace=False)
	for x in to_infect:
		add_node_attr(graph, x, {"infected":1})
		
def infect_nodes(graph, infected_rate): #infect nodes every time step
	healthy_nodes = get_healthy(graph)
	infected = []
	for node in healthy_nodes:
		for neighbor in graph.neighbors(node):
			if node_state_by_id(graph, neighbor) == 1:
				infected.append(node)
				add_node_attr(graph, node, {"infected":np.random.choice(a=[0,1], p=[1-infected_rate, infected_rate])})
				break

	return infected
				
def recover_nodes(graph, recovery_rate, just_infected): #cure nodes every time step
	infected_nodes = get_infected(graph)
	inf = [node for node in infected_nodes if node not in just_infected]
	for node in inf:
		add_node_attr(graph, node, {"infected":np.random.choice(a=[0,1], p=[recovery_rate, 1-recovery_rate])})
	
	
def node_state_by_id(graph, id):
	return nx.get_node_attributes(graph,"infected")[id]




