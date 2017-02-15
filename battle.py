import sys


def battle(numlist):
    """Spliting numbers into 2 lists - odds and evens, counting their
    0's and 1's, and returning winner"""

    evens = []
    odds = []

    # assigning numbers to proper lists - even and odd
    for num in numlist:
        if num == 0:
            pass
        elif num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    # main part comparing numbers of soldiers of each side
    even_soldiers = counter(evens, "0")
    odd_soldiers = counter(odds, "1")
    if even_soldiers > odd_soldiers:
        return "evens win"
    elif even_soldiers < odd_soldiers:
        return "odds win"
    else:
        return "tie"


def counter(numbers, soldier):
    """Function counting soldiers for positive numbers and spies
    for negative numbers and returning the difference"""
    spies = 0
    soldiers = 0
    for number in numbers:
        # transforming numbers to strings containing their binary representation
        number_as_bin = str(bin(number)).replace("0b", "")
        if number < 0:
            spies += number_as_bin.count(soldier)
        else:
            soldiers += number_as_bin.count(soldier)

    return soldiers - spies

if __name__ == "__main__":
    print(battle([int(arg) for arg in sys.argv[1:]]))
