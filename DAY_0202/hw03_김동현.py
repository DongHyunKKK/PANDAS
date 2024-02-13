import pymysql
import pandas as pd
import numpy as np

# user_table 생성
def create_table(conn, cur):
    try:
        query1 = 'drop table if exists user_table'
        query2 = """
            create table user_table
            (userID char(8),
            userName varchar(10),
            birthYear int,
            addr char(2),
            mobile1 char(3),
            mobile2 char(8),
            height smallint,
            mDate date,
            CONSTRAINT pk_user_table primary key (userID))
        """
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성 완료')
    
    except Exception as e:
        print(e)

def main():
    # 데이터베이스(shoppingmall) 연결
    conn = pymysql.connect(host = 'localhost',
                           user = 'root', password = '2357',
                           db = 'shoppingmall', charset = 'utf8')
    
    # cursor 객체 생성
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_table(conn, cur)

    # 연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')

main()

conn = pymysql.connect(host = 'localhost',
                           user = 'root', password = '2357',
                           db = 'shoppingmall', charset = 'utf8')

curs = conn.cursor()
sql = """insert into user_table(userID, userName, birthYear, addr, mobile1, mobile2, height, mDate)
            values (%s, %s, %s, %s, %s, %s, %s, %s)"""

curs.execute(sql, ('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'))
curs.execute(sql, ('KJD', '김제동', 1974, '경남', None, None, 173, '2013-03-03'))
curs.execute(sql, ('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'))
curs.execute(sql, ('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'))
curs.execute(sql, ('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'))
curs.execute(sql, ('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'))
curs.execute(sql, ('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'))
curs.execute(sql, ('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'))
curs.execute(sql, ('SDY', '신동엽', 1971, '경기', None, None, 176, '2008-10-10'))
curs.execute(sql, ('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08'))

conn.commit()
print('INSERT 완료')

curs.close()
conn.close()

# buy_table 생성
def create_table(conn, cur):
    try:
        query1 = 'drop table if exists buy_table'
        query2 = """
            create table buy_table
            (num int,
            userID char(8),
            prodName char(6),
            groupName char(4),
            price int,
            amount smallint,
            CONSTRAINT pk_buy_table primary key(num),
            foreign key(userID) references user_table(userID))
        """
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성 완료')
    
    except Exception as e:
        print(e)

def main():
    # 데이터베이스(shoppingmall) 연결
    conn = pymysql.connect(host = 'localhost',
                           user = 'root', password = '2357',
                           db = 'shoppingmall', charset = 'utf8')
    
    # cursor 객체 생성
    cur = conn.cursor()

    # 테이블 생성 함수 호출
    create_table(conn, cur)

    # 연결 종료
    cur.close()
    conn.close()
    print('Database 연결 종료')

main()

conn = pymysql.connect(host = 'localhost',
                           user = 'root', password = '2357',
                           db = 'shoppingmall', charset = 'utf8')

curs = conn.cursor()
sql = """insert into buy_table(num, userID, prodName, groupName, price, amount)
            values (%s, %s, %s, %s, %s, %s)"""

curs.execute(sql, (1, 'KHD', '운동화', None, 30, 2))
curs.execute(sql, (2, 'KHD', '노트북', '전자', 1000, 1))
curs.execute(sql, (3, 'KYM', '모니터', '전자', 200, 1))
curs.execute(sql, (4, 'PSH', '모니터', '전자', 200, 5))
curs.execute(sql, (5, 'KHD', '청바지', '의류', 50, 3))
curs.execute(sql, (6, 'PSH', '메모리', '전자', 80, 10))
curs.execute(sql, (7, 'KJD', '책', '서적', 15, 5))
curs.execute(sql, (8, 'LHJ', '책', '서적', 15, 2))
curs.execute(sql, (9, 'LHJ', '청바지', '의류', 50, 1))
curs.execute(sql, (10, 'PSH', '운동화', None, 30, 2))
curs.execute(sql, (11, 'LHJ', '책', '서적', 15, 1))
curs.execute(sql, (12, 'PSH', '운동화', None, 30, 2))

conn.commit()
print('INSERT 완료')

curs.close()
conn.close()


# python 실행 결과
conn = pymysql.connect(host = 'localhost', user = 'root', password = '2357',
                       db = 'shoppingmall', charset = 'utf8')

cur = conn.cursor()
query = """
select userName, prodName, addr, concat(mobile1, mobile2) as 연락처
from buy_table as b
	inner join user_table as u
	on b.userID = u.userID"""

print('문제 1번')
print('-' * 42)
print(f" {'userName'} {'prodName'}   {'addr'}       {'연락처'}")
print('-' * 42)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

conn = pymysql.connect(host = 'localhost', user = 'root', password = '2357',
                       db = 'shoppingmall', charset = 'utf8')

cur = conn.cursor()
query = """
select distinct b.userID, userName, prodName, addr, concat(u.mobile1, u.mobile2)
from buy_table as b
	inner join user_table as u
	on u.userID = b.userID
where b.userID = 'KYM'"""

print('문제 2번')
print('-' * 50)
print(f" {'userID'} {'userName'} {'prodName'}   {'addr'}      {'연락처'}")
print('-' * 50)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

conn = pymysql.connect(host = 'localhost', user = 'root', password = '2357',
                       db = 'shoppingmall', charset = 'utf8')

cur = conn.cursor()
query = """
select b.userID, userName, prodName, addr, concat(u.mobile1, u.mobile2)
from buy_table as b
	inner join user_table as u
	on u.userID = b.userID
order by b.userID"""

print('문제 3번')
print('-' * 50)
print(f"{'userID'}  {'userName'}  {'prodName'}  {'addr'}      {'연락처'}")
print('-' * 50)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)
query = """
select b.userID, userName, prodName, addr, concat(u.mobile1, u.mobile2)
from buy_table as b
	inner join user_table as u
	on u.userID = b.userID
order by b.userID"""

print('문제 3번')
print('-' * 50)
print(f"{'userID'}  {'userName'}  {'prodName'}  {'addr'}      {'연락처'}")
print('-' * 50)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

conn = pymysql.connect(host = 'localhost', user = 'root', password = '2357',
                       db = 'shoppingmall', charset = 'utf8')

cur = conn.cursor()
query = """
select distinct b.userID, userName, addr
from buy_table as b
	inner join user_table as u
	on u.userID = b.userID
order by b.userID"""

print('문제 4번')
print('-' * 25)
print(f"{'userID'}  {'userName'}   {'addr'}")
print('-' * 25)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

conn = pymysql.connect(host = 'localhost', user = 'root', password = '2357',
                       db = 'shoppingmall', charset = 'utf8')

cur = conn.cursor()
query = """
select b.userID, userName, addr, concat(u.mobile1, u.mobile2) as 연락
from buy_table as b
	inner join user_table as u
	on u.userID = b.userID
where addr in ('경북', '경남')
order by b.userID"""

print('문제 5번')
print('-' * 40)
print(f"{'userID'}  {'userName'}   {'addr'}      {'연락처'}")
print('-' * 40)

cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()