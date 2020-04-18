def test():
    string = "Hello"

    print(string.lower())

    print(string.capitalize())

    print(string.upper())

    # userInput = input("Enter an integer value")


test()

def Q3(a, b, c):
    data = [a, b, c]
    for x in range(0, 2):
        temp = data[x]
        data[x] = data[x + 1]
        data[x + 1] = temp
    print(data[0], data[1], data[2])


Q3(3, 1, 2)


def Q5():
    width = input("Enter the width of the picture")
    while (width < 1):
        width = input("Error. Enter a value greater than 0. Enter the width of the picture")

    height = input("Enter the height of the picture")
    while (height < 1):
        height = input("Error. Enter a value greater than 0. Enter the height of the picture")

    # newPic = makeEmptyPicture(width, height)

    total = 0

    prevX = 0
    prevY = 0
    prevW = 0
    prevH = 0

    more = 1

    while (more == 1):

        rectX = input("Enter the x coord for the rectangle")
        while (rectX < 1) or (rectX > width - 1):
            rectX = input("Error. Enter a value greater than 0 and less than " + str(width - 1))

        rectY = input("Enter the y coord for the rectangle")
        while (rectY < 1) or (rectY > height - 1):
            rectY = input("Error. Enter a value greater than 0 and less than " + str(height - 1))

        rectW = input("Enter the width for the rectangle")
        while (rectW < 1) or (rectW > width - 1 - rectX):
            rectW = input("Error. Enter a value greater than 0 and less than " + str(width - 1 - rectX))

        rectH = input("Enter the height for the rectangle")
        while (rectH < 1) or (rectH > height - 1 - rectY):
            rectH = input("Error. Enter a value greater than 0 and less than " + str(height - 1 - rectY))

        # addRect(newPic, rectX, rectY, rectW, rectH)
        # repaint(newPic)

        prevX = rectX
        prevY = rectY
        prevW = rectW
        prevH = rectH

        total = total + 1

        more = input("Enter 1 to continue")

        while (more == 1):

            rectX = input("Enter the x coord for the rectangle")
            while (rectX < prevX and rectX > prevX + prevW):
                rectX = input(
                    "Error. Enter a value greater than " + str(prevX) + " and less than " + str(prevX + prevW))

            rectY = input("Enter the y coord for the rectangle")
            while (rectY < prevY and rectY > prevY + prevH):
                rectY = input(
                    "Error. Enter a value greater than " + str(prevY) + " and less than " + str(prevY + prevH))

            rectW = input("Enter the width for the rectangle")
            while (rectW < 1) or (rectW > prevX - prevW):
                rectW = input("Error. Enter a value greater than 1 and less than " + str(prevX - prevW))

            rectH = input("Enter the height for the rectangle")
            while (rectH < 1) or (rectH > prevY - prevH):
                rectH = input("Error. Enter a value greater than 1 and less than " + str(prevY - prevH))

            # addRect(newPic, rectX, rectY, rectW, rectH)
            # repaint(newPic)

            prevX = rectX
            prevY = rectY
            prevW = rectW
            prevH = rectH

            total = total + 1

            more = input("Enter 1 to continue")

    print("The total number of rectangles added was " + str(total))


Q5()
