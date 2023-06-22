import sys

Zero = ["   ***   ",
        " *     * ",
        "*       *",
        "*       *",
        "*       *",
        " *     * ",
        "   ***   "]

One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*****"]
Thr = [" *** ", "*   *", "    *", "  **", "    *", "*   *", " *** "]
# For = ["    *", "   **", "  * *", " *  *", " ******", "    *", "    *"]
For = ["    * ", "   ** ", "  * * ", " *  * ", " *****", "    * ", "    * "]
Fiv = ["***** ", "*     ", "* *** ", "     *", "     *", "*    *", " ****"]
Six = ["  ***  ", " *     ", " *     ",
       " ****  ", " *   * ", " *   * ", "  ***  "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = ["  ***  ", " *   * ", " *   * ",
         "  ***  ", " *   * ", " *   * ", "  ***  "]
Nine = [" **** ", "*    *", "*    *", " **** ", "     *", "     *", "     *"]

Digits = [Zero, One, Two, Thr, For, Fiv, Six, Seven, Eight, Nine]
# Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            line = line.replace("*", str(number))
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
