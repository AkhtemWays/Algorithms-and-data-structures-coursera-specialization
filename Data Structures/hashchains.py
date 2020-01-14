# python3

# Problem description: In this task your goal is to implement a hash table with lists chaining.
# You are already given the number of buckets m and the hash function. It is a polynomial hash function
# prime number and x are fixed.
#  Your program should support the following kinds of queries:
#  add string — insert string into the table. If there is already such string in the hash table, then just ignore the query.
#  del string — remove string from the table. If there is no such string in the hash table, then just ignore the query.
#  find string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.
#  check i — output the content of the i-th list in the table. Use spaces to separate the elements of the list.
#  If i-th list is empty, output a blank line.
# Input Format. There is a single integer m in the first line — the number of buckets you should have.
# The next line contains the number of queries N. It’s followed by N lines, each of them contains one query in the format
# described above.
# Constraints. 1 ≤ N ≤ 105; N 5 ≤ m ≤ N. All the strings consist of latin letters. Each of them is non-emptyand has length at most 15
# Output Format. Print the result of each of the find and check queries,
# one result per line, in the same order as these queries are given in the input
# Memory Limit: 512MB
# Sample 1: Input: 5
#                  12
#                  add world
#                  add HellO
#                  check 4
#                  find World
#                  find world
#                  del world
#                  check 4
#                  del HellO
#                  add luck
#                  add GooD
#                  check 2
#                  del good
#                  Output:
#                  HellO world
#                  no
#                  yes
#                  HellO
#                  GooD luck
# Sample 2: Input: 4
#                  8
#                  add test
#                  add test
#                  find test
#                  del test
#                  find test
#                  find Test
#                  add Test
#                  find Test
#                  Output:
#                  yes
#                  no
#                  no
#                  yes



class chain_hasher:
    x = 263
    prime_number = 1000000007
    def __init__(self, cardinality):
        self.cardinality = cardinality # number of chains
        self.hash_table = []
    def make_chain(self): # hash table initialization
        for i in range(self.cardinality):
            self.hash_table.append([])
        return self.hash_table
    def append(self, string): # append when there is no string in the table, otherwise just skip this step
        index_to_add_at = self.PolyHash(string) # firstly calculation of the chain the string should be in in order to increase
        for i in self.hash_table[index_to_add_at]: # the running time
            if i == string:
                return
        self.hash_table[index_to_add_at].append(string)

    def PolyHash(self, string): # the function that assigns unique key to each query using the following polynomial expression
        ans = 0
        for i in reversed(string):
            ans = (ans*self.x + ord(i)) % self.prime_number
        index_of_chain = ans % self.cardinality
        return index_of_chain
    def print_constructed_chain(self, chain_number): # print blank line if the chain is empty, otherwise reversed chain
        if len(self.hash_table[chain_number]) == 0:
            print(' ')
        print(" ".join(self.hash_table[chain_number][::-1]))
    def delete_string(self, string): # firstly find the chain, if the string is inside it delete it, otherwise ignore
        index_of_chain = self.PolyHash(string)
        for i in self.hash_table[index_of_chain]:
            if i == string:
                self.hash_table[index_of_chain].remove(string)
    def find(self, string):
        index_to_check_at = self.PolyHash(string)
        for i in self.hash_table[index_to_check_at]:
            if i == string:
                print('yes')
                return
        print('no')



def process():
    m = int(input())
    num_of_queries = int(input())
    queries = [input() for i in range(num_of_queries)]
    processor = chain_hasher(m)
    processor.make_chain()
    for query in queries:
        query = query.split()
        if query[0] == 'add':
            processor.append(query[1])
        elif query[0] == 'check':
            processor.print_constructed_chain(int(query[1]))
        elif query[0] == 'del':
            processor.delete_string(query[1])
        else:
            processor.find(query[1])


if __name__ == '__main__':
    process()