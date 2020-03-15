# import replit


def main():
    while True:  # Emulate do_while loop
        lines = input("Number of lines: ")

        try:
            print_pascal(int(lines))
        except ValueError:  # Catch errors
            print("Please enter an integer.")

        response = input(
            "\n...press enter to continue.... type 'stop' to exit\n")
        if response == "stop":  # Break condition
            break
        # replit.clear() # Clear the console


def calculate_row(n):
    """Calculate row 'n' of Pascal's triangle and return a list."""
    line = [1]
    for k in range(1, n):
        value = line[k - 1] * (
            n - k) // k  #Formula for element k in row n of Pascal's triangle
        line.append(value)
    return line


def pascal(lines):
    """Calculate Pascal's triange with the specified number of lines and return a list of rows"""

    triangle = []
    for row in range(1, lines + 1):
        triangle.append(calculate_row(row))
    return triangle


def print_pascal(lines):
    """Print Pascal's triangle with the specified number of lines."""

    if lines == 0:  #If zero rows are requested
        print()
        return

    triangle = pascal(lines)  #Generate the triangle list
    last_row = triangle[-1]

    #Utility function to format one row of the triangle
    def format_row(row):
        max_num_width = len(str(
            last_row[len(last_row) // 2]))  #Padding between each element
        
        line_str=" ".join([f"{element:^{max_num_width}}" for element in row])
        # line_str = ""
        # for element in row:
        #     line_str += f" {element:^{max_num_width}} "  #Center each element in alloted space
        return line_str

    max_width = len(format_row(last_row))

    #Finally, print each row
    for row in range(lines):
        f_row = format_row(triangle[row])
        print(f"{f_row:^{max_width}}")  #Center the formated row in the space of longest row


# execute only if run as a script
if __name__ == "__main__":
    main()
