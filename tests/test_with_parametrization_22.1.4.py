from main import is_triangle
import pytest

def ids_a(val):
   return "a=({0})".format(str(val))

def ids_b(val):
   return "b=({0})".format(str(val))

def ids_c(val):
   return "c=({0})".format(str(val))

@pytest.mark.parametrize('a', [-1, 0, 2, 3, 1], ids=ids_a)
@pytest.mark.parametrize('b', [-1, 0, 1, 4, 15], ids=ids_b)
@pytest.mark.parametrize('c', [-3, 0, 1, 5, 1], ids=ids_c)
def test_is_triangle(a, b, c):
    result = is_triangle(a, b, c)
    if a <= 0 or b <= 0 or c <= 0:
        assert result == False
    elif a + b > c and a + c > b and b + c > a:
        assert result == True
    elif a + b <= c and a + c <= b and b + c <= a:
        assert result == False

