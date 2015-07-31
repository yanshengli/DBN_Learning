__author__ = 'lige'
#encoding:utf-8
import networkx as nx
def build_graph(word_word,word_sort,vectors,f,k):
    G=nx.DiGraph()#创建空图
    print len(word_sort)
    #print word_sort
    for i in range(0,len(word_sort)):
        G.add_node(i)#创造节点

    for i in range(0,word_word.shape[0]):
        for j in range(0,word_word.shape[1]):
            if word_word[i,j]>=1:
                G.add_edge(i,j)#加一条有向边

    #pos =nx.circular_layout(G)
    #plot.title('the orginal graph with pos')
    #nx.draw(G,pos,with_label=True,node_size=300)
    #plot.show()
    #print nx.degree(G)
    #clusters=nx.clustering(G.to_undirected())
    #print clusters
    #sort_cluster=sorted(clusters.iteritems(),key= lambda jj:jj[1],reverse=True)
    #print sort_cluster
    #print sort_cluster[len(clusters)/2+1]
    #print nx.betweenness_centrality(G)
    features=dict()
    #print vectors.shape[1]
    for i in range(0,vectors.shape[1]):
        features[i]=0
    out_cen=nx.out_degree_centrality(G)
    print out_cen
    for line in out_cen:
        print vectors[k].indices[line]
        features[vectors[k].indices[line]]=out_cen[line]
    print features

    for i in range(0,len(features)):
        f.write(str(features[i])+'\t')
    f.write('\n')



    #dia_len=nx.diameter(G.to_undirected())
    #shortest_path=nx.average_shortest_path_length(G.to_undirected())
    #clustering=nx.average_clustering(G.to_undirected())
    #f.write(str(dia_len)+'\t'+str(shortest_path)+'\t'+str(clustering)+'\t'+'\n')
    #print dia_len

    #f.write('\n')


    #print out_cen
    #print out_feature

    #clos_cen= nx.closeness_centrality(G)

    #print clos_feature


    #print nx.is_connected(G.to_undirected())
    #sub_graph= nx.strongly_connected_component_subgraphs(G)
    #strong_sub_graph_node= len(nx.nodes(sub_graph[0]))

    #f.write(str(k)+'\t'+str(dia_len)+'\t'+str(shortest_path)+'\t'+str(clustering)+'\t'+'\n')


