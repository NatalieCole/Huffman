#Huffman COmpression algorithm coursework
#store hashmap and compressed file in a different file
print("Huffman Compression time...")
#get the user to input a text file of their choice:
print("Please enter the text file to compress: ")
textFile = input()
#read in a text file and make it a string:
fileStr = open(textFile, 'r').read()
len_fileStr = len(fileStr)
print("Your data is", len_fileStr * 7, "bits long") #calculate how many bits ar ein the original file

#create a lsit of characters and theiir frequencty and a list of the characters in use:
letters = [] #array
only_letters = [] #array
for letter in fileStr:
    if letter not in letters:
        freq = fileStr.count(letter) #calculate the frequency
        letters.append(freq) ##append the frequency
        letters.append(letter) #append the letter
        only_letters.append(letter) #append the letter

#generate base-level nodes for the huffman tree (that I will use to compresss the file) frequency and the letter:
nodes = []
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
#outputs letters with binary codes
print("Your binary codes are as follows:")
for letter in letter_binary:
    print (letter[0], letter[1])

#creates bitstring of the original message using the new codes you have generated for each letter:
#go through the string and create the compressed data
bitstring = ""
for character in fileStr:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]

binary = ((bin(int(bitstring, base=2)))) ##convert the string to a binary number


##here I need to open a file for the compressed data and enter it in:
f = open("CompressedFile.txt", "w") #clear the file incase there is anything in there from before
f = open("CompressedFile.txt", "a")
f.write(binary) #put the compressed binary version of the file in the compression file
f.close()

##summary of data compression:
original_file_size = len(fileStr)*7
compressed_file_size = len(binary)-2
percentage = (compressed_file_size/original_file_size) *100
print("Your original file-size was",original_file_size,"bits, The Compressed file is", compressed_file_size, "bits.")
print("This is a saving of ", original_file_size-compressed_file_size, "bits, with a compression percentage of", percentage,"%")

##decompress, using the letter_binary array (basically a dictionary of the letters and codes)
##convert the binary back to a string:
bitstring = str(binary[2:])
decompressed_string = ""
code = ""
for digit in bitstring:
    code = code+digit
    position = 0
    for letter in letter_binary:
        if code == letter[1]:
            decompressed_string = decompressed_string+letter_binary[position][0]
            code = ""
        position +=1

f = open("DecompressedFile.txt", "w") #clear the file incase there is anything in there from before
f = open("DecompressedFile.txt", "a")
f.write(decompressed_string) #write the compressed text into the decompressed file
f.close()

##Still to do:
#put it all into functions and procedurers like a proper programmer
