def count_summa(a):
    if a == []:
        return 0
    else:
        sum = count_summa(a[1:])
        sum = sum + a[0]
        return sum


x1 = int(input("введіть перше натуральне число списку = "))
x2 = int(input("введіть останнє натуральне число списку = "))

a = list(range(x1, x2 + 1))
c = count_summa(a)
print("сумма всіх натуральних чисел списку = ", c)
