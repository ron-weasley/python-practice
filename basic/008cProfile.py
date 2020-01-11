import cProfile
def c():
 b=4
 c=3.232
 d=int(c+b)
 print(d)
 print(c)

cProfile.run('c()')