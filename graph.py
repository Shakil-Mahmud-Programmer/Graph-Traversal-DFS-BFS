class Node:
    def __init__(self, data, dis):
        self.data = data
        self.dis = dis
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None


class graph:
    def DFS(self,start,li,disp):
        for i in [start.first, start.second, start.third, start.fourth]:
            if i != None:
                li.append(i)
        disp += start.dis
        print(f'Node: {start.data} distance from previous Node: {start.dis} Total traviling distance from root Node: {disp}')
        for j in reversed(li):
            li.pop()
            self.DFS(j,li,disp)
        return


    def BFS(self,start,li,disp):
        for i in [start.first, start.second, start.third, start.fourth]:
            if i != None:
                li.append(i)
        disp += start.dis
        print(f'Node: {start.data} distance from previous Node: {start.dis} Total traviling distance from root Node: {disp}')
        for j in li:
            li.remove(j)
            self.BFS(j,li,disp)
        return




#root node/level 0
Grpah = Node('X',0)

#level 1
Grpah.first = Node('A',5)
Grpah.second = Node('B',3)
Grpah.third = Node('C',1)
Grpah.fourth = Node('D',6)

#level 2
Grpah.first.first = Node('E',2)
Grpah.first.second = Node('F',1)
Grpah.first.third = Node('G',2)
Grpah.second.first = Node('H',10)
Grpah.third.first = Node('I',5)
Grpah.third.second = Node('J',2)
Grpah.fourth.first = Node('K',7)
Grpah.fourth.second = Node('L',3)

#level 3
Grpah.first.second.first = Node('M',4)
Grpah.first.second.second = Node('N',4)
Grpah.third.first.first = Node('O',5)


disp = 0
Agent = graph()
print('DFS')
Agent.DFS(Grpah,[],disp)
print('BFS')
Agent.BFS(Grpah,[],disp)






