while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)
#recursivly combines base nodes to create the huffman tree and allocates either a 0 or 1 to each
#pair of nodes prior to combinging which will be later used to createa ninary code for each letter
#this recursive function combine nodes together and create a tree which I can then assign binary pathways to
#orders the nodes in order of size and then it combines them togeteher in a series of binary pathways
#it also allocates a string of 0 r 1 depending it the node is on the left or the right
#produces a unique set of binary codes for each later
#frequent letters require the least number of bits to encode
def combine(nodes):
    position = 0
    newnode = []
    #get the two nodes with the lowest frewquency:
    if len(nodes)>1:
        nodes.sort()
        #adds in the 0,1 depending on whether it's the left or right node:
        nodes[position].append("0")
        nodes[position+1].append("1")
        #this orders the nodes in order of size
        combined_node1 = (nodes[position][0]+nodes[position+1][0])
        combined_node2 = (nodes[position][1]+nodes[position+1][1])
        #then it combines the njodes together
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree
newnodes = combine(nodes)
#tree needs to be inverted
huffman_tree.sort(reverse=True)
print("Here is the Huffman Tree, showing the merged nodes and binary pathways.")
#remove duplicate items in the huffman tree
#and create an array with just the nodes and their frequencyNode#this block is just for visualising and printing the huffman tree, take out at the end:
checklist = [] #array
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)
count = 0
for level in huffman_tree:
    print("Level",count, ":", level)
    count +=1
print()
##builds the binary codes for each character ibn the file
#checks to see what the codes are:
letter_binary= [] #array
if len(only_letters)==1:
    letter_code = [only_letters[0],"0"]
    letter_binary.append(letter_code*len(fileStr))
else:
    for letter in only_letters:
        lettercode = ""
        for node in checklist:
            if len(node)>2 and letter in node[1]:
                lettercode = lettercode + node[2]
        letter_code = [letter,lettercode]
        letter_binary.append(letter_code)
