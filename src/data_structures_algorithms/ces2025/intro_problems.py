# CSES Problem Set https://cses.fi/problemset/list/
def weird_algorithm():
    """
    Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
    $$ 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$$
    Your task is to simulate the execution of the algorithm for a given value of n.
    Input
    The only input line contains an integer n.
    Output
    Print a line that contains all values of n during the algorithm.
    Constraints

    1 \\le  \\le 10^6

    Example
    Input:
    3

    Output:
    3 10 5 16 8 4 2 1
    """
    n:int = int(input())
    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        print(n, end="")


def missing_number():
    """
    You are given all numbers between 1,2,\\ldots,n except one. Your task is to find the missing number.
    Input
    The first input line contains an integer n.
    The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
    Output
    Print the missing number.
    Constraints

    2 \\le n \\le 2 \\cdot 10^5

    Example
    Input:
    5
    2 3 1 5

    Output:
    4
    """
    n: int = int(input())
    nums = input()
    nums_sum = sum(int(i) for i in nums.split())
    n_sum = sum(range(n+1))
    print(n_sum - nums_sum)






if __name__ == "__main__":
    missing_number()
