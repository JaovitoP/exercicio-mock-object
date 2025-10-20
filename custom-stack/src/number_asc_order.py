from src.custom_stack_class import CustomStack, StackEmptyException


class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if not isinstance(stack, CustomStack):
            raise TypeError("O parâmetro deve ser uma instância de CustomStack")
        
        if stack.is_empty():
            raise StackEmptyException("A pilha está vazia")
        
        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
