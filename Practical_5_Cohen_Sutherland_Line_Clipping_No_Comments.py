import matplotlib.pyplot as plt

              
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

                       
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

                                
def cohen_sutherland(x1, y1, x2, y2,
                     xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:

        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2

        elif code1 & code2:
            return None

        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            else:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

                                   
def display(x1, y1, x2, y2, xmin, ymin, xmax, ymax, result):

    plt.figure(figsize=(7, 6))

                     
    plt.plot([xmin, xmax, xmax, xmin, xmin],
             [ymin, ymin, ymax, ymax, ymin],
             'k-', label="Clipping Window")

                   
    plt.plot([x1, x2], [y1, y2], 'b--',
             label="Original Line")

    if result:
        a, b, c, d = result
        plt.plot([a, c], [b, d], 'r-', linewidth=2,
                 label="Clipped Line")
        print("Line accepted after clipping.")
        print("Clipped coordinates:", a, b, c, d)
    else:
        print("Line rejected. It is outside the window.")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Cohen-Sutherland Line Clipping")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()

           
while True:

    print("\n--- LINE CLIPPING MENU ---")
    print("1. Enter Window and Line Coordinates")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        xmin = float(input("Enter xmin: "))
        ymin = float(input("Enter ymin: "))
        xmax = float(input("Enter xmax: "))
        ymax = float(input("Enter ymax: "))

        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if xmin >= xmax or ymin >= ymax:
            print("Invalid clipping window!")
            continue

        result = cohen_sutherland(
            x1, y1, x2, y2,
            xmin, ymin, xmax, ymax
        )

        display(x1, y1, x2, y2,
                xmin, ymin, xmax, ymax, result)

    elif choice == 2:
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Try again.")
