from datetime import datetime
from collections import defaultdict


def log_call(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a") as file:
            file.write(
                f"{timestamp} | {func.__name__} | "
                f"args={args}, kwargs={kwargs}\n"
            )

        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name):
    print(f"Hello, {name}!")


@log_call
def multiply(a, b):
    return a * b


def read_logs():
    counts = defaultdict(int)

    try:
        with open("log.txt", "r") as file:
            for line in file:
                parts = line.split("|")
                if len(parts) >= 2:
                    func_name = parts[1].strip()
                    counts[func_name] += 1

        print("\nFunction Call Counts:")
        for func, count in counts.items():
            print(f"{func}: {count}")

    except FileNotFoundError:
        print("log.txt not found.")


# Function calls
add(10, 20)
add(5, 7)

greet("sara")
greet("alan")

multiply(3, 4)
multiply(6, 8)
multiply(2, 5)

# Analyze logs
read_logs()