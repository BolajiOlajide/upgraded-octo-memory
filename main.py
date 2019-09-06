from dummy.ops import add

try:
    add(1, '2')
except TypeError as e:
    print(f'I warned you oooo. => {e.args[0]}')

print(f"The result is {add(5, 2)}")
