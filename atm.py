#!/usr/bin/python3

odd = "lambda s : len(s) % 2 == 1"

gt3 = "lambda s : len(s) > 3"

d = "lambda s : not eval(s)(s)"

print(eval(odd)(odd))
print(eval(odd)(gt3))
print(eval(gt3)(odd))
print(eval(gt3)(gt3))
print(eval(d)(odd))
print(eval(d)(gt3))
print(eval(d)(d))
