#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 18, 2025

# Min value program in python

import random


def get_min_number(array):

    # Initialize min
    min = 100

    # Find min number by comparing last highest
    for number in array:
        if number < min:
            min = number

    # Return min
    return min


def main():

    # Initialize array
    array = []

    # Add random numbers 10 times to the array
    for counter in range(10):

        # Append and display random number
        random_num = random.randint(1, 99)
        print("Adding {} to the array!".format(random_num))
        array.append(random_num)

    # Set min to function call and display
    lowest_num = get_min_number(array)
    print("The lowest number in the array was", lowest_num, "!")


if __name__ == "__main__":
    main()
