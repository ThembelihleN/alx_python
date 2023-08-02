def fibonacci_sequence(n):
    if n in {0, 1}:
        return n
    return fibonacci_sequence(n -1) + fibonacci_sequence(n -2)


fibonacci_sequence(6)
fibonacci_sequence(1)
fibonacci_sequence(0)
fibonacci_sequence(20)
