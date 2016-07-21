from orderedPair import *
from symbolic import *
import sys


sys.setrecursionlimit(100000)


# set
def element_of_set(x, set):
    if set is None:
        return False
    elif eql(x, car(set)):
        return True
    else:
        return element_of_set(x, cdr(set))


def adjoin_set(x, set):
    if element_of_set(x, set):
        return set
    else:
        return cons(x, set)


def intersection_set(set1, set2):
    if set1 is None or set2 is None:
        return None
    elif element_of_set(car(set1), set2):
        return cons(car(set1), intersection_set(cdr(set1), set2))
    else:
        return intersection_set(cdr(set1), set2)


# 2.59
def union_set(set1, set2):
    if set1 is None:
        return set2
    elif set2 is None:
        return set1
    elif not element_of_set(car(set1), set2):
        return cons(car(set1), union_set(cdr(set1), set2))
    else:
        return union_set(cdr(set1), set2)


# 2.60
# element_of_set, intersection_set, union_set不变
def _adjoin__set(x, set):
    return cons(x, set)


def _union_set(set1, set2):
    return cons(set1, set2)


# 2.61
def element_of_set_order(x, set):
    if set is None:
        return False
    elif x == car(set):
        return True
    elif x < car(set):
        return False
    else:
        return element_of_set_order(x, cdr(set))


def adjoin_set_order(x, set):
    if set is None:
        return lister(x)
    elif x < car(set):
        return cons(x, set)
    elif x == car(set):
        return set
    else:
        return cons(car(set), adjoin_set_order(x, cdr(set)))


def intersection_set_order(set1, set2):
    if set1 is None or set2 is None:
        return None
    else:
        x = car(set1)
        y = car(set2)
        if x == y:
            return cons(x, intersection_set_order(cdr(set1), cdr(set2)))
        elif x < y:
            return intersection_set_order(cdr(set1), set2)
        elif x > y:
            return intersection_set_order(set1, cdr(set2))


def union_set_order(s1, s2):
    if s1 is None and s2 is None:
        return lister(None)
    elif s1 is None:
        return s2
    elif s2 is None:
        return s1
    else:
        x = car(s1)
        y = car(s2)
        if x == y:
            return cons(x, union_set_order(cdr(s1), cdr(s2)))
        elif x < y:
            return cons(x, union_set_order(cdr(s1), s2))
        elif x > y:
            return cons(y, union_set_order(s1, cdr(s2)))


# tree
def make_tree(entry, left, right):
    return lister(entry, left, right)


def entry(tree):
    return car(tree)


def left_branch(tree):
    return car(cdr(tree))


def right_branch(tree):
    return car(cdr(cdr(tree)))


def element_of_tree(x, tree):
    if x == entry(tree):
        return True
    elif x < entry(tree):
        return element_of_tree(x, left_branch(tree))
    elif x > entry(tree):
        return element_of_tree(x, right_branch(tree))


def adjoin_tree(x, tree):
    if tree is None:
        return make_tree(x, None, None)
    elif x == entry(tree):
        return tree
    elif x < entry(tree):
        return make_tree(entry(tree),
                         adjoin_tree(x, left_branch(tree)),
                         right_branch(tree))
    elif x > entry(tree):
        return make_tree(entry(tree),
                         left_branch(tree),
                         adjoin_tree(x, right_branch(tree)))


# 2.63
def tree_to_list1(tree):
    if tree is None:
        return None
    else:
        return append(tree_to_list1(left_branch(tree)),
                      cons(entry(tree),
                           tree_to_list1(right_branch(tree))))


def tree_to_list2(tree, result=None):
    if tree is None:
        return result
    else:
        return tree_to_list2(left_branch(tree),
                             cons(entry(tree),
                                  tree_to_list2(right_branch(tree),
                                                result)))


#2.64
def list_to_tree(elements):
    return car(partial_tree(elements, length(elements)))


def partial_tree(elts, n):
    # display(elts)
    # print(n)
    if not n:
        return cons(None, elts)
    else:
        left_size = (n-1)//2
        left_result = partial_tree(elts, left_size)
        left_tree = car(left_result)
        non_left_elts = cdr(left_result)
        right_size = n - (left_size+1)
        this_entry = car(non_left_elts)
        right_result = partial_tree(cdr(non_left_elts), right_size)
        right_tree = car(right_result)
        remaining_elts = cdr(right_result)
        return cons(make_tree(this_entry, left_tree, right_tree),
                    remaining_elts)


# 2.65
def union_set_tree(tree1, tree2):
    return list_to_tree(
        union_set_order(tree_to_list2(tree1),
                        tree_to_list2(tree2)))


def intersection_tree(tree1, tree2):
    return list_to_tree(
        intersection_set_order(tree_to_list2(tree1),
                               tree_to_list2(tree2)))


# 2.66
def lookup(key, tree):
    if tree is None:
        return False
    elif key == entry(tree):
        return key
    elif key < entry(tree):
        return element_of_tree(key, left_branch(tree))
    elif key > entry(tree):
        return element_of_tree(key, right_branch(tree))


if __name__ == '__main__':
    s1 = lister(1, 2, 3, 4, 5)
    s2 = lister(3, 4, 5, 6, 7)
    s3 = lister(5, 6, 7, 8, 9)
    ss = lister(1, 2, 3, 1, 4, 2, 4, 9, 7, 5, 3, 3, 2, 2, 4, 6)

    display(element_of_set(4, s1))
    display(adjoin_set(1, s2))
    display(intersection_set(s1, s2))
    display(union_set(s1, s2))

    display(element_of_set_order(4, s1))
    display(adjoin_set_order(1, s2))
    display(intersection_set_order(s1, s2))
    display(union_set_order(s1, s2))

    tree1 = make_tree(7,
                      make_tree(3,
                                make_tree(1, None, None),
                                make_tree(5, None, None)),
                      make_tree(9,
                                None,
                                make_tree(11, None, None)))
    tree2 = make_tree(3,
                      make_tree(1, None, None),
                      make_tree(7,
                                make_tree(5, None, None),
                                make_tree(9,
                                          None,
                                          make_tree(11, None, None))))
    tree3 = make_tree(5,
                      make_tree(3,
                                make_tree(1, None, None),
                                None),
                      make_tree(9,
                                make_tree(7, None, None),
                                make_tree(11, None, None)))

    display(tree_to_list1(tree1))
    display(tree_to_list1(tree2))
    display(tree_to_list1(tree3))
    display(tree_to_list2(tree1))
    display(tree_to_list2(tree2))
    display(tree_to_list2(tree3))
    display(list_to_tree(lister(1, 3, 5, 7, 9, 11)))

