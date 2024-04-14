class EuclideanAlgorithm:
    def gcd(self, a, b):
        # Base case: if b is zero, return a
        if b == 0:
            return a
        else:
            # Otherwise, recursively call gcd with b as the new first number
            # and remainder of a divided by b as the new second number
            return self.gcd(b, a % b)


if __name__ == "__main__":
    # Create an instance of the EuclideanAlgorithm class
    euclidean_algo = EuclideanAlgorithm()

    try:
        # Get user input for the first number
        num1 = int(input("Enter first number: "))
        # Get user input for the second number
        num2 = int(input("Enter second number: "))
        # Calculate the GCD using the gcd method of EuclideanAlgorithm
        result = euclidean_algo.gcd(num1, num2)
        # Print the result
        print("GCD is:", result)
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter valid integers.")
