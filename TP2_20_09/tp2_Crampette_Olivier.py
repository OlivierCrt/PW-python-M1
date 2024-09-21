import numpy as np 
import matplotlib as plt 

#Echauffement
class Stack :

    def __init__(self) :
        self.liste = []


    def push(self,NewElement) :
        self.liste.append(NewElement)
        return True
    

    def pop(self) :
        if len(self.liste) == 0 :
            return None
        

        res = self.liste.pop()
        return res
    


    def get_top(self) :
        if not self.isEmpty() :
            return self.liste[-1]
        return None
    
    def get_liste(self):
        return self.liste


    def size(self) :
        return len(self.liste)
    
    def isEmpty(self):
        return len(self.liste) == 0

    def printStack(self) :
        print(self.liste)


stackTest = Stack()
stackTest.printStack()
stackTest.push(1)
stackTest.push(2)
stackTest.push(3)
stackTest.printStack()
stackTest.pop()
stackTest.printStack()

#Graph

class Graph :
    def __init__(self) :
        self.node_dict = dict()

    def printGraph(self) :
        print(self.node_dict)
    def setDict(self,dictP) :
        self.node_dict=dictP

    def getDict(self): 
        return self.node_dict

    def depth_first_search(self,starting_state) :
        stack=Stack()
        stack.push(starting_state)
        deja_vu=[]#;)


        while not stack.isEmpty( ) :
            current_node=stack.pop()
            if current_node not in deja_vu :
                deja_vu.append(current_node)
            neighbour= self.getDict()[current_node]


            for i in neighbour :
                if i not in deja_vu :
                    stack.push(i)

                
        return deja_vu
    


graph_dict = {
    'A': ['B','C'],
    'B': ['I', 'K'],
    'C': ['D'],
    'D': ['E','F'],
    'E': [],
    'F': ['H', 'G'],
    'G' : [],
    'H' : [],
    'I' :[],
    'K' : []
    
}
graph_test=Graph()
graph_test.setDict(graph_dict)

print(graph_test.depth_first_search('A'))







