def convertInt(numStr):
    convertInt = int(numStr)
    return convertInt

def calculate_sum(numOneStr, numTwoStr):
    numOneInt = convertInt(numOneStr)
    numTwoInt = convertInt(numTwoStr)
    result = numOneInt + numTwoInt
    return result

numOne = input("Enter the first number: ")
numTwo = input("Enter the second number: ")

answer = calculate_sum(numOne, numTwo)

print("Ans = " + str(answer))
