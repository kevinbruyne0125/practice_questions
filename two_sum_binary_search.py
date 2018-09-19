def two_sum(target, arr):

    for i in range(len(arr) - 1):
        _min = 0
        _max = len(arr) - 1
        first_sum = arr[i]
        new_target = target - first_sum
        while _min <= _max:
            guess = int((_max + _min) / 2)
            if arr[guess] == new_target:
                return (arr[guess],first_sum)
                
            elif arr[guess] < new_target:
                _min = guess + 1
            else:
                _max = guess - 1
    return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def big_array(size):
    big_arr = []
    for i in range(0, size):
        big_arr.append(i)
    return big_arr


try:
    target = int(input('Input target --> '))
    #array_size = int(input('Input list size --> '))
    print(two_sum(target,primes))
except ValueError:
    print("Integers only buddy boyo")



