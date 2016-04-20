
# records = [
#     ('foo', 1,2),
#     ('bar', 'hello'),
#     ('foo', 3,4)
# ]

# def do_foo(x, y):
#     print('foo', x, y)

# def do_bar(s):
#     print('bar', s)


# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

# #---------------------------------------------------------------------------------------------

# from collections import deque

# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             # return main function if pattern is matched
#             yield line, previous_lines
#         previous_lines.append(line)


# if __name__ == '__main__':
#     with open('test.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             # print previous lines
#             for pline in prevlines:
#                 print(pline, end='')
#             # print current line
#             print(line, end='')
#             # print 20 '-' for separate
#             print('-'*20)

#---------------------------------------------------------------------------------------------

# from collections import defaultdict

# d = defaultdict(list)

# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)

# print(list(d.items()))

#---------------------------------------------------------------------------------------------


# from collections import OrderedDict

# d1 = dict()

# d1['foo'] = 1
# d1['bar'] = 2
# d1['spam'] = 3
# d1['grok'] = 4

# print(d1)


# d2 = OrderedDict()

# d2['foo'] = 1
# d2['bar'] = 2
# d2['spam'] = 3
# d2['grok'] = 4

# print(d2)


#---------------------------------------------------------------------------------------------


# prices =      {
    
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM' : 205.55,
#     'HPQ' : 37.2,
#     'FB'  : 10.75
# }

# min_price = min(zip(prices.values(), prices.keys()))
# print(min_price)

# max_price = max(zip(prices.values(), prices.keys()))
# print(max_price)

# prices_sorted = sorted(zip(prices.values(), prices.keys()))
# print(prices_sorted)

#---------------------------------------------------------------------------------------------

# a =       {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }

# b =       {
#     'w': 10,
#     'x': 3,
#     'y': 2
# }


# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())

#---------------------------------------------------------------------------------------------

# items = [0,1,2,3,5,7,8,9]

# a = slice(2,4)
# print(items[a]) # [2,3]

# items[a] = [10, 11]
# print(items) #[0,1,10,11,5,7,8,9]

# del items[a]
# print(items) #[0,1,5,7,8,9]

#---------------------------------------------------------------------------------------------

# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]

# from collections import Counter

# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)

#---------------------------------------------------------------------------------------------

# from operator import itemgetter

# rows = [
#       {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#       {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#       {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#       {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]

# row_by_fname = sorted(rows, key=itemgetter('fname'))
# print(row_by_fname)
# row_by_lname = sorted(rows, key=itemgetter('lname'))
# print(row_by_lname)


# row_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
# print(row_by_lfname)

# print(min(rows, key=itemgetter('uid')))
# print(max(rows, key=itemgetter('uid')))

#---------------------------------------------------------------------------------------------

# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def __repr__(self):
#         return 'User( {})'.format(self.user_id)


# users = [User(23), User(1), User(99)]
# print(users)

# print(users[0])

#---------------------------------------------------------------------------------------------

# from operator import itemgetter
# from itertools import groupby

# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]


# rows.sort(key=itemgetter('date'))

# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print('    ', i)

# print(groupby(rows, key=itemgetter('date')))


#---------------------------------------------------------------------------------------------

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

new_prices = {key:value for key, value in prices.items() if value > 200}
tech_stock = {'AAPL', 'FB', 'IBM', 'MSFT'}
new_prices2 = {key:value for key, value in prices.items() if key in tech_stock}

print(new_prices2)