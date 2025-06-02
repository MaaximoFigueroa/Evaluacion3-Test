A=[]

for i in range (10):
    while True:
        try:
            A =float(input(f"dato {i+1}:"))
            if 7 <= A <= 700:
                A.append(dato)
                break
            else:
                print("Dato no multiplo de 7 hasta 700")
        except ValueError:
            print("ingrese un  nuevo valor que sea multiplo de 7:")
    for i in range (10):
        dato=float(input(f"dato{i+1}:"))
    print(A[i])