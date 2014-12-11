import SelectScript
import SelectScript.Interpreter

#     S     Memo        Cyc
#2    3     0m0.156s
#3    7     0m0.287s
#4    15    0m1.552s
#5    31    0m12.968s
#6    63    1m33.191s    1m39.084s
#7    127    

def move(step, towers):
    if towers == [] or towers[step[0]] == []:
        pass
    elif towers[step[1]] == []:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    elif towers[step[1]][-1] > towers[step[0]][-1]:
        towers[step[1]].append( towers[step[0]].pop() )
        return towers
    return []
  
problem = """
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[4,3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[4,3,2,1],[],[]], level=1
CONNECT BY NO CYCLE tower = move( mov.this, tower ), level=level+1
STOP WITH  ([] == move( mov.this, tower )) or level==15
              
AS list; """

problem = """
moves  = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]];
              
SELECT mov.this, tower
FROM mov=moves
WHERE [[],[],[8,7,6,5,4,3,2,1]] == move( mov.this, tower )
              
START WITH tower = [[8,7,6,5,4,3,2,1],[],[]]
CONNECT BY MEMORIZE 255 tower = move( mov.this, tower )
STOP WITH  [] == move( mov.this, tower )
              
AS list; """

bytecode = SelectScript.compile(problem, debug=True)

ss = SelectScript.Interpreter()
ss.addFunction('move', move)
ss.addFunction('str', str)

tree = ss.eval(bytecode)

def search(graph, max_iter, start=None, end=None):
    result = []
    
    if start == None:
        start_nodes = []
        end_nodes   = []

        for key in graph.keys():
            if None in graph[key][2]:
                start_nodes.append(key)
            if graph[key][0]:
                end_nodes.append(key)
                
        for s in start_nodes:
            for e in end_nodes:
                result += search(graph, max_iter, [s], [e])
                
        if result != []:
            result_sub = []
            for hashIDs in result:
                sub = []
                for key in hashIDs:
                    sub.append(graph[key][1])
                result_sub.append(sub)
            return result_sub
                
    elif start[-1] == end[0]:
        result.append(start + end[1:])
        #print "found1"
    
    elif len(start) + len(end) > max_iter:
        pass
    elif graph[start[-1]][3] > graph[end[0]][3]:
        #print "fuck", graph[start[-1]], graph[end[0]]
        pass
    
    else:
        for e in graph[end[0]][2]:
            if e == None:
                continue
            
            if graph[end[0]][3] < graph[e][3]:
                #print "DDD"
                continue
            
            if e == start[-1]:
                result.append(start + [e] + end)
                #print "found2"
                
            elif not e in end:
                for s in graph.keys():
                    if (start[-1] in graph[s][2]) and not (s in start):
                        if graph[start[-1]][3] < graph[s][3]:
                            #print "ddd"
                            result += search(graph, max_iter, start+[s], [e]+end)                       
    return result

#print "Tree", tree
#rr = search(tree, 127)


#print rr
#rr = reconstructResults4(tree, 16)
#print rr
#rr = reconstructResults(tree)
#print tree

#print tree

for i, e in enumerate(tree):
    print i, len(e)
    print e
    print