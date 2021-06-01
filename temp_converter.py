#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 1, 2021
# This program converts Celsius to Fahrenheit and Kelvin


# actual code ###
def Temp_converter():

    # vars
    celsius = input("what is the temperature in Celsius: ")

    # make sure the users num can be an integer
    try:
        celsius = float(celsius)
        # if the number is smaller than absolute 0
        if (celsius < -273.15):
            print("That temperature is not technically possible\n")
            Temp_converter()
        else:
            # convert to fahrenheit and Kelvin
            fahrenheit = celsius * (9/5) + 32
            kelvin = celsius + 273.15
            # print the results
            print("{}° Celsius is {:.1f}° Fahrenheit".
                  format(celsius, fahrenheit))
            print("{}° Clesius is {:.2f}° Kelvin".
                  format(celsius, kelvin))

    except ValueError:
        # if an error arose
        print("Not valid input\n")
        Temp_converter()


def main():
    Temp_converter()


if __name__ == "__main__":
    main()
