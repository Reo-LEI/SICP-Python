from mutable import *


# 3.3.2 queue
def front_ptr(queue):
    return car(queue)


def rear_ptr(queue):
    return cdr(queue)


def set_front_ptr(queue, item):
    return set_car(queue, item)


def set_rear_ptr(queue, item):
    return set_cdr(queue, item)


def make_queue():
    return cons(None, None)


def is_empty_queue(queue):
    if front_ptr(queue) is None:
        return True
    else:
        return False


def front_queue(queue):
    if is_empty_queue(queue):
        return 'error, FRONT call with an empty queue'
    else:
        return car(front_ptr(queue))


def insert_queue(queue, item):
    new_pair = cons(item, None)
    if is_empty_queue(queue):
        set_car(queue, new_pair)
        set_cdr(queue, new_pair)
        return queue
    else:
        set_cdr(rear_ptr(queue), new_pair)
        set_rear_ptr(queue, new_pair)
        return queue


def delete_queue(queue):
    if is_empty_queue(queue):
        return 'error, DELETE called with an empty queue'
    else:
        return set_front_ptr(queue, cdr(front_ptr(queue)))


# exer 3.21
def print_queue(queue):
    display_pair(front_ptr(queue))

q1 = make_queue()
print_queue(q1)

display_pair(insert_queue(q1, 'a'))
print_queue(q1)

display_pair(insert_queue(q1, 'b'))
print_queue(q1)

display_pair(delete_queue(q1))
print_queue(q1)

display_pair(delete_queue(q1))
print_queue(q1)


# exer 3.22
def _make_queue():
    front_ptr = None
    rear_ptr = None

    def set_front_ptr(item):
        nonlocal front_ptr
        front_ptr = item

    def set_rear_ptr(item):
        nonlocal rear_ptr
        rear_ptr = item

    def is_empty_queue():
        if front_ptr is None:
            return True
        else:
            return False

    def front_queue():
        if is_empty_queue():
            return 'error, FRONT call with an empty queue'
        else:
            return car(front_ptr)

    def insert_queue(item):
        new_pair = cons(item, None)
        if is_empty_queue():
            set_front_ptr(new_pair)
            set_rear_ptr(new_pair)
        else:
            set_cdr(rear_ptr, new_pair)
            set_rear_ptr(new_pair)

    def delete_queue():
        if is_empty_queue():
            return 'error, DELETE called with an empty queue'
        else:
            return set_front_ptr(cdr(front_ptr))

    def print_queue():
        display_pair(front_ptr)

    def dispatch(m):
        if m == 'front_ptr':
            return front_ptr
        elif m == 'rear_ptr':
            return rear_ptr
        elif m == 'set_front_ptr':
            return set_front_ptr
        elif m == 'set_rear_ptr':
            return set_rear_ptr
        elif m == 'is_empty_queue':
            return is_empty_queue
        elif m == 'front_queue':
            return front_queue
        elif m == 'insert_queue':
            return insert_queue
        elif m == 'delete_queue':
            return delete_queue
        elif m == 'print_queue':
            return print_queue
    return dispatch


def _front_ptr(q):
    return q('front_ptr')


def _rear_ptr(q):
    return q('rear_ptr')


def _set_front_ptr(q, item):
    return q('set_front_ptr')(item)


def _set_rear_ptr(q, item):
    return q('set_front_ptr')(item)


def _is_empty_queue(q):
    return q('is_empty_queue')()


def _front_queue(q):
    return q('front_queue')()


def _insert_queue(q, item):
    return q('insert_queue')(item)


def _delete_queue(q):
    return q('delete_queue')()


def _print_queue(q):
    return q('print_queue')()

q2 = _make_queue()
_print_queue(q2)

_insert_queue(q2, 'a')
_print_queue(q2)

_insert_queue(q2, 'b')
_print_queue(q2)

_delete_queue(q2)
_print_queue(q2)

_delete_queue(q2)
_print_queue(q2)


# exer 3.23
def dq_front_ptr(deque):
    return car(deque)


def dq_rear_ptr(deque):
    return cdr(deque)


def dq_set_front_ptr(deque, item):
    return set_car(deque, item)


def dq_set_rear_ptr(deque, item):
    return set_cdr(deque, item)


def make_deque():
    return cons(None, None)


def is_empty_deque(deque):
    if dq_front_ptr(deque) is None:
        return True
    else:
        return False


def front_deque(deque):
    if is_empty_queue(deque):
        return 'error, FRONT_DEQUE call with an empty deque'
    else:
        return car(dq_front_ptr(deque))


def rear_deque(deque):
    if is_empty_queue(deque):
        return 'error, REAR_DEQUE call with an empty deque'
    else:
        return car(dq_rear_ptr(deque))


def rear_insert_deque(deque, item):
    new_pair = cons(item, None)
    if is_empty_deque(deque):
        set_car(deque, new_pair)
        set_cdr(deque, new_pair)
        return deque
    else:
        set_cdr(dq_rear_ptr(deque), new_pair)
        dq_set_rear_ptr(deque, new_pair)
        return deque


def rear_insert_deque(deque, item):
    if is_empty_deque(deque):
        return rear_insert_deque(deque, item)
    else:
        return dq_set_front_ptr(deque, cons(item, dq_front_ptr(deque)))


def front_delete_queue(deque):
    if is_empty_deque(deque):
        return 'error, FRONT_DELETE_DEQUE called with an empty deque'
    else:
        return set_front_ptr(deque, cdr(front_ptr(deque)))


def rear_delete_queue(deque):
    def iter(deque, lst):
        if cdr(cdr(lst)) is None:
            set_cdr(lst, None)
            return dq_set_rear_ptr(deque, lst)
        else:
            iter(deque, cdr(lst))

    if is_empty_deque(deque):
        return 'error, REAR_DELETE_DEQUE called with an empty deque'
    elif cdr(dq_front_ptr(deque)) is None:
        return dq_set_front_ptr(deque, None)
    else:
        iter(deque, dq_front_ptr(deque))


# 3.3.3 Table
def symbol_test(sy):
    if isinstance(sy, (str, int, float)):
        return True
    else:
        return False


def equal(seq1, seq2):
    if symbol_test(seq1) and symbol_test(seq2):
        if eq(seq1, seq2):
            return True
        else:
            return False
    elif seq1 is None and seq2 is None:
        return True
    elif eq(car(seq1), car(seq2)):
        return equal(cdr(seq1), cdr(seq2))
    else:
        return False


def look_up(key, table):
    record = assoc(key, cdr(table))
    if record:
        return cdr(record)
    else:
        return False


def assoc(key, records):
    if records is None:
        return False
    elif equal(key, car(car(records))):
        return car(records)
    else:
        return assoc(key, cdr(records))


def insert(key, value, table):
    record = assoc(key, cdr(table))
    if record:
        set_cdr(record, value)
    else:
        set_cdr(table, cons(cons(key, value), cdr(table)))
        return 'ok'


def make_table():
    return cons('*table*', None)


def make_table_2d():
    table = cons('*table*', None)

    def lookup(k1, k2,):
        subtable = assoc(k1, cdr(table))
        if subtable:
            record = assoc(k2, cdr(subtable))
            if record:
                return cdr(record)
            else:
                return False
        else:
            return False

    def insert(k1, k2, value):
        subtable = assoc(k1, cdr(table))
        if subtable:
            record = assoc(k2, cdr(subtable))
            if record:
                set_cdr(record, value)
            else:
                set_cdr(subtable, cons(cons(k2, value), cdr(table)))
        else:
            set_cdr(table,
                    cons(cons(k1, cons(k2, value)),
                         cdr(table)))
        return 'ok'

    def dispatch(m):
        if m == 'lookup-proc':
            return lookup
        elif m == 'insert-proc':
            return insert
        else:
            return 'error, Unkonw operation -- TABLE'
    return dispatch





