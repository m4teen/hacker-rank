import math

def is_smart_number(num):
    """
    Determines whether a number is a 'smart number' (i.e. has an odd number of factors).

    A number is considered 'smart' if it is a perfect square, since only perfect squares
    have an odd number of divisors. For each test case, the program reads an integer and 
    prints 'YES' if it is smart, otherwise 'NO'.
    """
    val = int(math.sqrt(num))
    if len([x for x in range(1,val+1) if x**2 == num]) % 2 != 0:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



