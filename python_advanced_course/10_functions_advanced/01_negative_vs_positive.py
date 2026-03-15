def nums_sum(*args):
    n_sum = 0
    p_sum = 0

    for num in args:
        if num > 0:
            p_sum += num
        else:
            n_sum += num

    return n_sum, p_sum


numbers = [int(x) for x in input().split()]
neg_sum, pos_sum = nums_sum(*numbers)

print(neg_sum)
print(pos_sum)
if abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
