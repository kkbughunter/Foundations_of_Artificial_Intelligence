import networkx as nx
from matplotlib import pyplot as plt
import numpy as np

def draw(ar):
    g1 = nx.DiGraph()
    g1.add_edges_from([(ar[0], ar[2]), (ar[1], ar[2]), (ar[1], ar[3]), (ar[2], ar[4])])
    plt.tight_layout()
    nx.draw_networkx(g1, arrows=True)
    plt.savefig("g1.png", format="PNG")
    plt.clf()

def create(r,c):
    m = np.empty((r, c))
    for i in range(r):
        for j in range(c):
            m[i][j] = float(input(f"{i,j} Value : "))

    return m[r-1][c-1]

def main():
    nv = int(input("Enter the number of variables : "))
    t = ''
    v = []
    s = 1
    for i in range(nv):
        t = input("Enter the variable : ")
        v.append(t)
        print(f"Matrix for {t}")
        r = int(input("Enter the row : "))
        c = int(input("Enter the column : "))
        s *= create(r,c)

    draw(v)
    print(s," Value")
    
if __name__=="__main__":
    main()
