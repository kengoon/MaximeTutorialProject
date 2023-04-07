class A:
    def say_hello(self):
        print("Hello")

    def ada(self):
        print("ada")

# class B(A):
#     def say_hello(self):
#         print("hello")
#
#
# B().say_hello()

def _say_hello(self):
    print("Hello World")

A.say_hello = _say_hello
a = A()
a.say_hello()
a.ada()
