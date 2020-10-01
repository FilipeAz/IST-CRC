import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import collections
import powerlaw
import matplotlib.pyplot as plt
from graph import add_node_attr, draw_nodes_by_color, draw_communities
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def degree_dist(graph, n_nodes):
	degree_seq = sorted([d for n, d in graph.degree()], reverse=True)
	degree_count = collections.Counter(degree_seq)
	degree_list = []
	prob_degree_list = []

	for i in degree_count:
		deg = i
		prob = degree_count[i]/n_nodes
		degree_list.append(deg)
		prob_degree_list.append(prob)

	gamma = gamma_powerlaw(degree_seq)
	print("\n\tPowerLaw Gamma:" + str(gamma))
	
	return degree_list, prob_degree_list

def average_degree(n_nodes, n_edges):
	avg_degree = (2*n_edges)/n_nodes
	return avg_degree

def clustering_coeff(graph):
	tri_sum = 0
	n_triangles = nx.triangles(graph)
	for n in n_triangles:
		tri_sum += n_triangles[n]
	tri_sum /= 3

	return nx.clustering(graph), nx.average_clustering(graph), tri_sum
	
def average_path_length(graph):
	conn_components = nx.connected_component_subgraphs(graph)
	
	cc_apl = {}
	for comp in conn_components:
		cc_apl.update({list(nx.Graph(comp).nodes)[0]: nx.average_shortest_path_length(comp)})
		
	return cc_apl

def centrality_measures(graph):
	degree_dic = nx.degree_centrality(graph)
	eigenvector_dic = nx.eigenvector_centrality_numpy(graph)
	closeness_dic = nx.closeness_centrality(graph)
	betweenness_dic = nx.betweenness_centrality(graph)

	for elem in degree_dic:
		add_node_attr(graph, elem, {"degree": degree_dic[elem]})
		add_node_attr(graph, elem, {"eigenvector": eigenvector_dic[elem]})
		add_node_attr(graph, elem, {"closeness": closeness_dic[elem]})
		add_node_attr(graph, elem, {"betweenness": betweenness_dic[elem]})

def gamma_powerlaw(prob_degree_list):
	fit = powerlaw.Fit(prob_degree_list)
	return fit.power_law.alpha

def cumulative_prob(prob_degree_list):
	for i in range(len(prob_degree_list)-1):
		prob_degree_list[i+1] += prob_degree_list[i]
	return prob_degree_list

def draw_cumulative(degree_list, prob_degree_list):
	plt.title("Cumulative Degree Distribution - LogLog Scale", loc="center")
	plt.loglog(degree_list, prob_degree_list)
	plt.show()

def uniform_page_rank(graph):
	dic = nx.pagerank(graph)
	sort = {}
	for w in sorted(dic, key=dic.get, reverse=True):
		sort.update({w: dic[w]})
		
	return sort

def communities_func(graph):
	commu_list = list(greedy_modularity_communities(graph))
	n_commu = 0
	for n in commu_list:
		for elem in n:
			add_node_attr(graph, elem, {"community": n_commu})
		n_commu += 1

def network_report(graph, attribute_name):

	print("\nNetwork Structure Report:")

	n_nodes = graph.number_of_nodes()
	n_edges = graph.number_of_edges()
	avg_degree = average_degree(n_nodes, n_edges)
	print("\n\tAverage Degree:" + str(avg_degree))

	degree_list, prob_degree_list = degree_dist(graph, n_nodes)
	clustering_coefficient, average_clustering, n_triangles = clustering_coeff(graph)
	aver_path_length = average_path_length(graph)
	centrality_measures(graph)
	
	prob_degree_list = cumulative_prob(prob_degree_list)
	draw_cumulative(degree_list,prob_degree_list)

	page_rank = uniform_page_rank(graph)
	pageRank_top = {k: page_rank[k] for k in list(page_rank)[:20]}

	communities_func(graph)
	
	print("\n\tNumber of Triangles:" + str(n_triangles))
	print("\n\tNumber of Cliques: " + str(len(list(nx.algorithms.clique.enumerate_all_cliques(graph))) - graph.number_of_nodes() - graph.number_of_edges()))
	print("\n\tClustering Coefficient:" + str(clustering_coefficient))
	print("\n\tAverage Clustering Coefficient:" + str(average_clustering))
	print("\n\tAverage Path Length:" + str(aver_path_length))
	print("\n\tPage Rank Top 20:")
	for i in pageRank_top:
		print("\tID: "+str(i)+"  PageRank Vaule: "+str(pageRank_top[i])+"\tCategory: "+str(graph.node[i]["category"])+"\t\t\tRate: "+str(graph.node[i]["rate"])+"\t\tUploader: "+str(graph.node[i]["uploader"]))

	draw_nodes_by_color(graph, attribute_name)
	draw_communities(graph)