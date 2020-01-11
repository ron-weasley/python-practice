import collections
from collections import Counter

txt = "kdfgvuyvbedcjhbfvirbth1293478307cvx"
print(list(Counter(txt).elements()))
print("most_common: ", Counter(txt).most_common(3))
print(list(Counter(q=0, m=1, n=-100, p=4, d=5).elements()))

m = Counter("manny")
n = Counter("nanny")
print(m - n)
print(m + n)
print(m & n)
print(m | n)

# dequeue - Double Ended Queue
deq = collections.deque(["harry", "potter"])
deq.append("lol")
deq.append(1980)
deq.appendleft("The Hobbit")
print(deq)
deq.rotate(1)  # clockwise
print(deq)
deq.rotate(-2)  # anti-clockwise
print(deq)
print(deq.count("harry"))
deq.remove("lol")
print(len(deq))

deqCopy = deq.copy()
print("copy: ", deq)
print(id(deq[0]))
print(id(deqCopy[0]))
