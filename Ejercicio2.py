A = []
print("\n-----ingrese 10 datos:-----")
for i in range(10):
    dato=float(input(f"dato{i+1}:"))
    A.append(dato)
B=[]

print("\n-----ingrese 10 datos:-----")
for i in range(10):
    dato=float(input(f"dato{i+1}:"))
    B.append(dato)
C=[round((A[i]-B[i]))for i in range (10)]
print("Arreglo A :")
print("[]".join([f"{n:.2f}"for n in A]))
print("Arreglo B:")
print("[]".join([f"{n:.2f}"for n in B])) 
print("Arreglo C")
print("[]".join([f"{n:.2f}"for n in C]))