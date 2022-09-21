a = [i for i in range(10, 20)]
b = [i for i in range(15)]

print(f"перший список {a}")
print(f"другий список {b}")

set_a = set(a)
set_b = set(b)

set_c = set_b.difference(set_a)
set_d = set_a.difference(set_b)
print()
print(f"в 1-му списку відсутні такі елементи 2-го списку {set_c}")
print(f"в 2-му списку відсутні такі елементи 1-го списку {set_d}")

