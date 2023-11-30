############################################
# FUNTIONS FOR LSH
############################################

class Node:
    def __init__(self, name):
        self.name = name

class Edge:
    def __init__(self, node_left, node_right, edge_weight=0):
        self.node_left = node_left
        self.node_right = node_right
        self.edge_weight = edge_weight
        
    def getLeft(self):
        return self.node_left
    
    def getWeight(self):
        return self.edge_weight
    
    def setWeight(self, weight):
        self.edge_weight = weight
    
    def getRight(self):
        return self.node_right 
    
    def __str__(self):
        return f"Node[{self.node_left.name}]-Weight[{self.edge_weight}]-Node[{self.node_right.name}]"

def create_edge_key(edge):
    return f'{edge.node_left.name}_{edge.node_right.name}'
    
def create_netw(zips):
    nodes = {}
    edges = {}
    
    edge_id = 0
    a_band, b_band = zips
    ka, va = a_band
    kb, vb = b_band

    node_left = Node(ka)
    node_right = Node(kb)

    """
    pairs = 0
    match = 0
    weight = 0
    for a_rows, b_rows in zip(va, vb):
        pairs += 1
        if a_rows == b_rows:
            match += 1

    nodes[node_left.name] = node_left
    nodes[node_right.name] = node_right
    if match > 0:
        weight = match/pairs
        edge = Edge(node_left, node_right, weight)
        edges[f'{node_left.name}_{node_right.name}'] = edge
    """
    
    match = False
    for a_rows, b_rows in zip(va, vb):
        if a_rows == b_rows:
            match = True
            break
    
    nodes[node_left.name] = node_left
    nodes[node_right.name] = node_right
    if (match):        
        edge = Edge(node_left, node_right, 0.0)
        edges[create_edge_key(edge)] = edge
        
    return nodes, edges