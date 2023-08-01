def is_prime(number):
    if number > 1:
        for i in range(2, (number/2) + 1):
            if (number % i) == 0:
                break
            else:
                print("True")
        else:
            print("False")

is_prime(17)
is_prime(15)
is_prime(-5)
is_prime(0)
