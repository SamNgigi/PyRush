class Foo:

    @staticmethod
    def foo() -> int:
        """
        This is a multiline docstring
        Params: None:
        Returns: int
        """
        return 45

    @staticmethod
    def bar() -> int:
        """This is a single line docstring"""
        print('Another function to remove')
        return 44
