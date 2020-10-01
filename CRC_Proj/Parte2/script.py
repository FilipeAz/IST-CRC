import numpy as np
import sys
from graph import graph_init, infect_begin, get_healthy, get_infected, infect_nodes, recover_nodes, random_graph_init

def run_script(type_graph, n_nodes, infected_rate, recovery_rate, begin_infected):
	m0 = 3
	m = m0
	

	if type_graph == "sf":
		graph = graph_init(n_nodes, m0, m)			#testing scale free graph
	elif type_graph == "r":
		graph =random_graph_init(6, n_nodes)	    #testing random graph
	
	
	f = open("results" + str(infected_rate)	+ ".txt", "a")
	

	infect_begin(graph, begin_infected)
	
	
	healthy_nodes = get_healthy(graph)
	infected_nodes = get_infected(graph)

	f.write(type_graph + "\n")
	f.write("healthy: " + str(len(healthy_nodes)) + "\n")
	f.write("infected: " + str(len(infected_nodes)) + "\n")	

	i = 0
	while i <= 20:
		just_infected = infect_nodes(graph, infected_rate)
		recover_nodes(graph, recovery_rate, just_infected)
		i += 1
		
	healthy = "healthy: " + str(len(get_healthy(graph)))
	infected = "infected: " + str(len(get_infected(graph)))
	

	
	f.write(healthy + "\n")
	f.write(infected + "\n")
	f.write("infected_rate: " + str(infected_rate) + "\n")
	f.write("recovery_rate: " + str(recovery_rate) + "\n\n")

	f.close()


if __name__ == '__main__':

	for i in range(3):
		for j in np.arange(0.025, 0.525, 0.025):
			run_script(sys.argv[1], int(sys.argv[2]), j, 0.5, int(sys.argv[3]))
			
			
	vec = []
	for i in np.arange(0.025, 0.525, 0.025):
		f = open("results" + str(i) + ".txt", "r")
		x = f.readlines()
		med =(int(x[4].split()[1]) + int(x[12].split()[1]) + int(x[20].split()[1]))/3
		vec.append(float("{0:.2f}".format(med/(int(sys.argv[2])/100))))
		f.close()

	print(len(vec))
	print(vec)