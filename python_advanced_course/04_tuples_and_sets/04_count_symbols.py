text = input()
elements_dict = {}
result_set = set()
for el in text:
    result_set.add(el)
    if el not in elements_dict:
        elements_dict[el] = 1
    else:
        elements_dict[el] += 1

result_sorted = sorted(result_set)

for symbol in result_sorted:
    print(f"{symbol}: {elements_dict[symbol]} time/s")
