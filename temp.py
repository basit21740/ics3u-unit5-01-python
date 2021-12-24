#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# This program can convert degrees celsius to fahrenheit


def fahrenheit():
    # this function can convert degrees celsius to fahrenheit

    print("This program can convert degrees celsius to fahrenheit.")
    print("\n", end="")

    # input
    temperature_string = input("Enter a temperature(℃): ")
    print("\n", end="")

    try:
        temperature_integer = int(temperature_string)

        # process
        fahrenheit = (9/5)*temperature_integer + 32

        # output
        print("{0}°C is equal to {1}°F"
              .format(temperature_integer, fahrenheit))

    except Exception:
        print("This is not an integer")
    
    print("\nDone.")

def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()