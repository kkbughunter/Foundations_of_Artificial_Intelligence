
class aomaze:
  def __init__(self):
    self.graph={"A":["B","C"],
      "B":["D"],
      "C":["F"],
      "D":["C","G","E"],
      "E":["H"],
      "F":["G"],
      "G":["F","H"],
      "H":[]
     }
    self.and_adj=[["D","C","F"],["D","G","F"]]
    self.cost=[["A","B",9],
              [ "A","C",6],
              ["B","D",5],
              ["D","C",8],
              ["C","F",5],
              ["F","G",7],
              ["G","H",8],
              ["D","G",6],
              ["G","F",7]]
    self.path=[]
    
  def change_cost(self,cost,node1,node2,val):
    for i in cost:
      if (i[0]==node1 and i[1]==node2) or (i[0]==node2 and i[1]==node1):
        i[2]=val
        
  def find_all_paths(self, start, end, path=[]):
      path = path + [start]
      if start == end:
        return [path]
      if start not in self.graph:
        return []
      paths = []
      for node in self.graph[start]:
        if node not in path:
            new_paths = self.find_all_paths(node, end, path)
            for new_path in new_paths:
                paths.append(new_path)

      return paths
  def print_all_paths(self):
      start="A"
      goal="H"
      package="F"
      path1=self.find_all_paths(start,package)
      path2=self.find_all_paths(package,goal)
      for i in range(len(path1)):
        path1[i].pop(-1)
        for j in range(len(path2)):
          path_x=path1[i]+path2[j]
          self.path.append(path_x)

  def already(self,x,path):
    for i in path:
      if(x==i):
        return True
    return False
  def find_cost(self,cost,x,y):
    for i in cost:
      if(i[0]==x and i[1]==y) or (i[0]==y and i[1]==x):
        return i[2]
    return 0
  def cpy(self):
    return [["A","B",9],
              [ "A","C",6],
              ["B","D",5],
              ["D","C",8],
              ["C","F",5],
              ["F","G",7],
              ["G","H",8],
              ["D","G",6],
              ["G","F",7]]
  def path_cost(self,path):
    path=path[::-1]
    cost=self.cpy()
    flag=0
    for i in range(len(path)):
      flag=0
      for j in range(len(self.and_adj)):
        if(i!=0 or i!=1):
          if(path[i] in self.and_adj[j] and path[i-1] in self.and_adj[j] and path[i-2] in self.and_adj[j] and path[i]!=path[i-1] and path[i-1]!=path[i-2] and path[i]!=path[i-2]):
            if(self.already(path[i-1],path[:i-1])):
              x=self.find_cost(self.cost,path[i],path[i-1])
            else:  
              x=self.find_cost(cost,path[i-1],path[i])
            x+=self.find_cost(cost,path[i-2],path[i-3])
            self.change_cost(cost,path[i],path[i-1],x+2)
            print(path[i],self.find_cost(cost,path[i],path[i-1]))
            flag=1
          if(path[i] in self.and_adj[j] and path[i+1] in self.and_adj[j] and path[i-1] in self.and_adj[j] and path[i]!=path[i+1] and path[i+1]!=path[i-1] and path[i]!=path[i-1]):           
            print(path[i],self.find_cost(cost,path[i],path[i+1]))
            flag=1
            pass
      if(flag==0):
        if(i==1):
          x=self.find_cost(cost,path[i],path[i-1])
          self.change_cost(cost,path[i],path[i-1],x+1)
          print(path[i],self.find_cost(cost,path[i],path[i-1]))
          flag=0
        elif(i>1):
          x=self.find_cost(cost,path[i-1],path[i-2])
          self.change_cost(cost,path[i],path[i-1],x+1)
          print(path[i],self.find_cost(cost,path[i],path[i-1]))
          flag=0
        else:
          print(path[i],self.find_cost(cost,path[i],path[i+1]))
    return self.find_cost(cost,path[i],path[i-1])


  def ao_search(self):
    self.print_all_paths()

    print()
    for i in range(len(self.path)): 
      print("Path:",self.path[i])
      print("Cost:",self.path_cost(self.path[i]))
      print()
  
c=aomaze()
path=[]
c.ao_search()
