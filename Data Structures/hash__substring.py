# python3

# Task: In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern in the given text
# Input Format: There are two strings in the input: the pattern P and the text T.
# Constraints: 1 ≤ length of pattern ≤ length of Text ≤ 5·10**5. The total length of all occurrences of P in T doesn’t exceed 108.
# The pattern and the text contain only latin letters
# Output Format: Print all the positions of the occurrences of P in T in the ascending order.
# Use 0-based indexing of positions in the the text T.
# Memory Limit: 512MB.
# Sample 1: Input: aba abacaba
#           Output: 0 4
# Explanation: The pattern aba can be found in positions 0 (abacaba) and 4 (abacaba) of the text abacaba.
# Sample 2: Input: Test testTesttesT
#           Output: 4
# Explanation: Pattern and text are case-sensitive in this problem.
# Pattern Test can only be found in position 4 in the text testTesttesT.
# Sample 3: Input: aaaaa baaaaaaa
#           Output: 1 2 3
# Note that the occurrences of the pattern in the text can be overlapping, and that’s ok, you still need to output all of them.
# It is clear that the algorithm should use function that checks similarity between two patterns as rare as possible,
# and the idea is to use precomputed hash values of the string, the example of that is provided below PolyHash function


from random import randint
import sympy


class prepare_for_RabinKarp:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.text_length = len(text)
        self.pattern_length = len(pattern)
    def generate_prime_number(self): # generation of a big prime number
        return sympy.nextprime(self.text_length*1000000000000)
    def generate_x(self, prime_number):
        return randint(1, prime_number-1)
    def PolyHash(self, string, prime_number, x): # Function to hash pattern occurence using polynomial hashing
        hash = 0
        for i in range(len(string)-1, -1, -1):
            hash = (hash*x + ord(string[i])) % prime_number # in this project every substring is assigned a value of ASCII code
        return hash
    # Suppose we have text 'abcbd' and pattern length = 3.
    # Hashing the strings will be done from the end of the text to the front.
    # Assign a unique value to each character: lets suppose for character 'a' the value 0 is assigned, for 'b' = 1, for 'c' = 2 and
    # for 'd' = 3. Then hash substrings of pattern length: h('cbd') = (2 + x + 3x**2) modulo prime number.
    # Explanation: Multiply each hash value of a character by x to the power of it's corresponding positing starting from zero
    # And now to compute the next hash value we do not necessarily need to compute it again, because the next substring is 'bcb'
    # Since we already know the coefficients of it's last (pattern_length - 1) elements, we can assign them directly multiplying by x to
    # the corresponding power
    # Example: h('cbd') = (2 + x + 3x**2) mod prime_number, h('cbd') = (2 + x + 3x**2) mod prime_number
    #                      |                                                |
    #                      ------                                           ------
    #                           |                                                |
    #          h('bcb') = (1 + 2x + x**2) mod prime_number, h('bcb') = (1 + 2x + x**2) mod prime_number
    # The following function does that
    def Precompute_Hashes(self, prime_number, x):
        hash_array = [None]*(self.text_length - self.pattern_length + 1)
        string = text[self.text_length - self.pattern_length: self.text_length]
        hash_array[self.text_length - self.pattern_length] = self.PolyHash(string, prime_number, x)
        y = 1
        for i in range(1, self.pattern_length+1):
            y = (y * x) % prime_number
        for i in range(self.text_length - self.pattern_length - 1, -1, -1):
            hash_array[i] = (x*hash_array[i+1] + ord(text[i]) - y*ord(text[i+self.pattern_length])) % prime_number
        return hash_array
    def AreEqual(self, string, pattern):
        if string == pattern:
            return True
        return False

def RabinKarp(text, pattern):
    processor = prepare_for_RabinKarp(text, pattern)
    prime_number = processor.generate_prime_number()
    x = processor.generate_x(prime_number)
    result = []
    pHash = processor.PolyHash(pattern, prime_number, x)
    hash_array = processor.Precompute_Hashes(prime_number, x)
    for i in range(0, processor.text_length - processor.pattern_length + 1):
        if pHash != hash_array[i]:
            continue
        if processor.AreEqual(text[i:i + processor.pattern_length], pattern):
            result.append(i)
    return result


if __name__ == '__main__':
    pattern, text = input().rstrip(), input().rstrip()
    result = RabinKarp(text, pattern)
    # for i in result:
    #     print(i)
    print(len(result))

# The running time of functions: Precompute_Hashes: O(length of text + length of pattern)
#                                PolyHash(pattern): O(length of pattern)
#                                Total time spent in AreEqual: O(q * length of pattern), where q is the number of occurences of pattern in the text
#                                Average running time: O(length of text + (q + 1) * length of pattern), usually q is small, therefore
#                                this takes much less time than O(length of text * length of pattern)
#                                Worst case scenario: O(length of text * length of pattern) happens when function AreEqual is called over
#                                and over again. Example: Text = AAAAAAAA, pattern = AAA.