__author__ = 'LiGe'
#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as plot
from file_to_graph import file_to_mat

def build_graph(mat):
    G=nx.DiGraph()#创建空图
    for i in range(0,mat.shape[0]):
        G.add_node(i)#创造节点
    for i in range(0,mat.shape[0]):
        for j in range(0,mat.shape[1]):
            if mat[i,j]==1:
                G.add_edge(i,j)#加一条有向边

    #print nx.in_degree(G,0)
    #print nx.out_degree(G)
    #print nx.degree(G)
    print nx.clustering(G.to_undirected())
    print G.in_degree(1)
    #nx.convert_to_undirected(G)
    #nx.convert_to_undirected()
    print nx.betweenness_centrality(G)
    print nx.closeness_centrality(G)
    #print nx.diameter(G)
    print nx.average_shortest_path_length(G)
   # print nx.average_clustering(G)
    sub_graph= nx.strongly_connected_component_subgraphs(G)
    for line in sub_graph:
        print nx.degree(line)
        #pos =nx.circular_layout(G)
        #plot.title('the orginal graph with pos')
        #nx.draw(G,pos,with_label=True,node_size=300)
        #plot.show()
        nx.draw(line, with_label=True)
        plot.show()


if __name__=='__main__':
    file='benapi_renew/mmc.exe.txt'
    mat=file_to_mat(file)
    build_graph(mat)
