

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < length:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_value)

    print(fibonacci_list)
