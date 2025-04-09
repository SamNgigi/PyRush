class Foo:

    @staticmethod
    def foo() -> int:
        """
        This is a multiline docstring
        Params: None:
        Returns: int
        """
        print("Function to remove")
        return 40

    @staticmethod
    def bar() -> int:
        """This is a single line docstring"""
        print('Another function to remove')
        return 44
