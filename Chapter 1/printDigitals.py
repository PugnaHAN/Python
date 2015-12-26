Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One  = ["   *   ",
        "  **   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "   *   ",
        "  ***  "]

Two  = ["  ***  ",
        " *   * ",
        "*     *",
        "     * ",
        "   *   ",
        " *     ",
        "* * * *"]

Three = ["  ***  ",
         " *   * ",
         "      *",
         "  ***  ",
         "      *",
         " *   * ",
         "  ***  "]

Four = ["   *   ",
        "  **   ",
        " *  *  ",
        "*   *  ",
        "* * * *",
        "   *   ",
        "  ***  "]

Five = [" * * * ",
        " *     ",
        " *     ",
        " * * * ",
        "      *",
        "*     *",
        " * * * "]

Six  = ["  ***  ",
        " *     ",
        "*      ",
        "* ***  ",
        "*     *",
        " *   * ",
        "  ***  "]
Seven = ["** * **",
         "*    * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     ",
         "*      "]

Eight = ["  ***  ",
         " *   * ",
         "*     *",
         "  ***  ",
         "*     *",
         " *   * ",
         "  ***  "]

Nine = ["  ***  ",
        " *   * ",
        " *   * ",
        "  **** ",
        "     * ",
        " *   * ",
        "  ***  "]

digitals = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

number = input("Enter a number:")
i = 0
while i < 7:
    for num in number:
        n = int(num)
        outDigital = digitals[n][i]
        for c in outDigital:
            if c == '*':
                print(n, end = "")
            else:
                print(c, end = "")
        print(" ", end = "")
        #print(digitals[n][i], end = " ")
    print("\n", end = "")
    i += 1  
