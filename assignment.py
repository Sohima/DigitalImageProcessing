#Huffman Coding
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (charecter)
        self.symbol = symbol
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.huff = ''
 
# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
 
 
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
 
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
 
#taking input
# charecters for huffman tree
chars = list(map(str,input("enter the number of characters:").rstrip().split()))

# frequency of charecters
freq = list(map(int, input("enter the frequency of each character you entered:").rstrip().split()))
# list containing unused nodes
nodes = []
 
# converting ccharecters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))
 
while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
 
    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
 
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
 
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
 
# Huffman Tree is ready!
printNodes(nodes[0])

# Python code for run length encoding
from collections import OrderedDict
def runLengthEncoding(string):
    count = 0
    chatacter = ''
    previous_char = string[0]
    result = ''
    length = len(string) 
    
    i = 0
    while (i != length ):
        chatacter = string[i]
        
        if previous_char == chatacter :
            count = count + 1
        else :
            result = result + str(count) + previous_char
            count = 1
        #print(str(i) + str(chatacter) + str(previous_char) + "          " + str(result))
        previous_char = chatacter
        i = i + 1
        
    return result + str(count) + str(previous_char)

# taking input
string = str(input("enter the string:"))
print (runLengthEncoding(string))

#Develop KNN algo
from math import sqrt

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors
# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction   

# Test distance function
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
row0 = dataset[0]
for row in dataset:
	distance = euclidean_distance(row0, row)
	print(distance)