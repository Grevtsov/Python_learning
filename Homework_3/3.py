# a = [2,5,-3]
# print(max(a))
# a = a.remove(5)
# a = list(filter(lambda x: x != min(a), a))
# b = [b for b in a if a != min(a)]
# print(b)
def big_sum(a, b, c):
    a = [a, b, c]
    # print(max(a))
    a = list(sorted(a))
    a.remove(a[0])
    return sum(a)

print(big_sum(1,0,-3))