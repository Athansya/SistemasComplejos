'''
File: book_novel_graph.py
Project: Graphs
File Created: Saturday, 9th September 2023 12:21:46 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Saturday, 9th September 2023 12:21:48 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
'''

import json
import matplotlib.pyplot as plt
import networkx as nx



def main():
    # Load dictionary
    with open("./Graphs/related_names.json", 'r') as json_file:
        data = json.load(json_file)

    with open("./Graphs/name_counts.json", 'r') as json_file:
        node_sizes = json.load(json_file)


    # Creates directed graph
    G = nx.Graph()

    for character in data:
        G.add_node(character)

    for character, relationships in data.items():
        for related_character, count in relationships.items():
            G.add_edge(character, related_character, weight=count)

    # Calculate node sizes based on the sum of relationship values
    node_sizes = [node_sizes.get(node, 1) * 10 for node in G.nodes()]  # Default size is 100 for nodes not in the dict
    
    # Extract edge weights from the graph
    edge_weights = [G[character][target_character]['weight'] for character, target_character in G.edges()]

    # Calculate node positions
    pos = nx.drawing.nx_agraph.graphviz_layout(G)

    plt.figure(figsize=(20, 20))
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='lightblue', width=edge_weights)
    plt.savefig("./Graphs/novel_graph.png")

    # Extract graph properties
    graph_properties = {}
    graph_properties["Number_of_nodes"] = G.number_of_nodes()
    graph_properties["Number_of_edges"] = G.number_of_edges()
    graph_properties["Degrees_of_nodes"] = [G.degree(node) for node in G.nodes()]
    graph_properties["Density"] = nx.density(G)
    graph_properties["Number_of_connected_components"] = nx.number_connected_components(G)
    graph_properties["Clustering_coefficient"] = nx.clustering(G)
    # graph_properties["Eccentricity"] = nx.eccentricity(G)  # Not possible because graph is not connected
    graph_properties["Betweenness_centrality"] = nx.betweenness_centrality(G)
    # graph_properties["Diameter"] = nx.diameter(G)  # Not possible because graph is not connected
    with open("./Graphs/graph_properties.json", 'w') as json_file:
        json.dump(graph_properties, json_file)


if __name__ == "__main__":
    main()