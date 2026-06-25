def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

g = demo()

print(next(g))
print(next(g))
print(next(g))

def hi():
    for i in range(100):
        yield i
h = hi()
for i in h:
    print(i)