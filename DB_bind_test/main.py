import pymysql

def counect():
    conn = pymysql.connect(host='0.0.0.0', 
                           user='root', 
                           passwd='root', 
                           db='test', 
                           charset='utf8' )
    global cur
    cur = conn.cursor()
    return conn

# def create_table():
#     print("생성할 테이블 을 정의 하세요"
#           "종료 하시려면 ; 를 입력하세요")
#     global input_data
#     collected_String = ''
#     count = 0
#     while True:
#         input_data = input()
#         collected_String = collected_String + ' ' + input_data
#         count += 1
#         if input_data == ';': 
#             break
#     #print(collected_String.split(','), end = '\n')
#     # for a in range(count):
#     #     print(input_data)
#     #cur.execute(sql)
#     #conn.commit()

def search_data():
    # cur = conn.cursor()
    sql = 'select * from equipment'
    cur.execute(sql)
    result = cur.fetchall()
    # print(result)
    for results in result:
        print(results)

def option_search():
    option = input("검색할 조건 입력")
    sql = 'select * from ai_label where username = "'+option+'"'
    cur.execute(sql)
    result = cur.fetchall()
    for results in result:
        print(results)

def insert_data(conn):
    # cur = conn.cursor()
    # username = input('사용자 명 정의')
    # userid = input('사용자 ID 정의')
    # userpw = input('사용자 PW 정의')
    username, userid, userpw = input('사용자 명 정의\n'
                                     '사용자 ID 정의\n'
                                     '사용자 PW 정의\n').split()
    sql = "INSERT INTO testman(username, userid, userpw) VALUES('"+username+"', '"+userid+"', '"+userpw+"')"
    cur.execute(sql)
    conn.commit()

def delete_data(conn):
    # cur = conn.cursor()
    username = input('삭제할 사용자 명 정의')
    cur.execute("select * from testman where username = '"+username+"'")
    sql = "DELETE FROM testman WHERE username = '"+username+"'"
    cur.execute(sql)
    conn.commit()

def selecting_number(conn):
    choice = int(input('1 : 전체 조회\n'
                       '2 : 조건 검색\n'
                        '3 : 삽입\n'
                        '4 : 삭제\n'
                        '9 : 종료\n'
                         ': '))
    if choice == 1:
        search_data()
    elif choice == 2:
        option_search()
    elif choice == 3: 
        insert_data(conn)
    elif choice == 4:
        delete_data(conn)
    elif choice == 9:
        print('disconect...')
        conn.close()
        exit()
    else:
        print(f'Wrong Number : {choice}')
   
def main():
    conn = counect()
    # print('conect start...')
    # choice = int(input('1 : 전체 조회\n'
    #                '2 : 삽입\n'
    #                '3 : 삭제\n'
    #                ': '))
    # if choice == 1:
    #     search_data(conn)
    # elif choice == 2: 
    #     insert_data(conn)
    # elif choice == 3:
    #     delete_data(conn)
    # else:
    #     return print(f'Wrong Number : {choice}')
    while True:
       selecting_number(conn)
    
if __name__ =="__main__":
    main()
