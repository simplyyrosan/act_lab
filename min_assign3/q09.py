def pascal_triangle(n):
    triangle = []          # this will hold all rows

    for i in range(n):
        # start each row with 1
        row = [1]

        # for middle elements, each value is sum of two above it
        if triangle:  # not the first row
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])

            row.append(1)  # end each non-first row with 1

        triangle.append(row)

    return triangle


# example: take input and print nicely
rows = int(input("Enter number of rows: "))
for r in pascal_triangle(rows):
    print(" ".join(str(x) for x in r))