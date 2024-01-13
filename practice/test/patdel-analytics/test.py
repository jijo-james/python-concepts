# list of intergers

list_of_integers = [0, 1, 5, 2, 0, -1, 0]


def main(numbers: list, direction: str) -> list:
    count = 0
    if direction in ["right", "RIGHT", "R", "r"]:
        for i in numbers:
            if i == 0:
                count += 1
                numbers.remove(i)

        for i in range(count):
            numbers.append(0)
        return numbers

    if direction in ["left", "LEFT", "l", "L"]:
        zeros = []
        for i in numbers:
            if i == 0:
                zeros.append(i)
                numbers.remove(i)

        for i in range(len(numbers)):
            zeros.append(numbers[i])

        return zeros

    else:
        return "Invalid direction"


# if __name__ == __main__:
direction = str(input("Enter the direction to where '0's' need to move (L/r)"))
print(main(list_of_integers, direction))
