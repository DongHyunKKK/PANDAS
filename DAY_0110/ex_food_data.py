# file = 'food.txt'
#
# kor_food, china_food = [], []
# kind = ''
# with open(file, mode = 'r', encoding = 'utf8') as f:
#     data = f.readline()
#     if not data.index('*'):
#         kind = '한식' if data[1:] == '한식' else '중식'
#     else:
#         if kind == '한식': kor_food.append(data)
#         else:
#             china_food.append(data)
#
file = 'food.txt'
foods = {}
with open(file, mode = 'r', encoding = 'utf8') as f:
    line = None
    while line != '':  # 중간에 내용 없는 줄은 ''이 아니라 '\n'이므로 while문이 수행된다.
        line = f.readline()
        if line.find('*') != 0:
            if line != '\n' and len(line) != 0:  # len('\n') = 1
                foods[key].append(line.strip('\n'))
        else:
            key = line[1:].strip('\n')
            foods[key] = []

print(foods)
# file = 'food.txt'
# with open(file, mode = 'r', encoding = 'utf8') as f:
#     line = None
#     while line != '':
#         line = f.readline()
#         if line == '\n':
#             print(line)
# file = './food.txt'
# with open(file, mode = 'r', encoding = 'utf8') as f:
#     line = None
#     while line != '':  # 중간에 내용 없는 줄은 ''이 아니라 '\n'이므로 while문이 수행된다.
#         line = f.readline()
#         print(line.strip('\n'))
# data = {}
# key = ''
# for msg in datas:
#     if not msg.find('*'):
#         key = msg[1:]
#         data[key] = []
#     else:
#         print(data[key].append(msg[:-1]))
#
# print(data)
