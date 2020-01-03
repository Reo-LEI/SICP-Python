from orderedPair import *
from symbolic import *


def make_leaf(sy, weight):
    return lister('leaf', sy, weight)


def is_leaf(obj):
    return eq(car(obj), 'leaf')


def symbol_leaf(x):
    return car(cdr(x))


def weight_leaf(x):
    return car(cdr(cdr(x)))


def make_code_tree(left, right):
    return lister(left,
                  right,
                  append(symbols(left), symbols(right)),
                  weight(left) + weight(right))


def left_branch(tree):
    return car(tree)


def right_branch(tree):
    return car(cdr(tree))


def symbols(tree):
    if is_leaf(tree):
        return lister(symbol_leaf(tree))
    else:
        return car(cdr(cdr(tree)))


def weight(tree):
    if is_leaf(tree):
        return weight_leaf(tree)
    else:
        return car(cdr(cdr(cdr(tree))))


def decode(bits, tree):
    def _decode(bit, current_branch):
        if bit is None:
            return None
        else:
            next_branch = choose_branch(car(bit), current_branch)
            if is_leaf(next_branch):
                return cons(symbol_leaf(next_branch),
                            _decode(cdr(bit), tree))
            else:
                return _decode(cdr(bit), next_branch)

    def choose_branch(bit, branch):
        if bit == 0:
            return left_branch(branch)
        elif bit == 1:
            return right_branch(branch)
        else:
            return print('error: bad bit -- CHOOSE-BRANCH')
    return _decode(bits, tree)


def adjoin_set(x, set):
    if set is None:
        return lister(x)
    elif weight(x) < weight(car(set)):
        return cons(x, set)
    else:
        return cons(car(set), adjoin_set(x, cdr(set)))


def make_leaf_set(pairs):
    if pairs is None:
        return None
    else:
        pair = car(pairs)
        return adjoin_set(make_leaf(car(pair), car(cdr(pair))),
                          make_leaf_set(cdr(pairs)))

# 2.67
sample_tree = make_code_tree(make_leaf('A', 4),
                             make_code_tree(make_leaf('B', 2),
                                            make_code_tree(make_leaf('D', 1),
                                                           make_leaf('C', 1))))
sample_message = lister(0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0)


# 2.68
def encode(msg, tree):
    if msg is None:
        return None
    else:
        return append(encode_symbol(car(msg), tree),
                      encode(cdr(msg), tree))


def encode_symbol(msg, tree):
    if is_leaf(tree):
        return None
    elif memq(msg, symbols(left_branch(tree))):
        return cons(0, encode_symbol(msg, left_branch(tree)))
    elif memq(msg, symbols(right_branch(tree))):
        return cons(1, encode_symbol(msg, right_branch(tree)))
    else:
        return print('error, message is not exist')


# 2.69
def generate_huffman_tree(pairs):
    return successive_merge(make_leaf_set(pairs))


def successive_merge(set):
    if set is None:
        return None
    elif cdr(set) is None:
        return car(set)
    else:
        left = car(set)
        right = car(cdr(set))
        rest = cdr(cdr(set))
        tree = make_code_tree(left, right)
        return successive_merge(adjoin_set(tree, rest))

if __name__ == '__main__':
    message = decode(sample_message, sample_tree)
    pairs = lister(lister('A', 8), lister('B', 3), lister('C', 1),
                   lister('D', 1), lister('E', 1), lister('F', 1),
                   lister('G', 1), lister('H', 1),)
    # 2.68
    display(message)
    display(encode(message, sample_tree))
    display(make_leaf_set(pairs))

    # 2.69
    display(generate_huffman_tree(pairs))

    # 2.70
    alphabet = lister(lister('A', 2), lister('NA', 16), lister('BOOM', 1),
                      lister('SHA', 3), lister('GET', 2), lister('YIP', 9),
                      lister('JOB', 2), lister('WAH', 1))
    msg1 = lister('GET', 'A', 'JOB')
    msg2 = lister('SHA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA')
    msg3 = lister('WAH', 'YIP', 'YIP', 'YIP', 'YIP',
                  'YIP', 'YIP', 'YIP', 'YIP', 'YIP')
    msg4 = lister('SHA', 'BOOM')
    tree = generate_huffman_tree(alphabet)
    display(encode(msg1, tree))
    display(encode(msg2, tree))
    display(encode(msg1, tree))
    display(encode(msg2, tree))
    display(encode(msg3, tree))
    display(encode(msg4, tree))

    # 2.71
    n5 = lister(lister('A', 1), lister('B', 2), lister('C', 4),
                lister('D', 8), lister('E', 16), lister('F', 32))

    n10 = lister(lister('A', 1), lister('B', 2), lister('C', 4),
                 lister('D', 8), lister('E', 16), lister('F', 32),
                 lister('G', 64), lister('H', 128), lister('I', 256),
                 lister('J', 512), lister('K', 1024), lister('L', 2048))
    tree5 = generate_huffman_tree(n5)
    tree10 = generate_huffman_tree(n10)
    display(encode(lister('F'), tree5))
    display(encode(lister('A'), tree5))
    display(encode(lister('L'), tree10))
    display(encode(lister('A'), tree10))


