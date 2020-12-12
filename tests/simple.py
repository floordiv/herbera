from herbera import breakpoint


x = 5
breakpoint()
x = 10
breakpoint()


class MyClass:
    class AnotherClass:
        def __init__(self):
            self.type = 'hello!'

    @staticmethod
    def hello():
        return 'world'


breakpoint()
