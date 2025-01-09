# Binary-Tree
 given an array-based representation of a general tree, construct a tree from
 the input using the provided TreeNode class. You will write the function read
 tree() that will read
 the general tree from standard input and return the root of the tree as a TreeNode object.
 The first line of the input will provide n and d. n represents the length of the array-based representation
 and d represents the maximum number of children a node can have. Not all nodes will have d children
 and so the dash character- represents an empty child.
 The second line of the input is a list of n space-separated strings that represents the tree as an array.
 Each string represents a page/node in the tree and the dash character (-) represents an empty child
 and should be ignored.
 You will be provided a TreeNode class in a separate file treenode.py. This file will be imported in
 your solution and its notable methods are:
 • a = TreeNode(’A’): Constructs a TreeNode with a value of ’A’ and store it in a variable a.
 • a.get
 • a.get
 • a.add
 value() returns the value of the node A.
 children() returns a list of TreeNode objects that are the children of the node a.
 child(child) adds a TreeNode object, child, to the list of a’s children.
 • a.print
 tree() prints the tree to standard output. Each line in the output will have the
 following format: NODE-> CHILDA CHILDB CHILDC ...
