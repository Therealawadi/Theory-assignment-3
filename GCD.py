def gcd(a, b):
    # If b is zero, return a as GCD
    if b == 0:
        return a
    else:
        # Otherwise, recursively call gcd with b as the new first number
        # and remainder of a divided by b as the new second number
        return gcd(b, a % b)

# Example usage:
# Find the GCD of 48 and 18
result = gcd(48, 18)
# Print the result
print("GCD is:", result)
