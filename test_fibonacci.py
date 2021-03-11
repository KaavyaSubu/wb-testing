import fibonacci


class TestFib:
    def test_printFib(self):
        assert [0,1,1,2,3,5,8,13,21,34] == fibonacci.printFib()
