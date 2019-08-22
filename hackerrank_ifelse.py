n = int(input("Digite o número: "))

resto = n % 2

if 2<n<5 and resto ==0:
    print("Weird")
elif resto == 0 and n in range(2,5):
    print("Not Weird")
elif resto == 0 and n in range(6,20):
    print("Weird")
elif resto == 0 and n > 20:
    print("Not Weird")
