class Node:
    """The Node class is a container for the suffix tree structure. Each node stores 
    its outgoing edges, whether it is a leaf, and a unique ID (generated automatically using _id_counter)."""
    _id_counter = 0 # It starts at 0 and incremented when we move to a new node. It gives a UNIQUE ID to each node
    def __init__(self):
        self.children = {}   # The children is a tuple with a label (substring of the edge) and a node (the outgoing node). To keep track of connections
        self.is_leaf = False # To mark if the node is the end of an edge or not
        self.id = Node._id_counter # This is to assign a UNIQUE ID to each node
        Node._id_counter += 1 # We increment the id_counter for the next node


def insert_suffix(root, suffix):
    """Insert one suffix into the tree (with edge compression)."""
    node = root # The root is an empty node created previously
    i = 0
    while i < len(suffix): # We loop until we have placed all the letters in the suffix
        current_pos = suffix[i] # The current position of the suffix
        
        """CASE A: there is already an edge starting with this character."""
        if current_pos in node.children:
            label, child = node.children[current_pos] # label = the substring on that edge, child = the node ending the edge
            j = 0
            while j < len(label) and i+j < len(suffix) and label[j] == suffix[i+j]: # Compare the suffix against the edge label
                j += 1 # To move to the next character
                
            """CASE A1: If we matched the entire edge label"""
            if j == len(label): # We move to the child node and insert the rest of the suffix
                node = child
                i += j 
            else: ### CASE A2: partial match
                existing_label = label[j:] # The unmatched tail of the label
                new_label = suffix[i+j:] # The unmatched tail of the suffix
                split_node = Node()
                
                # We split the edge in 2, the existing label
                split_node.children[existing_label[0]] = (existing_label, child)
                # The leftover part of the new suffix
                new_child = Node()
                new_child.is_leaf = True # We end with this new suffix so change is_leaf to true
                split_node.children[new_label[0]] = (new_label, new_child) # New label and new leaf
                # Update current node
                node.children[current_pos] = (label[:j], split_node)
                return
        else:
            # Create new edge
            new_child = Node()
            new_child.is_leaf = True
            node.children[current_pos] = (suffix[i:], new_child)
            return


def build_suffix_tree(s):
    """Naive O(n^2) suffix tree construction."""
    Node._id_counter = 0  # reset IDs
    root = Node()
    s += "$"
    for i in range(len(s)):
        insert_suffix(root, s[i:])
    return root

def print_tree(node, indent=0):
    """Print suffix tree as text with indentation."""
    for label, child in node.children.values():
        print(" " * indent + label)
        print_tree(child, indent + 4)

# Example
s = "TATAT"
tree = build_suffix_tree(s)
print("Suffix tree for", s + "$")
print_tree(tree)

s = "mississippi"
tree = build_suffix_tree(s)
print("Suffix tree for", s + "$")
print_tree(tree)