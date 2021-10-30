
# counter class variable testing:
class MyClass:
    global_count = 0
    def __init__(self, reset=False):
        if reset:
            MyClass.global_count = 0
        MyClass.global_count += 1
        self.count = MyClass.global_count

    def reset_global_count(self):
        MyClass.global_count = 0

    def __str__(self):
        return str(self.count)

a = MyClass()
print(a)

b = MyClass()
print(b)

print(f"Obj a.count: {a.count}")
print(f"Obj b.count: {b.count}")



class ChildClassA(MyClass):
    def __init__(self, reset=False):
        super().__init__(reset=reset)

class ChildClassB(MyClass):
    def __init__(self, reset=False):
        super().__init__(reset=reset)


ca = ChildClassA(reset=True)
print(f"Obj ca.count: {ca.count}")

cb = ChildClassB(reset=True)
print(f"Obj cb.count: {cb.count}")

cc = ChildClassA()
print(f"Obj cc.count: {cc.count}")

cd = ChildClassB()
print(f"Obj cd.count: {cd.count}")


class ChildClassC(MyClass):
    global_count = 0
    def __init__(self):
        super().__init__()

class ChildClassD(MyClass):
    global_count = 0
    def __init__(self):
        super().__init__()

ce = ChildClassC()
print(f"Obj ce.count: {ce.count}")

cf = ChildClassD()
print(f"Obj cf.count: {cf.count}")
