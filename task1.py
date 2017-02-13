def battle(numlist):

    evens = []
    odds = []

    # assigning numbers to proper lists - even and odd
    for num in numlist:
        if num == 0:  # removing zeros as they have no effect on a battle
            numlist.remove(num)
        elif num % 2 == 0:
            evens.append(int(bin(num).replace("0b", "")))
        else:
            odds.append(int(bin(num).replace("0b", "")))

    # main part comparing numbers of soldiers of each side
    even_soldiers = counter(evens, "0")
    odd_soldiers = counter(odds, "1")
    if even_soldiers > odd_soldiers:
        print("evens win")
    elif even_soldiers < odd_soldiers:
        print("odds win")
    else:
        print("tie")


def counter(numbers, soldier):
    """Function counting soldiers for positive numbers and spies
    for negative numbers and returning the difference"""
    spies = 0
    soldiers = 0
    for number in numbers:
        if number < 0:
            number = str(number)
            spies += number.count(soldier)
        else:
            number = str(number)
            soldiers += number.count(soldier)

    return soldiers - spies
