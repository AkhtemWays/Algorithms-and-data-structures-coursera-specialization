# python3


# Problem description: To implement a simple phone book manager with the following types of
# user queries: adding the number to the book, deleting the number from the book, find the name by number.
# Input Format. There is a single integer N in the first line — the number of queries.
# It’s followed by N lines, each of them contains one query in the format described above
# Constraints: 1 ≤ N ≤ 10
# Output Format.
# Print the result of each find query — the name corresponding to the phone number or “not found" (without quotes)
# if there is no person in the phone book with such phone number.
# Output one result per line in the same order as the find queries are given in the input

class Phone_book:
    def __init__(self):
        self.phone_book = [None] * 10**5 # initialization according to constraints
    def add_number(self, number, name):
        self.phone_book[number] = name
    def delete_number(self, number):
        if self.phone_book[number] != None:
            self.phone_book[number] = None
    def find(self, number):
        if self.phone_book[number] != None:
            print(self.phone_book[number])
        else:
            print('not found')

def process_queries():
    N = int(input())
    queries = [input() for i in range(N)]
    phone_book = Phone_book()
    for query in queries:
        query = query.split()
        fun_type = query[0]
        number = int(query[1])
        if fun_type == 'add':
            phone_book.add_number(number, query[2])
        elif fun_type == 'del':
            phone_book.delete_number(number)
        else:
            phone_book.find(number)
if __name__ == '__main__':
    process_queries()




