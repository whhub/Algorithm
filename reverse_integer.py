

def reverse_integer(x):
    n = int(x)
    result = 0
    while n != 0:
        tail = n % 10
        n = int(n/10)
        result = result * 10 + tail
    return result

num = 123
print("Reverse %d, get %d" % (num, reverse_integer(num)))
