# Python3 implementation of the approach
 
MAX = 10
 
# Function to return the maximum
# even number that can be formed
# with any number of digit swaps
 
 
def getMaxEven(string, length):
 
    string = list(string)
    print(string)
 
    # To store the frequencies of
    # all the digits
    freq = [0]*MAX
 
    # To store the minimum even digit
    # and the minimum overall digit
    minEvenDigit = MAX
    minDigit = MAX
    for i in range(length):
        digit = ord(string[i]) - ord('0')
        print("ord(string[i])", ord(string[i]))
        print("ord('0')", ord('0'))
        freq[digit] += 1

        print("string[{0}] = {1} and digit:{2} freq[{2}] = {3}".format(i, string[i], digit, freq[digit]))

        # If digit is even then update
        # the minimum even digit
        if (digit % 2 == 0):
            minEvenDigit = min(digit, minEvenDigit)
            print("minEventDigit ", minEvenDigit )
 
        # Update the overall minimum digit
        minDigit = min(digit, minDigit)
        print("minDigit " ,minDigit)
 
    # If there is no even digit then
    # it is not possible to generate
    # an even number with swaps
    if (minEvenDigit == MAX):
        return "-1"
 
    # Decrease the frequency of the
    # digits that need to be swapped
    freq[minEvenDigit] -= 1
    freq[minDigit] -= 1
    print("# Decrease the frequency of the # digits that need to be swapped")
    print("freq[minEvenDigit]{} freq[minDigit]{}".format(freq[minEvenDigit], freq[minDigit]))
 
    i = 0
 
    for a in range(len(freq)):
        print("freq[{}] = {}".format(a ,freq[a]))

    # Take every digit starting from the maximum
    # in order to maximize the number
    for j in range(MAX - 1, -1, -1):
        # print(j)
        # Take current digit number of times
        # it appeared in the original number
        for k in range(freq[j]):
            print("k",k)
            print("j",j)
            print("freq[j]", freq[j])
            string[i] = chr(j + ord('0'))
            print("chr(j + ord('0'))", chr(j + ord('0')))
            i += 1
 
        # If current digit equals to the
        # minimum even digit then one instance of it
        # needs to be swapped with the minimum overall digit
        # i.e. append the minimum digit here
        if (j == minEvenDigit):
            print("if j = minEvenDigit")
            string[i] = chr(minDigit + ord('0'))
            i += 1
 
    # Append once instance of the minimum
    # even digit in the end to make the number even
    #string.append(chr(minEvenDigit + ord('0')));
 
    return "".join(string)
 
 
# Driver code
if __name__ == "__main__":
    # string = "1023422"
    string = "135794"
    length = len(string)
 
    # Function call
    print(getMaxEven(string, length))
 
# This code is contributed by AnkitRai01