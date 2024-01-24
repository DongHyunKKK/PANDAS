# -----------------------------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성 하기
# - 예) message.txt ====> message_copy.txt
# -----------------------------------------------------------------
filename = 'message.txt'

# 원본 파일에 내용 읽은 후 저장
with open(filename, mode = 'r', encoding = 'utf8') as f:
    data = f.read()

# 복사본 파일에 내용 쓰기
with open('message_copy.txt', mode ='w', encoding ='utf8') as f:
    f.write(data)

# 원본 파일에 내용 읽은 후 저장
with open(filename, mode = 'r', encoding = 'utf8') as of:
    with open('message_copy.txt', mode='w', encoding='utf8') as nf:
        nf.write(of.read())