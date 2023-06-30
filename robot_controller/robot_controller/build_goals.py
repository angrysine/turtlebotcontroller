import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem as tsp

# Build the graph
def build_graph(data):
    nodes, edges = data["nodes"], data["edges"]
    graph = {}
    for node in nodes:
        edge_in_node = {}
        for edge in edges: 
            if edge['target'] == node['id'] or edge['from'] == node['id']:
                edge_in_node[(edge['target'] if edge['from'] == node['id'] else edge['from'])] = {'weight': edge['weight']}

        graph[node['id']] = edge_in_node
    return graph, nodes

def build_goals(data):
    graph, nodes = build_graph(data)
    goals = []

    for node_id in tsp(nx.Graph(graph)):
        for node in nodes:
            if node['id'] == node_id:
                goals.append((node['x']/500, node['y']/500))
                break
    
    return goals