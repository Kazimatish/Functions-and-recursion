def recursive(n):
    if(n == 0):
        return 'good bye'
    print("Kalam")
    recursive(n - 1)

recursive(n = int(input("Enter a number: ")))