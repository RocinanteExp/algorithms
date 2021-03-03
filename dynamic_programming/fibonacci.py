import sys

# the slowest method
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# if n is big enough, you will reach maximum recursion call stack exception
def fib_memoize(n, memo):
    if memo[n] is not None:
        return memo[n]
    else:
        result = 1
        if n <= 2:
            result = 1
        else:
            result = fib_memoize(n - 1, memo) + fib_memoize(n - 2, memo)
        memo[n] = result
        return result

# best in performance
def fib_memoize_bottom_up(n):
    if n <= 2:
        return 1;
    memo = [None] * (n + 1)
    memo[1] = memo[2] = 1
    for index in range(3, n + 1):
        memo[index] = memo[index - 1] + memo[index - 2]
    return memo[n]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <number>')
        sys.exit()

    num = fib_memoize_bottom_up(int(sys.argv[1]))
    #num = fib_memoize(int(sys.argv[1]), [None] * (int(sys.argv[1]) + 1))
    #num = fib(int(sys.argv[1]))
    print(num)
