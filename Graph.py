import pygame as pg
from pygame import Vector2 as Vec2

class Node:
    next_node_id = 0
    
    def __init__(self, position : Vec2):
        self.index = Node.next_node_id
        Node.next_node_id += 1
        
        self.position : Vec2 = position
        
        #extra info - to implement
    
    def __str__(self) -> str:
        return("node-" + str(self.index) + ", " + str(self.position))
    

class Edge:
    def __init__(self, node_index_1 : int, node_index_2 : int, weight : int = 1) -> None:
        self.from_node : int = node_index_1
        self.to_node : int = node_index_2
        self.weight = weight
        
    def __str__(self) -> str:
        return(str(self.from_node)+"-"+str(self.to_node)+": "+str(self.weight))
        
class SparceGraph:
    def __init__(self) -> None:
        self.node_vector : list[Node] = []
        self.edge_list_vector : list[list[Edge]] = []
        self.is_digraph : bool = False
        
    def add_node(self, node : Node) -> int :
        self.node_vector.insert(node.index, node)
        self.edge_list_vector.insert(node.index, list())
        
    
    def remove_node(self, node_id : int) -> None :
        pass
    
    def add_edge(self, edge : Edge) -> None :
        if self.is_edge_unique(edge.from_node, edge.to_node): 
            self.edge_list_vector[edge.from_node].append(edge)
            if not self.is_digraph:
                self.edge_list_vector[edge.to_node].append(Edge(edge.to_node, edge.from_node, edge.weight))
            
    def is_edge_unique(self, from_n : int, to_n : int) -> bool :
        for edge in self.edge_list_vector[from_n] :
            if edge.to_node == to_n: 
                print("wrong edge")
                return False
        return True
    
    def remove_edge(self, from_node, to_node) -> None :
        pass
    
    def no_of_nodes(self) -> int :
        return len(self.node_vector)
    
    def no_of_edges(self) -> int :
        total = 0
        for index in self.edge_list_vector:
                total+=len(index)
        return total
                
    
    def is_empty(self) -> bool :
        if len(self.node_vector)==0: return True
        else: return False
    
    def is_in_graph(self, node : int) -> bool :
        pass
    
    def __str__(self) -> str:
        temp = ""
        for node in self.node_vector:
            temp += str(node) + "\n"
        return temp
    