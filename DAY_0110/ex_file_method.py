# -----------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -----------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode = 'r', encoding = 'utf8') as f:
    f.seek(5)
    print(f.read(30))
    print(f'현재 위치 : {f.tell()}')
    print(f.name, f.closed)
    f.seek(0)
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')

print(f.name, f.closed)