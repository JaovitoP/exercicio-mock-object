import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_and_top():
    stack = CustomStack(3)
    stack.push(10)
    assert stack.top() == 10
    assert not stack.is_empty()
    assert stack.size() == 1


def test_push_until_full():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(StackFullException):
        stack.push(3)


def test_pop_removes_element():
    stack = CustomStack(3)
    stack.push("a")
    stack.push("b")
    popped = stack.pop()
    assert popped == "b"
    assert stack.top() == "a"
    assert stack.size() == 1


def test_pop_from_empty_stack_raises():
    stack = CustomStack(1)
    with pytest.raises(StackEmptyException):
        stack.pop()


def test_top_from_empty_stack_raises():
    stack = CustomStack(2)
    with pytest.raises(StackEmptyException):
        stack.top()


def test_is_empty_and_size_behavior():
    stack = CustomStack(5)
    assert stack.is_empty()
    stack.push(99)
    assert not stack.is_empty()
    assert stack.size() == 1
