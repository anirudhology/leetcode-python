class MultiplyStrings:
    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        # Special case
        if num1 == '0' or num2 == '0':
            return '0'
        # Lengths of two strings
        m, n = len(num1), len(num2)
        # List to store the products
        products = [0] * (m + n - 1)
        # Process the strings
        for i in range(m):
            for j in range(n):
                products[i + j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        # Process the products array further
        for i in range(len(products) - 1, 0, -1):
            products[i - 1] += products[i] // 10
            products[i] %= 10
        # String for the final result
        output = ''
        for i in products:
            output += str(i)
        return output
