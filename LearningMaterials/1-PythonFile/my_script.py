#%%
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    :param n: A non-negative integer.
    :return: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#%%

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is: {factorial(number)}")
#%%

number = 5
print(f"The factorial of {number} is: {factorial(number)}")
# %%
