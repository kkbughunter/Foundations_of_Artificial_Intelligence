from queue import PriorityQueue
import math
g={}
node={}
pos={}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
f = {}
visited = set()
def create_graph():
  g['A'].append(('B', 9))
  g['B'].append(('A', 9))
  g['A'].append(('C', 6))
  g['C'].append(('A', 6))
  g['B'].append(('D', 5))
  g['D'].append(('B', 5))
  g['C'].append(('D', 8))
  g['D'].append(('C', 8))
  g['D'].append(('E', 7))
  g['E'].append(('D', 7))
  g['C'].append(('F', 5))
  g['F'].append(('C', 5))
  g['D'].append(('G', 6))
  g['G'].append(('D', 6))
  g['H'].append(('E', 4))
  g['E'].append(('H', 4))
  g['G'].append(('F', 7))
  g['F'].append(('G', 7))
  g['H'].append(('G', 8))
  g['G'].append(('H', 8))

def manhattan_dst(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def Euclidean_dst(x1, y1, x2, y2):
  sum=0
  sum+=(abs(x1-x2) * abs(x1-x2))
  sum+=(abs(y1-y2) * abs(y1-y2))
  result=round(math.sqrt(sum),2)
  return result

 
def greedy_best_fs(x, y, select):
    global f, visited
    cost = 0
    cas =0
    visited = set()
    t = node[(x, y)]
    if(select == 0):
        f[t] = manhattan_dst(x, y, 3, 3)
    else:
        f[t] = Euclidean_dst(x, y, 3, 3)
    path = []
    q = PriorityQueue()
    q.put((f[t], t, cost))  
    while q.qsize() > 0:
        (c1, t1, g1) = q.get()
        if t1 in visited:
            continue
        visited.add(t1)
        print((c1, t1, g1)) 
        path.append(t1)
        if t1 == 'H':
            break
        for (t, c1) in g[t1]:
            (x1, y1) = pos[t]
            if(select == 0):
                f[t] = manhattan_dst(x1, y1, 3, 3)
            else:
                f[t] = Euclidean_dst(x1, y1, 3, 3)
            q.put((f[t], t, g1 + c1))  
        cas = g1 + c1
    print("Path =>", path)
    print("Cast =>", cas)
def a_star(x, y , select):
  global f, visited
  visited=[]
  f = {}
  path = []
  cas = []
  t = node[(x, y)]
  if(select==0):
      f[t] = manhattan_dst(x, y, 3, 3)
  else:
      f[t] = Euclidean_dst(x, y, 3, 3)
  q = PriorityQueue()
  q.put((f[t], 0, t))
  while q.qsize() > 0:
    (c1, g1, t1) = q.get()
    if t1 in visited:
      continue
    visited.append(t1)
    print((c1, g1, c1 - g1, t1))
    path.append(t1)
    if t1 == 'H':
      break
    while q.qsize() > 0:
        (c2,g2,t2)=q.get()
        visited.append(t2)
    for (t, c2) in g[t1]:
        if(t not in visited):
            (x1, y1) = pos[t]
            if(select==0):
                f[t] = manhattan_dst(x1, y1, 3, 3) + c2 + g1   
            else:
                f[t] = Euclidean_dst(x1, y1, 3, 3) + c2 + g1 
            q.put((f[t], c2 + g1, t))
            cas = c2 + g1
  print("Path =>", path)
  print("Cast =>", cas)

c = 'A'
for i in range(1, 4):
  for j in range(1, 4):
    if i == 1 and j == 3:
      continue
    node[(i, j)] = c
    pos[c] = (i, j)
    g[c] = []
    c = chr(ord(c) + 1)
 
create_graph()

char='A'
print("Estimated Cost : Manhattan Distance")
for i in range(1,4):
   for j in range(1,4):
       if(i==1 and j==3):
          continue
       else:
          print(char," : ",manhattan_dst(i, j, 3, 3))
          char=chr(ord(char)+1)
char='A'
print("\nEstimated Cost : Euclidean Distance")
for i in range(1,4):
   for j in range(1,4):
       if(i==1 and j==3):
          continue
       else:
          print(char," : ",Euclidean_dst(i, j, 3, 3))
          char=chr(ord(char)+1)


print("\nGreedy Best First Search (Manhattan Distance)")
greedy_best_fs(1,1,0)
print("\nA_star Search (Manhattan Distance)")
a_star(1,1,0)

print("\nGreedy Best First Search (Euclidean Distance)")
greedy_best_fs(1,1,1)
print("\nA_star Search (Euclidean Distance)")
a_star(1,1,1)




