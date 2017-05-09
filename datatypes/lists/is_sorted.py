def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))
