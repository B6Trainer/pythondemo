# ==============================
# CUSTOM EXCEPTION FILE
# ==============================

class MyError(Exception):
    pass


# Example usage
def check_value(x):
    if x < 0:
        raise MyError("Negative value not allowed")
    return x


try:
    print(check_value(-5))
except MyError as e:
    print("Custom Exception:", e)


# ==============================
# END OF FILE
# ==============================