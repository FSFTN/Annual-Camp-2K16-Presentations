def add(*args):
    t = 0
    for n in args:
       t += n
    return t


def concat(**kwargs):
    r = []
    for k,v in kwargs.items():
       r.append(k + ": " + v)

    return r




class Tree(object):
   total_trees = 0
   def __init__(s, branches = 0):
     s.branches = branches   # creates an instance variable


   def grow(s, how_many = 1):
     s.branches += how_many

   def __str__(s):
     return "I have " + str(s.branches) + " number of branches"


tree = Tree()
print(tree)

tree.grow()
print(tree)

tree1 = Tree(10)
print(tree1)

tree1.grow()
print(tree1)

tree1.grow(10)
print(tree1)

print("Total number of trees: ", Tree.total_trees)

print(add(1,2,3,4,5))


print(concat(arg1 = "one", arg2 = 2, arg3 = "so long"))
