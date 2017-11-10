import pytest

def inc(x):
    return x + 1;

def test_answer():
    assert inc(3) == 4
    # assert inc(3) == 3

def test_modulo():
    a = 24
    assert a % 2 == 0, "value was odd, should be even"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)

# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    # def test_two(self):
    #     assert a % 2 == 0, "value was odd, should be even"
