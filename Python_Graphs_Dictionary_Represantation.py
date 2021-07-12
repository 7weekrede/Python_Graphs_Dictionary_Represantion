graph = {}

def add_node(v):
    if v in graph:
        print("Node is Already Present in Graph")
    else:
        graph[v] = []
def add_edge(v1,v2,value):
    if v1 not in graph:
        print(v1, " is not Present in the Graph")
    elif v2 not in graph:
        print(v2," is not Present in the Graph")
    else:
        list1 = [v2,value]
        list2 = [v1,value]
        graph[v1].append(list1)
        graph[v2].append(list2)
def delete_node(v):
    if v not in graph:
        print(v," is not Present in Nodes")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1, " is not Present in the Graph")
    if v1 not in graph:
        print(v2," is not Present in the Graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
        if v1 in graph[v2]:
            graph[v2].remove(v1)


add_node(100)
add_node(200)
add_node(300)
add_edge(100,200,20)
add_node(400)
add_node(500)
add_node(600)

print(graph)
delete_node(400)
print(graph)
