def fibonacci_sequence(n):
    if n in {0, 1}:
        return n
    return fibonacci_sequence(n -1) + fibonacci_sequence(n -2)


[fibonacci_sequence(n) for n in range(6)]
[fibonacci_sequence(n) for n in range(1)]
[fibonacci_sequence(n) for n in range(0)]
[fibonacci_sequence(n) for n in range(20)]
