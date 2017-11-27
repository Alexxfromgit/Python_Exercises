

def multiples_of_3_and_5(a):
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
    for i in range(a):
        x.append(i)

        if (x[i] % 3 == 0 or x[i] % 5 == 0) and x[i] != 0:
            z.append(i)

    return sum(z)


#for answer use this:
print(multiples_of_3_and_5(1000))
