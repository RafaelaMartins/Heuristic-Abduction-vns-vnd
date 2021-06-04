import random

from graph import Graph


def get_rgb_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return str(r)+" "+str(g)+" "+str(b)

def generate_dot(graph: Graph, file_name):

    text = "graph G {\n"

    #for v in graph.vertex_list():
    #    text += "\t"+v.label + " [color="+color[v.color]+",style=filled]\n"

    for v in graph.vertex_list():
        for w in graph.adjacent_list(v):
            text += "\t"+v.label + " -- " + w.label + "\n"
    text += "}"

    with open(file_name+".dot", "w") as file:
        file.write(text)