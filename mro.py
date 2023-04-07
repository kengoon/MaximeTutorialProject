# M.R.O is Method Resolution Order

class A:
    a = 2
    def say_hello(self):
        print("Hello A")

class B:

    a = 3
    # def say_hello(self):
    #     pass
    #     # print("Hello B")


class C(B, A):
    pass

c = C()
print(c.say_hello())