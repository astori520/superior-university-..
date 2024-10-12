#LAB 05
# Task 1: DFS with Stack & Node
class Node:
    def __init__(self,value):
        self.value = value
        self.neighbours = []
    def add_neighbours(self,node):
        self.neighbours.append(node)
def dfs_with_stack(start_node):
    stack = []
    visited = set()
    stack.append(start_node)
    print(f'starting dfs from node: {start_node.value}')
    while stack:
        node = stack.pop()
        if node not in visited:
            print(f'visited: {node.value}')
            visited.add(node)
            print(f'neighbors of {node.value} (to visit next): {[neighbours.value for neighbours in reversed(node.neighbours) if neighbours not in visited ]}')
            
            for neighbours in reversed(node.neighbours):
                if neighbours not in visited:
                    stack.append(neighbours)
    print(" DFS complete")
def perform_dfs_on_list(node_list):
    if not node_list:
        print("no nodes to traverses") 
        return
    start_node = node_list[0]
    print(f'nodes provided: {[node.value for node in node_list]}')

    dfs_with_stack(start_node)

                      

if __name__ == "__main__":
    p = Node("P")
    q = Node("Q")
    r = Node("R")
    s = Node("S")
    t = Node("T")
    p.add_neighbours(q)
    p.add_neighbours(q)
    q.add_neighbours(s)
    r.add_neighbours(t)
    nodes = [p,q,r,s,t]
    perform_dfs_on_list(nodes)
