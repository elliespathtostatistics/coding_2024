#Definition for a binary tree node.
from typing import Optional, List
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def successor(self, root: TreeNode) -> int:
        root = root.right
        while root.left:
            root = root.left
        return root.val
                
    # One step left and then always right
    def predecessor(self, root: TreeNode) -> int:
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # The node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root

def my_func(param1: str) -> int:
    return len(param1)

def expr_lesson1():
    # left_expr = right_expr
    # right expr gets evaluated first
    # there's a resultant value for right expr
    # that value then gets assigned by reference to a_node (copy by reference)
    a_node = TreeNode(5) 
    # same process but a new instance of a treenode is created
    # this treenode contains its own separate val, left and right
    b_node = TreeNode(10) 
    # we are taking the reference at a_node and assigning that to c_node
    c_node = a_node 
    # we are taking the reference at b_node and assigning that to d_node
    d_node = b_node
    # first, right expr gets evaluated, which is simply 3
    # we are updating the member variable val that was found by dereferencing the location stored at c node
    # and that happens to be a TreeNode that was stored at the location, and we are upating the member 
    # variable to 3
    c_node.val = 3
    # a statement that consists of an expression
    # that expression is a function w one parameter
    # that expression has to be fully evaluated first before it is passed to the function 
    # the expression a_node.val is evaluated by dereferencing a_node which is a reference to a TreeNode object
    # what is stored at member variable val which is 3
    # c node got a copy of the reference that's stored at a node, therefore a node and c node refers to the same 
    # underlying object, when you end up dereferencing, they both have that change 

    # this will evaluate to 3
    print(a_node.val)

def copy_lesson1():
    # list or primitives i.e. ints, strings etc.
    a_list = [1, 2, 3, 4]
    # shallow copy makes a new list and copies each element according to the copy by ref or value principle
    # in this case this is copy by value because each element is a primitive although a new list is made
    shallow_a_list = a_list[:]
    # a copy of the reference is simply made, a_list and reference_alist as a result refer to the same 
    # underlying list
    reference_alist = a_list 
    # deep copy makes a new list and copies each element by value regardless of the copy ref or copy by val 
    # principle

    deep_a_list = copy.deepcopy(a_list)


    shallow_a_list[0] = 0
    reference_alist[0] = 10
    deep_a_list[0] = 100

    print(a_list)
    print(shallow_a_list)
    print(reference_alist)
    print(deep_a_list)


    b_list = [TreeNode(5), TreeNode(6), TreeNode(7)]

    shallow_b_list = b_list[:]

    deep_b_list = copy.deepcopy(b_list)

    reference_blist = b_list

    shallow_b_list[0].val = 8
    reference_blist[0].val = 80
    deep_b_list[0].val = 800

    print("blist", [item.val for item in b_list])
    print("shallow", [item.val for item in shallow_b_list])
    print("reference", [item.val for item in reference_blist])
    print("deep", [item.val for item in deep_b_list])

def copy_lesson2():
    a = [[5, 6], [1, 2], [3, 4]]
    b = list(a)
    b.sort(key=lambda x: x[0])
    print(a)
    print(b)

class Student:
    def __init__(self, grades, name):
        self.grades = grades
        self.name = name 

    def get_avg(self):
        if not self.grades:
            return None
        else:
            return sum(self.grades)/len(self.grades)

    def print_summary(self):
        print(self.name)
        print(self.get_avg())

def classes_lesson3():
    s1 = Student(name = 'Ellie', grades = [98, 67, 100, 100])
    s2 = Student(name = 'David', grades = [89, 98, 90, 120])
    s1.print_summary()
    s2.print_summary()
    print("type(s1)", type(s1))

def main():
    copy_lesson1()

    classes_lesson3()
    


if __name__ == '__main__':
    main()

'''
practice lists and dictionaries, for lists
access a list by index
    literal integer -> 0, 1, -2, -1
    using a variable -> insert a var in there l[val]
    accessing list of lists
        rows and cols
creating lists 
    create len 10 list
    list of lists with rows and cols
    rows, cols
    lists of objects
    zip

removing from lists
    by index
    or remove
adding to list 
    appending w list of int
    appending w list of lists
    extend vs. append
    combining two lists


dictionaries
    getting list of keys
    getting list of values
    ordering keys
    ordering values
    print out students avg grades alphabetically
    initializing complex types like a list (having a counter var associated w each key)
        - student grade student grade
    deleting a key
    adding a new key value pair
when to use a dict vs. list vs. heap vs. deque vs. tree

looping
    iterate from 0 to end of list
    iterate from end of list to 0
    while til you reach terminal condition
        what if you dont know terminal condition til you enter while loop
    -say you have list of int, keep track of most frequent int, stop once you reach 5 of any particular int, 
    report first number reach 5 occurances

class syntax
    constructor
    calling a method from within a class
    calling a method outside of a class in a main method
    callng another member method inside a class
    
'''


