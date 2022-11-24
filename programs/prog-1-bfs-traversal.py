from queue import Queue

def initializeValues(visited,level,parent,queue):
	for node in adjList.keys():
		visited[node] = False
		parent[node] = None
		level[node] = -1
	s="A"
	visited[s] = True
	level[s] = 0
	queue.put(s)

def bfsTraversal(adjList,parent,level,queue,bfsTraversalOutput):
	while not queue.empty():
		u = queue.get()
		bfsTraversalOutput.append(u)
		for v in adjList[u]:
			if not visited[v]:
				visited[v] = True
				parent[v] = u
				level[v] = level[u] + 1
				queue.put(v)

def printValues(bfsTraversalOutput):
	print("Output : ",end="")
	for node in bfsTraversalOutput:
		print(node,end=" ")
	print()

if __name__ == '__main__':
	adjList = {
		"A" : ["B","D"],
		"B" : ["C","A"],
		"C" : ["B"],
		"D" : ["A","E","F"],
		"E" : ["D","F","G"],
		"F" : ["D","E","H"],
		"G" : ["E","H"],
		"H" : ["G","F"]
	}
	visited = {}
	level = {}
	parent = {}
	bfsTraversalOutput=[]

	queue = Queue()
	initializeValues(visited,level,parent,queue)
	bfsTraversal(adjList,parent,level,queue,bfsTraversalOutput)
	printValues(bfsTraversalOutput)
