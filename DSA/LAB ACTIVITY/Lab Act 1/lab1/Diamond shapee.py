def print_diamond(n):
    # Check if n is an odd integer
    if n % 2 == 0:
        return "Please provide an odd integer."

    # Print the upper part of the diamond
    for i in range(1, n // 2 + 2):
        spaces = " " * ((n // 2 + 1) - i)
        superstars = "*" * (2 * i - 1)
        print(spaces + superstars)

    # Print the lower part of the diamond
    for i in range(n // 2, 0, -1):
        spaces = " " * ((n // 2 + 1) - i)
        superstars = "*" * (2 * i - 1)
        print(spaces + superstars)


# Test the function with n  = 5

