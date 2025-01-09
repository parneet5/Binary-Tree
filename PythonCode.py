from treenode import TreeNode

def read_tree():
    """Construct a tree from standard input.

    The first line of standard input will have the format: n d
        - n: The length of the array-based representation of the tree
        - d: The maximum number of children a node can have.

    The second line contains n space-separated strings where each string
    represents the value of a TreeNode. A string can be a single character
    (eg. 'W') or a series of characters (eg. 'AA', 'AB'). The dash '-' character
    represents an empty node and should be ignored.

    Returns:
        The root of the tree as a TreeNode object.
    """
    import sys
    input = sys.stdin.read().splitlines()

    n, d = map(int, input[0].split())
    tree_values = input[1].split()

    tree_nodes = [TreeNode(value) if value != '-' else None for value in tree_values]

    tree_root = tree_nodes[0]

    current_index = 0  #
    for i in range(1, n):
        if tree_nodes[i] is None:
            continue  

        while current_index < n and (
            tree_nodes[current_index] is None or
            len(tree_nodes[current_index].get_children()) >= d
        ):
            current_index += 1

        if current_index < n:
            tree_nodes[current_index].add_child(tree_nodes[i])

    return tree_root

def main():
    # Do not modify
    read_tree().print_tree()

if __name__ == "__main__":
    main()

