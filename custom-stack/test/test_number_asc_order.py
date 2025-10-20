import pytest
from src.number_asc_order import NumberAscOrder
from src.custom_stack_class import CustomStack, StackEmptyException

def test_sort_returns_sorted_numbers():
    stack = CustomStack(6)
    numbers = [25, 3, 14, 50, 8, 1]
    for n in numbers:
        stack.push(n)

    sorter = NumberAscOrder()
    sorted_numbers = sorter.sort(stack)

    assert sorted_numbers == sorted(numbers)
    assert stack.is_empty()


def test_sort_empty_stack_raises():
    stack = CustomStack(6)
    sorter = NumberAscOrder()
    with pytest.raises(StackEmptyException):
        sorter.sort(stack)


def test_sort_invalid_parameter_raises():
    sorter = NumberAscOrder()
    with pytest.raises(TypeError):
        sorter.sort([1, 2, 3])
