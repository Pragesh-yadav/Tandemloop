a = int(input("Enter the number : "))

# Iterate using loop
for num in range(a + 1):
    if num % 2 != 0:
        print(num, end = " ,")
