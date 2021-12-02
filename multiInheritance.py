class A(object):
    def __init__(self, *args, **kwargs):
        print("A")
        # super(A, self).__init__(*args, **kwargs)


class B(object):
    def __init__(self, *args, **kwargs):
        print("B")
        # super(B, self).__init__(*args, **kwargs)


class C(B):
    def __init__(self, *args, **kwargs):
        print("C")
        # super(B, self).__init__(*args, **kwargs)

class E(A, C):
    def __init__(self, arg, *args, **kwargs):
        print("E", "arg=", arg)
        super(E, self).__init__(arg, *args, **kwargs)
        C.__init__(self, *args, **kwargs)


print("MRO:", [x.__name__ for x in E.__mro__])
E(10)
