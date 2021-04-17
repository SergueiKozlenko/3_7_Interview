class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def size(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]


if __name__ == '__main__':
    brackets = '()[]{}'
    input_string = list(input('Введите последоательность:'))
    negative_result = ''
    stack = Stack()
    for element in input_string:
        if (brackets.index(element) + 1) % 2 != 0:
            stack.push(element)
        if (brackets.index(element) + 1) % 2 == 0:
            if stack.isEmpty():
                negative_result = 'Несбалансированно: непарная закрывающая скобка'
                break
            elif stack.peek() + element in brackets:
                stack.pop()
            else:
                negative_result = 'Несбалансированно: непарная закрывающая скобка'
                break
    if negative_result:
        print(negative_result)
    elif stack.size() == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно: непарная открывающая скобка')
