from collections import deque

graph = {}

graph["start"] = ["edgeL1", "edgeR1"]

graph["edgeL1"] = ["edgeC", "finish"]

graph["edgeR1"] = ["edgeC", "EdgeF1"]

graph["edgeC"] = []

graph["edgeF1"] = ["finish"]


def shortestWay(way):
    return way == 'finish'

def width_search(way):
    search_row = deque()
    search_row += graph[way]
    verified = []
    path = ''
    count = 0

    while search_row:
        chosenWay = search_row.popleft()
       
        if not chosenWay in verified:
            
            if(shortestWay(chosenWay)):
                print('The shortest path to the finish is', count )
                print('PATH:', path, 'FINISH')
                return True
            else:
                search_row += graph[chosenWay]
                verified.append(chosenWay)
                path += chosenWay + ' -> '
                count += 1
    return False

width_search("start")
