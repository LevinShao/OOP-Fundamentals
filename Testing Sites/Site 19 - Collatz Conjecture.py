def collatz_sequence(n):
    """
    Generates and prints the Collatz sequence for a given positive integer.

    Args:
        n: A positive integer to start the sequence.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return

    print(f"Collatz sequence for {n}:")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = (3 * n) + 1
        sequence.append(n)
    print(sequence)

n_choice = input("What shall n be > ")

collatz_sequence(n_choice)