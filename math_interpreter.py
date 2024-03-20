operation = input("Expression :")
x, y, z=operation.split(" ")
# print(f"x={x}, y={y}, z={z}")

if y=='+':
    print(float(int(x) + int(z)))
elif y=='-':
    print(float(int(x) - int(z)))
elif y=='*':
    print(float(int(x) * int(z)))
elif y=='/' and z!=0:
    print(float(int(x) / int(z)))
else:
    print("wrong input")