from encodings import utf_8
import json
import re
import pymysql
#change path로 경로 지정, model명 변수로 받아와서 이름 입력받아 인식하게 변경.


def counect():
    conn = pymysql.connect(host='127.0.0.1', 
                           user='root', 
                           passwd='admin', 
                           db='testai', 
                           charset='utf8' )
    global cur
    cur = conn.cursor()
    return conn


def insert_json_label(conn):
    with open('path', encoding= 'utf-8') as json_file:
        json_line = json.load(json_file) # JSON의 Key값으로 접근
        label_name = json_line['label_id']
        output_file = json_line['outputFile']
        collected_file = json_line['collected File']
        argument = json_line['agument']
        tr_ratio = json_line['tr_ratio']
        flow_window_size = json_line['flow_window_size']
        flow_window_gap = json_line['flow_window_gap']
        threat_report = json_line['threat_report']
 
        sql = "insert into ai_label(label_name, output_file, collected_file, argument, tr_ratio, flow_window_size, flow_window_gap, threat_report)"
        sql += "values('"+label_name+"','"+output_file+"','"+collected_file+"','"+argument+"','"+tr_ratio+"','"+flow_window_size+"','"+flow_window_gap+"','"+threat_report+"')"
        
        sql_insert = sql.replace('\n', '')
        cur.execute(sql_insert)
        conn.commit()



def insert_json_preproecess(conn): 
    with open('path', encoding= 'utf-8') as json_file:
        json_line = json.load(json_file) # JSON의 Key값으로 접근
        # json_line = json_data # JSON 객체를 가지는 배열
        pre_name = json_line['pre_id']
        #label_id = json_line['Label_data']
        train_raw = json_line['Train_raw']
        test_raw = json_line['Test_raw']
        train_result = json_line['Train_result']
        test_result = json_line['Test_result']
        data_path = json_line['Data_path']
        # data_type = json_line['Data_Type']
        # network_type_feature = json_line['Network_type_feature']
        # http_feature = json_line['Http_feature']
        # flow_port_feature = json_line['Flow_port_feature']
        # flow_byte_pkt_feature = json_line['Flow_byte_pkt_feature']
        # flow_statistic_feature = json_line['Flow_statistic_feature']
        # gan_threat_extension = json_line['GAN_Threat_Extension']
        # create_time = json_line['create_time']
        
        sql = "insert into ai_preprocess(pre_name, train_raw, test_raw, train_result, test_result, data_path)"
        sql += "values('"+ pre_name+"','"+train_raw+"','"+test_raw+"','"+train_result+"','"+ test_result+"','"+data_path+"')"
        #sql += "values('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s')"
        
        sql_insert = sql.replace('\n','')
        cur.execute(sql_insert)
        conn.commit()
            
def insert_json_model(conn):
    with open('path', encoding= 'utf-8') as json_file:
        json_line = json.load(json_file) # JSON의 Key값으로 접근
        model_name = json_line['model_id']
        learning_file = json_line['learning_file']
        test_file = json_line['test_file']
        title = json_line['title']
        save_gh = json_line['save_gh']
        s_pos = json_line['s_pos']
        c_num = json_line['c_num']
        epochs = json_line['epochs']
        batch_size = json_line['batch_size']
        accuracy_threshold = json_line['accur_thres']
        data_path = json_line['Data_path']
        model_path = json_line['Model_path']
        
        sql = "insert into ai_model(model_name, learning_file, test_file, title, save_gh, s_pos, c_num, epochs, batch_size, accur_thres, data_path, model_path)"
        sql += "values('"+model_name+"','"+learning_file+"','"+test_file+"','"+title+"','"+save_gh+"',"
        sql += "'"+s_pos+"','"+c_num+"','"+epochs+"','"+batch_size+"','"+accuracy_threshold+"','"+data_path+"','"+model_path+"')" 
        
        sql_insert = sql.replace('\n','')
        cur.execute(sql_insert)
        conn.commit()
    pass


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
    cur.execute("select * from ai_preprocess where username = '"+username+"'")
    sql = "DELETE FROM ai_preprocess WHERE username = '"+username+"'"
    cur.execute(sql)
    conn.commit()

def selecting_number(conn):
    choice = int(input('1 : 전체 조회\n'
                       '2 : 조건 검색\n'
                        '3 : 삽입\n'
                        '4 : 삭제\n'
                        '5 : Label_json삽입\n'
                        '6 : Preprocess_json삽입\n'
                        '7 : Model_json삽입\n' 
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
    elif choice == 5:
        insert_json_label(conn)
    elif choice == 6:
        insert_json_preproecess(conn)
    elif choice == 7:
        insert_json_model(conn)
    elif choice == 9:
        print('disconect...')
        conn.close()
        exit()
    else:
        print(f'Wrong Number : {choice}')
   
def main():
    conn = counect()
    while True:
       selecting_number(conn)
    
if __name__ =="__main__":
    main()
