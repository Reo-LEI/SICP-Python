# Exercise 1.1
# Below is a sequence of expressions.
# What is the result printed by the interpreter
# in response to each expression? Assume that the sequence
# is to be evaluated in the order in which it is presented.

# Statement
Solution  # with explanation

# 10
10

# (+ 5 3 4)
5 + 3 + 4  # = 12

# (- 9 1)
9 - 1  # = 8

# (/ 6 2)
6 / 2  # = 3

# (+ (* 2 4) (- 4 6))
(2 * 4) + (4 - 6)  # = 6

# (define a 3)
a = 3
# the value of a is now 3; print nothing

# (define b (+ a 1))
b = a + 1
# b = 4; print nothing

# (+ a b (* a b))
a + b + (a * b)  # = 3 + 4 + (3 * 4) = 19

# (= a b)
a = b  # This is a boolean check
# Results in "False"

"""
(if (and (> b a) (< b (* a b)))
    b
    a)
"""
if b > a and b < (a * b):  # This condition is true
    b  # this is returned
else:
    a  # this is not returned
# 4

"""
(cond ((= a 4) 6)
      ((= b 4) (+ 6 7 a))
      (else 25))
"""
if a = 4:  # False
    return 6
elif b = 4:  # True
    return 6 + 7 + a  # This is returned
else:
    return 25  # This line does not run

# (+ 2 (if (> b a) b a))
2 + b if b > a else a  # 6

"""
(* (cond ((> a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1))
"""
if a > b:  # False
    z = a
elif a < b:  # True
    z = b
else:  # Skip
    z = -1
return z * (a + 1)
# 16
