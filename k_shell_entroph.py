import networkx as nx
import H_index
import operator
import math
import matplotlib.pyplot as plp
# nx.draw_networkx(G)
# plp.show()

def informationEntrophy(G, nodes, h, degree_dic):
    h_indexdic = {}
    for i in range(len(nodes)):
        h_indexdic[nodes[i]] = h[i]
    # h_list = [(nodes[i], h[i]) for i in range(len(nodes))]  # (alt, imp): (候选元素，重要性)
    # h_list.sort(key=lambda x: (x[1], x[0]), reverse=True)  # [(节点编号，h_index),(节点编号，h_index),...]

    I_dic = {}
    for i in nodes:
        degrees = degree_dic[i]
        values = h_indexdic[i]
        if degrees > 1:
            for j in nx.neighbors(G, i):
                values += h_indexdic[j]
        else:
            pass
        I_dic[i] = values
    return I_dic
def originalinforEntro(G, nodes, degree_dic):
    I_dic = {}
    e_dic = {}
    sum_de = 0
    for j in nodes:
        sum_de += degree_dic[j]
    for i in nodes:
        I_dic[i] = degree_dic[i] / sum_de
    for k in nodes:
        e = 0
        for k_nei in nx.neighbors(G, k):
            e += I_dic[k_nei]*math.log(I_dic[k_nei])
        e_dic[k] = -e
    return e_dic
def k_shell(graph):
    importance_dict={}
    level=1
    while len(graph.degree):
        importance_dict[level]=[]
        while True:
            level_node_list=[]
            for item in graph.degree:
                if item[1]<=level:
                    level_node_list.append(item[0])
            graph.remove_nodes_from(level_node_list)
            importance_dict[level].extend(level_node_list)
            if not len(graph.degree):
                return importance_dict
            if min(graph.degree,key=lambda x:x[1])[1]>level:
                break
        level=min(graph.degree,key=lambda x:x[1])[1]
    return importance_dict
def dic_Sort(a):
    sorted_a = sorted(a.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    b = []
    for i in range(len(a)):
        b.append(sorted_a[i][0])
    return b
def newmethod(k_shellsets, I_dic):
    a = len(k_shellsets)
    sorted_kshellsets = dict(sorted(k_shellsets.items(), key=operator.itemgetter(0), reverse=True))  # big shell is in the front
    # print(sorted_kshellsets)
    partition = []  # the kshell partition with sorted information entrophy [{nodes:entrophy}]
    for k in sorted_kshellsets.keys():  # i in [3,2,1]
        # print(i)
        par_dic = {}
        for j in k_shellsets[k]:
            par_dic[j] = I_dic[j]
        partition.append(dic_Sort(par_dic))

    influencialNodes = []
    length = []
    for f in partition:
        length.append(len(f))  # get the length of each partition

    for maxL in range(max(length)):
        for k_shelll in range(len(partition)):  # k_shell = 0,1,2
            if maxL < len(partition[k_shelll]):  # 若现在的maxL小于目前列表的长度
                influencialNodes.append(partition[k_shelll][maxL])
            else:
                pass
    return influencialNodes
# def print_f(result, name):
#     print(name, result)
#     stop = len(result)
#     slices = int(stop * 0.2)
#     print(result[:slices])

# G = nx.Graph()
# G.add_nodes_from(list(range(1, 18)))
# G.add_edges_from([(1, 2), (1, 3), (1, 5), (1, 4), (1, 6), (2, 3), (2, 4), (3, 4), (5, 6), (5, 7), (6, 7), (7, 8), (7, 9), (8, 9), (8, 16), (9, 10), (9, 11), (10, 12), (10, 14), (11, 15), (12, 13), (12, 16),  (17, 16)])

# G = nx.Graph()
# G.add_nodes_from(list(range(1, 27)))
# G.add_edges_from([(1, 2), (1, 3), (1, 5), (1, 4), (1, 8), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 11), (2, 12), (3, 4), (3, 8), (4, 23), (5, 9), (5, 10), (6, 7), (8, 26), (8, 25), (13, 15), (14, 15), (15, 17), (17, 23), (16, 23), (18, 23), (19, 23), (21, 23), (22, 23), (20, 23), (24, 25)])

# G = nx.Graph()
# G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# G.add_edges_from([(0, 1), (0, 10), (1, 2), (1, 3), (1, 5), (1, 6), (1, 7), (1, 8), (2, 3), (2, 4), (3, 4), (3, 9), (4, 7), (5, 6), (5, 8), (8, 9),(7, 10)])

# G = nx.read_edgelist('USAir97.edgelist', nodetype=int)
# G1 = nx.read_edgelist('football.edgelist')
# G = nx.read_edgelist('football.edgelist', nodetype=int)
# G = nx.read_edgelist('jazz.edgelist', nodetype=int)
#
# #
# nodes = list(nx.nodes(G))
# degree_dic = {}
# for i in nodes:
#     degree_dic[i] = nx.degree(G, i)
# #
# # nOfh_index = 0
# #
# h = H_index.calcHIndexValues(G, 0)
# # I_dic = informationEntrophy(G, nodes, h, degree_dic)
# I_dicOri = originalinforEntro(G, nodes, degree_dic)
# k_shellsets = k_shell(G)
# #
# # result = newmethod(k_shellsets, I_dic)
# resultOri = newmethod(k_shellsets, I_dicOri)
# #
# # print_f(result, 'new_method')
# print_f(resultOri, 'old_method')
#
# # nx.draw_networkx(G1)
# # plp.show()
# G = nx.read_edgelist('Facebook.edgelist')
