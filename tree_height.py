import sys
import threading


class Node:
    def __init__(self):
        self.children = []


def compute_height(num, parents):
    nodes = [Node() for _ in range(num)]
    root_index = 0

    for child_index in range(num):
        parent_index = parents[child_index]

        if parent_index != -1:
            nodes[parent_index].children.append(nodes[child_index])
        else:
            root_index = child_index

    return get_height(nodes[root_index])


def get_height(node):
    if not node.children:
        return 1
    else:
        return 1 + max([get_height(child) for child in node.children])


def main():
    input_str = input()

    if "a" in input_str:
        print()
        return

    if "I" in input_str:
        num = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(num, parents))

    if "F" in input_str:
        filename = input()
        if "a" in filename:
          
            return
        path = "test/" + filename
        with open(path, 'r') as file:
            num = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(compute_height(num, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
