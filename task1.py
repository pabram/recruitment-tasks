def task_1(numlist):
    # removing zeros from list as they have no effect on a battle
    while 0 in numlist:
        numlist.remove(0)

    evens = []
    odds = []

    # assigning numbers to proper lists - even and odd
    for num in numlist:
        if num % 2 == 0:
            evens.append((bin(num)).replace("0b", ""))
        else:
            odds.append((bin(num)).replace("0b", ""))

    # main part comparing numbers of soldiers of each side
    if counter(evens, "0") > counter(odds, "1"):
        print("evens win")
    elif counter(evens, "0") < counter(odds, "1"):
        print("odds win")
    else:
        print("tie")


def counter(numbers, soldier):
    """Function counting soldiers for positive numbers and spies for negative numbers and returning the difference"""
    spies = 0
    soldiers = 0
    for number in numbers:
        if int(number) < 0:
            spies += number.count(soldier)
        else:
            soldiers += number.count(soldier)

    return soldiers - spies
