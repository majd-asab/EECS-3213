import random;


# return index of next shortest path 
# in other words, next cheapest node.
# @ param node: the node we are at.
def nextShortestPath(node,lastNode):
	# @param A: Matrix size
	# @param o: Source node
	# @param d: destination node
	matrix = {
		1:[0,1,0,0,0,0],
		2:[1,0,3,2,0,8],
		3:[0,3,0,0,4,0],
		4:[0,2,0,0,2,0],
		5:[0,0,4,2,0,1],
		6:[0,0,0,0,1,0],
	}

	# # find array corresponding to "o"
	# if(not (o in matrix)) or  (not (d in matrix)):
	# 	print "ERROR: source or destination node doesn't exist."
	# 	return -1;

	paths = matrix[node];

	# find index of lowest value thats not a Zero in "o"
	lowestValue = 0;
	indexOfLowestValue =0
	for i in range(0,len(paths)):
		if((lowestValue == 0) and (paths[i] > 0) and (not((i+1) == lastNode))):
			lowestValue = paths[i];
			indexOfLowestValue = i+1;
		elif(paths[i] > 0 and (lowestValue > paths[i]) and (not((i+1) == lastNode))):
			lowestValue = paths[i];
			indexOfLowestValue = i+1;
	nextNodeAndCost ={"nextNode":indexOfLowestValue, "cost":lowestValue};
	return nextNodeAndCost;

def DijkstraAlgorithm(A,o,d):
	sourceNode = o;
	lastNode   = o;
	nextNode   = [o];
	cost       = 0;
	i = 5;
	while(not (nextNode[len(nextNode)-1] == d)):
		# find next shortest path and cost
		data = nextShortestPath(nextNode[len(nextNode)-1],lastNode);
		nextNode.append(data["nextNode"]);
		cost  	  += data["cost"];
		# set last node to current node
		lastNode = nextNode[len(nextNode)-2];
		# print nextNode, cost;
		# i -=1;
	print "path: ",nextNode;
	print "cost: ",cost


DijkstraAlgorithm(6,1,6);
