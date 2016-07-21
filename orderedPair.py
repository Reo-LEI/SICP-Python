__all__ = ['cons', 'car', 'cdr', 'lister', 'list_ref', 'length', 'append',
           'last_pair', 'reverse', 'mapper', 'for_each', 'display', 'count_leave',
           'deep_reverse', 'mapper', 'mapping', 'subsets', 'mapping_n']


def cons(a, b):
    return (a, b)


def car(x):
    return x[0]


def cdr(x):
    return x[1]


def car_n(seqs):
    return mapping(car, seqs)


def cdr_n(seqs):
    return mapping(cdr, seqs)


def lister(*args):
    def conser(x, y):
        if not y:
            return cons(x, None)
        else:
            return cons(x, conser(y[0], y[1:]))
    L = list(args)
    first, other = L[0], L[1:]
    return conser(first, other)


# def lister(first, *args):
#     if first == ():
#         return None
#     elif isinstance(first, tuple):
#         return cons(first[0], lister(first[1:]))
#     else:
#         return cons(first, lister(args))


def list_ref(item, n):
    if n == 0:
        return car(item)
    else:
        return list_ref(cdr(item), n-1)


def last_pair(item):
    if cdr(item) is None:
        return car(item)
    else:
        return last_pair(cdr(item))


def length(item):
    if item is None:
        return 0
    else:
        return 1+length(cdr(item))


def count_leave(item):
    if item is None:
        return 0
    elif not isinstance(item, tuple):
        return 1
    else:
        return count_leave(car(item))+count_leave(cdr(item))


def append(l1, l2):
    if l1 is None:
        return l2
    else:
        return cons(car(l1), append(cdr(l1), l2))


def reverse(item):
    if not isinstance(item, tuple):
        return item
    else:
        return cons(reverse(cdr(item)), car(item))


def deep_reverse(item):
    if not isinstance(item, tuple):
        return item
    else:
        return cons(deep_reverse(cdr(item)), deep_reverse(car(item)))


def mapping(func, item):
    # return a seq
    # 接受一个序列，依次将序列各个元素作为func的参数，返回结果序列
    if item is None:
        return None
    else:
        return cons(func(car(item)), mapping(func, cdr(item)))


def mapper(func, tree):
    # return a tree
    # 接受一个树，依次讲各个叶节点作为func的参数，返回树
    if tree is None:
        pass
    elif not isinstance(tree, tuple):
        return func(tree)
    else:
        return cons(mapper(func, car(tree)), mapper(func, cdr(tree)))


def mapping_n(func, *seqs):
    # return a seq
    # 接受n个序列，依次取各个序列第k元素组成序列seq(k)作为func的参数，返回结果序列
    def car_n(seq):
        return mapping(car, seq)

    def cdr_n(seq):
        return mapping(cdr, seq)

    def seq_trans(seq):  # 将序列转化为元组
        def translator(s):
            if cdr(s) is None:
                return [car(s)]
            else:
                return [car(s)]+translator(cdr(s))
        return tuple(translator(seq))

    def _map(f, seq):
        if car(seq) is None:
            return None
        else:
            return cons(f(*seq_trans(car_n(seq))), _map(f, cdr_n(seq)))  # 用*解包元组调用f

    if len(seqs) > 1:
        seqs = lister(*seqs)  # 判断seqs为树或者多个列表并解包
    else:
        seqs = seqs[0]  # 若为树直接解包
    return _map(func, seqs)


def for_each(proc, item):
    if item is None:
        pass
    else:
        proc(car(item))
        for_each(proc, cdr(item))


def subsets(s):
    # 递归思路:
    # 集合{a,b,c}的子集=集合{b,c}的子集+集合{b,c}的子集与集合{a}的并集
    # 集合{b,c}的子集=集合{c}的子集+集合{c}的子集与集合{b}的并集
    # 集合{c}的子集={}和{c}
    if s is None:
        return lister(None)
    else:
        return append(subsets(cdr(s)), mapping(lambda x: cons(car(s), x), subsets(cdr(s))))


def display(items):

    def order(item):
        if item is None:
            return False
        elif not isinstance(item, tuple):
            return True
        else:
            return order(car(item))

    if order(items):

        def show(item):
            if not isinstance(item, tuple):
                # 判断叶子，由[show(car(item))]处理
                # 直接返回元素，
                return item

            elif cdr(item) is None:
                # 嵌套列表叶子为(x, None)形式，由show(cdr(item))处理
                # 避免None再次引用递归，提前省去并除去None标识符
                # [car(item)]为与其余元素合并作准备
                return [car(item)]

            elif not isinstance(cdr(item), tuple):
                # 非嵌套列表为序对，序对cdr(item)由于没有None所以并非(x, None)形式
                # 序对用元组表示
                # 序对cdr(item)为元素，所以[show(cdr(item))]需嵌套到列表中合并
                return tuple([show(car(item))]+[show(cdr(item))])

            elif isinstance(car(cdr(item)), tuple) and cdr(cdr(item)) == None:
                # item为只有一项的嵌套列表,其第一项为列表，第二项为标识符None
                # [show(car(item))]构建外层列表
                # [show(car(cdr(item)))] 取嵌套列表余下元素并嵌套
                return [show(car(item))]+[show(car(cdr(item)))]

            else:
                # item列表大于一项
                # [show(car(item))]为最外层构建列表, 若有嵌套列表元素会再次递归，表现为再嵌套
                # show(cdr(item))再次调用函数处理余下列表
                return [show(car(item))]+show(cdr(item))

    else:

        def nested(item):
            if item is None:
                return False
            elif isinstance(cdr(item), tuple) and car(item) is None:
                return True
            else:
                return nested(car(item))

        def show(item):
            if not isinstance(item, tuple):
                return item
            elif car(item) is None:
                return [cdr(item)]
            elif not isinstance(car(item), tuple):
                return tuple([show(car(item))]+[show(cdr(item))])
            elif nested(item):
                return [show(cdr(car(item)))]+[show(cdr(item))]
            else:
                return show(car(item))+[show(cdr(item))]

    print(show(items), '\n')
    return show(items)

if __name__ == '__main__':
    display(lister(1, 2, 3, 4))

    x = cons(lister(1, 2), lister(3, 4))
    display(x)
#    print(x, length(x), count_leave(x), '\n')

    y = lister(lister(1, 2), lister(3, 4))
    display(y)
#    print(y, length(y), count_leave(y), '\n')

    z = lister(cons(1, 2), cons(3, 4), 5, 6)
    display(z)
#    print(z, length(z), count_leave(z), '\n')

    p = lister(1, lister(2, lister(3, 4)))
    display(p)
#    print(p, length(p), count_leave(p), '\n')

    list1 = lister(1, 2, 3)
    list2 = lister(4, 5, 6)
    list3 = lister(7, 8, 9)
    testlist = lister(list1, list2, list3)
    display(testlist)
#    print(listtest, '\n')
#    print(reverse(listtest), '\n')
    r = deep_reverse(testlist)
    k = deep_reverse(p)
#    print(deep_reverse(listtest), '\n')
#    print(k, '\n')
    display(r)
    display(k)
    display(mapper(lambda x: x**2, testlist))
    display(mapping_n(lambda x, y, z: x+y+z, list1, list2, list3))
