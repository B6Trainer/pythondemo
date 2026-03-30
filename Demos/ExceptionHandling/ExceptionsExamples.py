# ==============================
# EXCEPTION HANDLING - MAIN FILE
# ==============================

# 🔹 Example 1: Basic try-except
try:
    x = 10 / 0
except:
    print("Error occurred")


# 🔹 Example 2: Specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# 🔹 Example 3: Multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Divide by zero error")


# 🔹 Example 4: Multiple exceptions in one line
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Error occurred")


# 🔹 Example 5: else block
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)


# 🔹 Example 6: finally block
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup always runs")


# 🔹 Example 7: Getting error details
try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)


# 🔹 Example 8: Raising exception
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount


try:
    print(withdraw(1000, 1500))
except ValueError as e:
    print("Withdraw error:", e)


# 🔹 Example 9: Full flow example
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Execution complete")


# ==============================
# END OF FILE
# ==============================