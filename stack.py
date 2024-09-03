def reverse_string(s: str) -> str:
    stack = []

    
    for char in s:
        stack.append(char)

    
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string


input_string = "Hello World"
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")
