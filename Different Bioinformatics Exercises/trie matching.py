class Node:
    def __init__(self):
        self.mark = False
        self.edges = [None] * 26

def trie_insert(node, string, index = 0):
    if index == len(string):
        node.mark = True
        return
    dist = ord(string[index])-ord('A')
    if node.edges[dist] is None:
        node.edges[dist] = Node()
    trie_insert(node.edges[dist], string, index+1)

def trie_search(node, string, index = 0):
    if index == len(string):
        return True
    dist = ord(string[index])-ord('A')
    if node.edges[dist] is None:
        return False
    return trie_search(node.edges[dist], string, index+1)

root = Node()
array= input()
i = input()
n = len(i)
while i!="*":
    trie_insert(root,i)
    i = input()
for i in range(len(array)-n+1):
    if trie_search(root , array[i:i+n]):
        print(i)