#!/usr/bin/python3
""" Prime Game setup """


def isprime(n):
    """ Return prime number """
    for s in range(2, n):
        if n % s == 0:
            return False
    return True


def delete_numbers(n, nums):
    """ Remove numbers - return zero """
    for s in range(len(nums)):
        if nums[s] % n == 0:
            nums[s] = 0


def isWinner(x, nums):
    """ name of player that won
    most rounds removed
    """
    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):
        # prints("game# ", game+1)
        nums2 = list(range(1, nums[game] + 1))
        # print("nums: ", nums2)
        turn = 0
        while True:
            """
            # monitor turns, uncomment to watch
            if turn % 2 != 0:
                print("Ben turn ")
            else:
                print("Maria turn ")
            """
            change = False
            for s, n in enumerate(nums2):
                # print("n: ", n, "s: ", s)
                if n > 1 and isprime(n):
                    delete_numbers(n, nums2)
                    change = True
                    turn += 1
                    break
            # print("movement: ". nums2)
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
        # print("Maria: {}, Ben: {}".format(Maria, Ben))
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
