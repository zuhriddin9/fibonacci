def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sum(n):
    if n <= 0:
        return 0
    else:
        return fibonacci(n) + fibonacci_sum(n - 1)

def interactive_fibonacci():
    while True:
        print("Choose an option:")
        print("1. Get nth Fibonacci number")
        print("2. Get sum of Fibonacci sequence up to nth number")
        print("3. Exit")
        choice = input("Enter choice (1, 2, or 3): ")
        if choice == "3":
            print("Exiting...")
            break
        n = int(input("Enter the value of n: "))
        if choice == "1":
            print(f"The {n}th Fibonacci number is {fibonacci(n)}")
        elif choice == "2":
            print(f"The sum of Fibonacci sequence up to {n} is {fibonacci_sum(n)}")
        else:
            print("Invalid choice, please try again.")

interactive_fibonacci()


