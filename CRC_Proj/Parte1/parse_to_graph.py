from graph import init_node, add_node_attr

def parsing_to_graph(graph, filename):
	with open(filename) as file:
		lines = file.readlines()
		for line in lines:
			elem = line.split()
			
			if len(elem) > 1:
				if elem[4] == '&':
					elem[3] += " " + elem[4] + " " + elem[5]
					del elem[4]
					del elem[4]
					
				dictionary={"uploader": elem[1],
							"age": elem[2],
							"category": elem[3],
							"length": elem[4],
							"views": elem[5],
							"rate": elem[6],
							"ratings": elem[7],
							"comments": elem[8]}
				if graph.has_node(elem[0]):
					add_node_attr(graph, elem[0], dictionary)
				else:
					init_node(graph, elem[0])
					add_node_attr(graph, elem[0], dictionary)

				for k in elem[9:]:
					if graph.has_node(k):
						graph.add_edge(elem[0],k)
					else:
						init_node(graph, k)
						graph.add_edge(elem[0],k)

			else:
				init_node(graph, elem[0])