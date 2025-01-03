from random import choice



class Node:
    def __init__(self, name, type  ):
        self.name = name
        self.type = type
        self.initial_minutes= 7*50
        self.minutes = self.initial_minutes
    def dot(self):
        percentage = self.minutes/self.initial_minutes
        colour = getColour(percentage)
        print(self.name, "[color=\"", colour, "\", label=\"", self.name, "\\n", self.minutes, "\", style=filled];")


class Edge:
    def __init__(self, node_from, node_to, minutes):
        self.nodeFrom = node_from
        self.nodeTo = node_to
        self.minutes = minutes

    def print(self):
        print(self.nodeFrom, self.nodeTo, self.minutes)
    def dot(self):
        print(self.nodeFrom.name, "->", self.nodeTo.name, "[label=", self.minutes, "];")


class Model:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, name, type):
        self.nodes.append(Node(name, type))

    def add_edge(self, edge):
        self.edges.append(edge)
        edge.nodeFrom.minutes = edge.nodeFrom.minutes - edge.minutes
        edge.nodeTo.minutes = edge.nodeTo.minutes - edge.minutes

    def get_node(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def get_edge(self, name1, name2):
        for e in self.edges:
            if e[0] == name1 and e[1] == name2:
                return e
        return None

    def get_edges(self):
        return self.edges

    def get_nodes(self, type):
        result = []
        for n in self.nodes:
            if n.type == type:
                result.append(n)
        return result

    def dot(self):
        print("digraph G {")
        for n in self.nodes:
            n.dot()
        for e in self.edges:
            e.dot()
        print("}")

def getColour(value):
    red = int( (1 - (value*value) ) * 180 )
    green = int( (value * value )* 180 )

    red = "%02X" % red
    green = "%02X" % green

    return '#' + red + green +'00'


if __name__ == '__main__':

    m = Model()
    for x in range(1, 5):
        m.add_node("S" + str(x), "S")
    for x in range(5, 25):
        m.add_node("J" + str(x), "J")
    for x in range(0,24):
        m.add_edge(Edge(m.nodes[x], choice(m.get_nodes("S")), 15))
        m.add_edge(Edge(m.nodes[x], choice(m.get_nodes("S")), 15))
        #m.add_edge(Edge(m.nodes[x], choice(m.nodes), 15))


    m.dot()

