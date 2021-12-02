class A:
    attr1 = []
    def test(self):
        # self.attr2 = "test"
        print(self.attr2 )

class B(A):
    attr2 = "test"


b = B()
b.test()