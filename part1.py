"""Prompt       Graph Theory Data Structures

In class we created an adjacency list and adjacency matrix function which takes any number tuple edge_pairs and returns either an adjacency list (dictionary where the values are lists) or an adjacency matrix (implemented as a list of lists)

In class when given an edge_pair like (1,4) we assumed that the pairing is that 1 -> 4 (ie node 1 has a directed edge to node 4). For this assignment, you're going to do the following:

Part 1:

Create two functions, one which will convert any number of tuple edge_pairs into an adjacency list and one which will convert them to an adjacency matrix.

The difference is that now, the functions will check for an input from the user which will indicate the direction of an edge tuple. It will take in a key value pair which will be named "direction" and expected inputs are:
    '->' for left to right 
    '<-' for right to left 
    '<>' for both directions

So your functions should be able to check for and do all of these. You can either use if elif else logic for this and input separate logic for each case or use helper functions or possibly a slightly more clever approach...

Once you've created these functions, you're going to do the following:

-----------<BONUS

Bonus point opportunity, create an additional matrix function using a numpy array. Please note that a numpy array is not mutable, so it isn't recommended that you use it in the class functions below.

>-----------
"""

"""
Resources used:
Professor code and class video as a reference
https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
https://www.geeksforgeeks.org/comparison-between-adjacency-list-and-adjacency-matrix-representation-of-graph/
"""


from pprint import pprint
import numpy as np

"""
returns a dictionary where key represent nodes and values representing nodes which node in key is connected to.
 @param *pairs - gets pairs of arguments which are all digits. All of them gets collected into pairs. 
 @return {dict} which represent graph relationship 
"""
def adjacency_list(*pairs):
    valid_direction = ['->', '<-', '<>']
    adjacency_list = dict()
    for pair in pairs:
        direction = input(f'Please enter direction for this pair {pair}: ')
        while direction not in valid_direction:
            direction = input('Incorrect direction. Can you try once again: ')
        if direction == '->':
            node = pair[0]
            if node in adjacency_list:
                adjacency_list[node].append(pair[1])
            else:
                adjacency_list[node] = [pair[1]]
        if direction == '<-':
            node = pair[1]
            if node in adjacency_list:
                adjacency_list[node].append(pair[0])
            else:
                adjacency_list[node] = [pair[0]]
        if direction == '<>':
            node = pair[0]
            if node in adjacency_list:
                adjacency_list[node].append(pair[1])
            else:
                adjacency_list[node] = [pair[1]]
            node = pair[1]
            if node in adjacency_list:
                adjacency_list[node].append(pair[0])
            else:
                adjacency_list[node] = [pair[0]]
    #count = len(pairs)
    return adjacency_list

"""
gets number of nodes present in graph
 @param *args - gets pairs of digits. All of them gets collected into args. 
 @return all unique node and total length of nodes in graph
"""
def count_nodes(*args):
    set_of_nodes = set()
    for edge_pair in args:
        #for both directions
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1]) 
    return set_of_nodes, len(set_of_nodes)

"""
  n*n, where n is # of vertices / nodes in graph
 Formula:
 A[i][j] = 1 iff i and j are adjacent
 A[i][j] = 0  otherwise

makes adjacency matrix from inputs
 @param *args - gets pairs of digits. All of them gets collected into args. 
 @return adjacency matrix (2d array) representation of graph from inputs using above formula.
"""
def adjacency_matrix(*args):
    count = count_nodes(*args)[1]
    adjacency_matrix = []
    list_to_append = []
    valid_direction = ['->', '<-', '<>']
    for row in range(count+1):
        list_to_append.append(0)
    for column in range(count+1): # 0 to that value
        adjacency_matrix.append(list_to_append[:]) #completely new deep copy and get new reference for each
    for pair in args:
        direction = input(f'Please enter direction for this pair {pair}: ')
        while direction not in valid_direction:
            direction = input('Incorrect direction. Can you try once again: ')
        if direction == "->":
            adjacency_matrix[pair[0]][pair[1]] = 1
        if direction == "<-":
            adjacency_matrix[pair[1]][pair[0]] = 1
        if direction == "<>":
            adjacency_matrix[pair[0]][pair[1]] = 1
            adjacency_matrix[pair[1]][pair[0]] = 1
    #pprint(adjacency_matrix)

    return adjacency_matrix

"""
Bonus: Numpy implementation

 n*n, where n is # of vertices / nodes in graph
 Formula:
 A[i][j] = 1 iff i and j are adjacent
 A[i][j] = 0  otherwise

makes adjacency matrix from inputs
 @param *args - gets pairs of digits. All of them gets collected into args. 
 @return adjacency matrix (2d array) representation of graph from inputs using above formula.
"""
def numpy_matrix(*args):
    count = count_nodes(*args)[1]
    #print(count)
    adjacency_matrix = np.zeros(shape = (count+1, count+1), dtype= int)
    valid_direction = ['->', '<-', '<>']
    for pair in args:
        direction = input(f'Please enter direction for this pair {pair}: ')
        while direction not in valid_direction:
            direction = input('Incorrect direction. Can you try once again: ')
        if direction == "->":
            adjacency_matrix[pair[0]][pair[1]] = 1
        if direction == "<-":
            adjacency_matrix[pair[1]][pair[0]] = 1
        if direction == "<>":
            adjacency_matrix[pair[0]][pair[1]] = 1
            adjacency_matrix[pair[1]][pair[0]] = 1
    #pprint(adjacency_matrix)
    return adjacency_matrix


if __name__ == "__main__":
    # expected:
    # for -> : {1: [2, 3], 2: [3, 4], 3: [4, 6], 4: [1, 5], 5: [2, 4]}
    # for <- : {1: [4], 2: [1, 5], 3: [1, 2], 4: [2, 3, 5], 5: [4], 6: [3]}
    # for <> : 
            # {1: [2, 3, 4],
            #  2: [1, 3, 4, 5],
            #  3: [1, 2, 4, 6],
            #  4: [2, 3, 1, 5, 5],
            #  5: [4, 2, 4],
            #  6: [3]}

    #pprint(adjacency_list((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)))
    """
        (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)
    Expected:    
    <>
    [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]]
        ->
    [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
    <-
    [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]]
    """
    pprint(adjacency_matrix((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)))
    #pprint(numpy_matrix((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)))