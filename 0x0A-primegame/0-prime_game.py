#!/usr/bin/python3

# Prime number checker

# from array import array


def isWinner(x, nums):
    # where x is the number of rounds and nums is an array of n
    # Return: name of the player that won the most rounds
    # If the winner cannot be determined, return None

    ben = 0
    maria = 0
    for a in nums:
        print(a)
        primes = []
        for i in range(2, a+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        # print(primes)
        if(len(primes) % 2 == 0):
            ben = ben + 1

        else:
            maria = maria+1

    if(maria > ben):
        return('Winner: Maria')
    elif(maria < ben):
        return('Winner: Ben')
    else:
        return ('Winner: None')


isWinner(5, [2, 5, 1, 4, 3])
