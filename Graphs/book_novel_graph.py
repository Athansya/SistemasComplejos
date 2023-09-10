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
    G = nx.DiGraph()

    for character in data:
        G.add_node(character)

    for character, relationships in data.items():
        for related_character, count in relationships.items():
            G.add_edge(character, related_character, weight=count)

    # Calculate node sizes based on the sum of relationship values
    node_sizes = [node_sizes.get(node, 1) * 10 for node in G.nodes()]  # Default size is 100 for nodes not in the dict
    
    # Calculate node positions
    pos = nx.drawing.nx_agraph.graphviz_layout(G)

    plt.figure(figsize=(20, 20))
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='lightblue')
    plt.savefig("./Graphs/novel_graph.png")


if __name__ == "__main__":
    main()