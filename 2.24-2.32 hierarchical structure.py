from orderedPair import *

def count_leave(items):
    if items == None: return 0
    elif not isinstance(items, tuple): return 1
    else: return count_leave(car(items))+count_leave(cdr(items))

def deep_reverse(item):
    if not isinstance(item, tuple): return item
    else: return cons(deep_reverse(cdr(item)), deep_reverse(car(item)))

def fringe(tree):
    if tree == None: return None
    elif not isinstance(tree, tuple): return lister(tree)
    else: return append(fringe(car(tree)), fringe(cdr(tree)))

def make_mobile(left, right):
    return lister(left, right)

def make_branch(length, structure):
    return lister(length, structure)

def left_branch(mobile):
    return car(mobile)

def right_branch(mobile):
    return car(cdr(mobile))

def branch_length(branch):
    return car(branch)

def branch_structure(branch):
    return car(cdr(branch))

def total_weight(mobile):
    if mobile == None: return 0
    elif not isinstance(mobile, tuple): return mobile
    else: return (total_weight(left_branch(mobile))
                  + total_weight(right_branch(mobile)))

def mobile_blance(mobile):
    if branch_length(left_branch(mobile))*total_weight(left_branch(mobile))\
       == branch_length(right_branch(mobile))*total_weight(right_branch(mobile)):
        return True
    else: return False

def square_tree(tree):
    if tree == None: pass
    elif not isinstance(tree, tuple): return tree**2
    else: return cons(square_tree(car(tree)), square_tree(cdr(tree)))

def square_tree_map(tree):
    return mapping(lambda x: x**2 if not isinstance(x, tuple)
                  else square_tree_map(x), tree)

def square_tree_mapper(tree):
    return mapper(lambda x: x**2, tree)

def subsets(s):
    # 递归思路:
    # 集合{a,b,c}的子集=集合{b,c}的子集+集合{b,c}的子集与集合{a}的并集
    # 集合{b,c}的子集=集合{c}的子集+集合{c}的子集与集合{b}的并集
    # 集合{c}的子集={}和{c}
    if s == None: return lister(None)
    else: return append(subsets(cdr(s)), mapping(lambda x: cons(car(s), x), subsets(cdr(s))))
    

if __name__ == '__main__':
    x = cons(lister(1, 2),lister(3, 4))
    display(x)
    print(x, length(x), count_leave(x), '\n')

    y = lister(lister(1, 2),lister(3, 4))
    display(y)
    print(y, length(y), count_leave(y), '\n')

    z = lister(cons(1, 2), cons(3, 4), 5, 6)
    display(z)
    print(z, length(z), count_leave(z), '\n')

    p = lister(1,lister(2,lister(3,4)))
    display(p)
    print(p, length(p), count_leave(p), '\n')

    list1 = lister(1, 2, 3)
    list2 = lister(4, 5, 6)
    list3 = lister(7, 8, 9)
    listtest = lister(list1, list2, list3)
    display(listtest)
    print(deep_reverse(listtest), '\n')
    print(fringe(listtest), '\n')

    mobile = make_mobile(make_branch(10, 10), make_branch(10,20))
    display(left_branch(mobile))
    display(right_branch(mobile))
    print(branch_length(right_branch(mobile)), branch_structure(right_branch(mobile)))
    print(total_weight(mobile))
    print('moile blance:', mobile_blance(mobile), '\n')

    tree = lister(1, lister(2, lister(3, 4), 5), lister(6, 7))
    display(mapping(lambda x: x**2, list1))
    display(tree)
    display(square_tree(tree))
    display(square_tree_map(tree))
    display(square_tree_mapper(tree))
    print(subsets(list1))
