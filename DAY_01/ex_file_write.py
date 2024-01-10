# -----------------------------------------------------------------
# 파일 입출력 => 출력 즉, 쓰기(write)
# - 사용 내장 함수 : open(file, mode = 'w', encoding = '지정')
# -----------------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 지운다.
# file = open(filename, mode = 'w', encoding = 'utf-8')

# (1) open => 쓰기(a : append) 모드의 경우 파일이 없으면 생성, 있으면 마지막에 추가한다.
file = open(filename, mode = 'a', encoding = 'utf-8')

# (2) write
file.write('12345678\n')
file.write('''Ha Ha Ha
aaa
111111''')

file.writelines(['a\n', 'b\n', '1111\n', '2222\n'])

# (3) close
file.close()