from orderedpair import *

def enumerate_interval(low, high):
    if low > high: return None
    else: return cons(low, enumerate_interval(low+1, high))

def enumerate_tree(tree):
    if tree == None: return None
    elif not isinstance(tree, tuple): return lister(tree)
    else: return append(enumerate_tree(car(tree)), enumerate_tree(cdr(tree)))

def map_list(func, seq):
    if seq == None: return None
    else: return map_list(func(car(seq)), map_list(func, cdr(seq)))

def filt(predicate, seq):
    if seq == None: return None
    elif predicate(car(seq)):
        return filt(predicate, cdr(seq))
    else: return filt(predicate, cdr(seq))

def accumulate(op, init, seq):
    if seq == None: return init
    else:
        if op == 'add':return car(seq)+accumulate(op, init, cdr(seq))
        elif op == 'mul':return car(seq)*accumulate(op, init, cdr(seq))
        else: return op(car(seq), accumulate(op, init, cdr(seq)))


# 2.33
def map_(p, seq):
    return  accumulate(lambda x, y: cons(p(x), y), None, seq)

def append_(seq1, seq2):
    return  accumulate(cons, seq2, seq1)

def length_(seq):
    return accumulate(lambda x,y: 1, 0, seq)


# 2.34
def horner_eval(x, coefficient_seuence):
    return accumulate(lambda this_coeff, higher_item: this_coeff+x*higher_item,
                      0, coefficient_seuence)

# 2.35
def count_leave_(tree):
    # 对树的映射
    # 若节点要叶节点，返回1组成的列表，调用accumulate累积
    # 若节点为内部节点，则调用count_leave_计算叶节点
    return accumulate('add', 0, mapping(lambda x: 1 if not isinstance(x, tuple)
                                                else count_leave_(x), tree))

# 2.36
def car_n(seqs):
    return mapping(car, seqs)

def cdr_n(seqs):
    return mapping(cdr, seqs)

def accumulate_n(op, init, seqs):
    if car(seqs) == None: return None
    else: return cons(accumulate(op, init, car_n(seqs)),
                      accumulate_n(op, init, cdr_n(seqs)))

# 2.37
def dot_product(v, w):
    return accumulate('add', 0, mapping_n(lambda x,y: x*y, v, w))

def matrix_mul_vector(m, v):
    return mapping(lambda col: dot_product(v, col), m)

def _transpose(m):
    return mapping_n(lambda *col: lister(*col), m)

def transpose(mat):
    return accumulate_n(cons, None, mat)

def _matrix_mul_matrix(m, n):
    return mapping(lambda line: mapping_n(lambda *col:
                                          dot_product(line, lister(*col)), n), m)

def matrix_mul_matrix(m, n):
    # 利用矩阵转置将n的列转为行，再利用mapping对n的各行应用点乘
    return mapping(lambda line: mapping(lambda col:
                                        dot_product(line, col), transpose(n)), m)

# 2.38
def fold_right(op, init, seq):
    # 从序列最右侧[op(an, init)]开始组合（折叠）
    # 直接效果就是右侧元素结果作用于左侧元素
    if seq == None: return init
    else:
        if op == 'add':return car(seq)+fold_right(op, init, cdr(seq))
        elif op == 'mul':return car(seq)*fold_right(op, init, cdr(seq))
        elif op == 'div': return car(seq)/fold_right(op, init, cdr(seq))
        else: return op(car(seq), fold_right(op, init, cdr(seq)))

def fold_left(op, init, seq):
    # 从序列最左侧[op(a1, init)]开始组合（折叠）
    # 直接效果就是左侧元素结果作用于右侧元素
    def _iter(result, rest):
        if rest == None: return result
        else:
            if op == 'add':return _iter(result+car(rest), cdr(rest))
            elif op == 'mul':return _iter(result*car(rest), cdr(rest))
            elif op == 'div': return _iter(result/car(rest), cdr(rest))
            else: return _iter(op(result, car(rest)), cdr(rest))
    return _iter(init, seq)

def reverse_right(seq):
    # 直接效果为作则元素作为列表加在右侧元素组成的列表末尾
    return fold_right(lambda x, y: append(y, lister(x)), None, seq)

def reverse_left(seq):
    # 直接效果为构建逆向序列
    return fold_left(lambda x, y: cons(y, x), None, seq)




if __name__ == '__main__':
    list1 = lister(1,2,3)
    list2 = lister(4,5,6)
    list3 = lister(7,8,9)
    list4 = lister(10,11,12)
    seqs = lister(list1, list2, list3, list4)
    tree = lister(1, lister(2, lister(3, 4), 5), lister(6, 7))
    
    display(accumulate('add', 0, list1))
    display(map_(lambda x: x**2, list1))
    display(append_(list1, list2))
    display(length(list1))
    print(horner_eval(2, lister(1, 3, 0, 5, 0, 1)), '\n')
    print(count_leave_(tree), '\n')
    display(accumulate_n('add', 0, seqs))
    display(mapping_n(lambda x,y,z,k: x+y+z+k, seqs))

    v1 = lister(1, 2, 3, 4)
    v2 = lister(4, 5, 6, 6)
    v3 = lister(6, 7, 8, 9)
    m  = lister(v1, v2, v3)
    print(dot_product(v1, v2), '\n')
    display(matrix_mul_vector(m,v1))
    display(transpose(m))
    display(matrix_mul_matrix(m, transpose(m)))

    display(fold_right('div', 1, list1))
    display(fold_left('div', 1, list1))
    print(fold_right(lister, None, list1))
    print(fold_left(lister, None, list1))
    print(reverse_right(list1))
    print(reverse_left(list1))
