num = int(input())
for i in range(2, num):
    if num % i == 0:
        print("no es primo")
        break
    if i == num - 1 and num % i != 0:
        print("es primo")
