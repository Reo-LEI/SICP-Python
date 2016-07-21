from orderedPair import *

__all__ = ['op_type_table', 'put', 'get', 'attach_tag', 'type_tag', 'content',
           'appaly_generic']

# 由于put和get过程到3.3节才介绍，故在此先用如下的替代版进行练习
op_type_table = {}


def put(op, type, item):
    global op_type_table
    if type in op_type_table:
        op_type_table[type][op] = item
    else:
        op_type_table[type] = {}
        op_type_table[type][op] = item


def get(op, type):
    return op_type_table[type][op]


def attach_tag(tag, data):
    return cons(tag, data)


def type_tag(data):
    return car(data)


def content(data):
    return cdr(data)


def appaly_generic(op, *args):
    def types(*seq):
        seqs = lister(*seq)
        return mapping(type_tag, seqs)

    def contents(*seq):
        seqs = lister(*seq)
        return mapping(content, seqs)

    def funcs(op, tags):
        if tags is None:
            return None
        else:
            return cons(get(op, car(tags)), funcs(op, cdr(tags)))

    def iter(op_seq, data_seq):
        if op_seq is None:
            return None
        else:
            return cons(car(op_seq(car(data_seq))),
                        iter(cdr(op_seq), cdr(data_seq)))

    type_tags = types(*args)
    datas = contents(*args)
    proc = funcs(op, type_tags)

    if length(proc) > 1:
        return iter(proc, datas)
    elif length(proc) == 1:
        return car(proc)(car(datas))
    else:
        return print('No method for these types -- APPLY_GENERIC')


if __name__ == '__main__':
    def test1(x):
        return print(x)


    def test2(x):
        return print(x)


    def test3(x):
        return print(-x)

    put('test1', 'T1', test1)
    put('test2', 'T2', test2)
    put('test3', 'T2', test3)

    def test3(x):
        return print(x)
    put('test3', 'T1', test3)

    print(op_type_table)

    print(get('test1', 'T1'))
    get('test1', 'T1')(1)
    print(get('test2', 'T2'))
    get('test2', 'T2')(2)
    print(get('test3', 'T2'))
    get('test3', 'T2')(3)

    x = attach_tag('T1', 1)
    y = attach_tag('T2', 1)

    def test_t3(k):
        return appaly_generic('test3', k)
    test_t3(x)
    test_t3(y)