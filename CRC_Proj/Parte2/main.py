import sys
from graph import graph_init, infect_begin, get_healthy, get_infected, infect_nodes, recover_nodes, random_graph_init


if __name__ == '__main__':


	type_graph = sys.argv[1]
	n = int(sys.argv[2])
	m0 = 3
	m = m0
	infected_rate = sys.argv[3]
	infected_rate = float(infected_rate)
	recovery_rate = sys.argv[4]
	recovery_rate = float(recovery_rate)
	begin_infected = sys.argv[5]
	begin_infected = int(begin_infected)


	if type_graph == "sf":
		graph = graph_init(n, m0, m)			#testing scale free graph
	elif type_graph == "r":
		graph =random_graph_init(6, n)			#testing random graph
	
	
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

