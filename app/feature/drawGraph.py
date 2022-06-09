import math
import matplotlib.pyplot as plt
import networkx as nx


def drawGraph(path):
    # f = open('/Users/leminhdung/Documents/VS/Code/TKDGTT/CK/data.tsp')
    if "data" not in path: quit()
    path_ = path
    if 'greedy' in path or 'sa' in path or 'tabu' in path: 
        t = path.index("data")
        path_ = path[:t]+"data.tsp"
    f = open(path_)
        
    data = []
    check = False

    for line in f:
        if line.strip() == "NODE_COORD_SECTION":
            check = True
        elif check:
            if line.strip() != "EOF":
                arr = line.strip().split(" ")
                data.append(arr[1:])
    n = len(data)
    G = nx.Graph()

    for i in  range(1,n+1):
        G.add_node(i,pos = (float(data[i-1][0]),float(data[i-1][1])))
        for j in range(i+1,n+1):
            t =math.sqrt(pow(float(data[i-1][0])-float(data[j-1][0]),2)+pow(float(data[i-1][1])-float(data[j-1][1]),2))
            G.add_edge(i,j,weight = round(t,2))

    pos=nx.spring_layout(G) 
    
    if 'tsp' in path:
        nx.draw_networkx(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,font_size=5,edge_labels=labels)
        # plt.show()
    elif 'greedy' in path or 'sa' in path or 'tabu' in path : 
        res = []
        f1 = open(path)
        
        # f1 = open('/Users/leminhdung/Documents/VS/Code/TKDGTT/CK/data.greedy.20222205.tour')
        check1 = False

        for line in f1:
            if line.strip() == "TOUR_SECTION":
                check1 = True
            elif check1:
                if line.strip() != "EOF":
                    arr = line.strip().split(" ")
                    for e in arr: 
                        if e != "": res.append(int(e))
        b = []     
        for  i in range(n-1):
            b.append(res[i:i+2]) 
        # print(b)
        colors = []
        edges = G.edges()
        for u,v in edges:
            # print([u,v])
            # print([u,v] in res)
            
            if [u,v] in b or [v,u] in b:
                colors.append('r')
            else: colors.append('b')
        weights = [G[u][v]['weight'] for u,v in edges]
        print(weights)
        # print(colors)
        nx.draw(G, pos, edge_color=colors)


    plt.show()
    
if __name__ == '__main__':
    path=str(input("Input path: "))
    # path ="/Users/leminhdung/Documents/VS/Code/TKDGTT/CK/data.greedy.20222205.tour"
    drawGraph(path)
