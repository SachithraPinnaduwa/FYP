def multiply(num1, num2):
    # Convert the input strings to lists of integers
    num1 = [int(digit) for digit in num1]
    num2 = [int(digit) for digit in num2]

    # Reverse the lists to start from the least significant digit
    num1.reverse()
    num2.reverse()

    # Initialize a result list with zeros
    result = [0] * (len(num1) + len(num2))

    # Multiply the digits of num1 with the digits of num2
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Reverse the result list to get the final product
    result.reverse()

    # Convert the result list back to a string
    result = ''.join(map(str, result))

    return result