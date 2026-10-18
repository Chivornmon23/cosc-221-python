def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_string = " "
    while stack:
        reversed_string += stack.pop()

    return reversed_string

print(reverse_string("YGNAEL NUON"))
print(reverse_string("YEMILOS RUOP"))
print(reverse_string(" AKILOMLAHPNAHC PAHC"))