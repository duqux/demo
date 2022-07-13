from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_userinfo(userinfo):
    query = "INSERT INTO userinfo(natid,name,gender,salary,birthday,tax) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, userinfo)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    userinfo = [('TS100', 'Jun', 'M','4000','10061996','10'),
             ('TS101', 'Minghao', 'M','7000','07111997','20')]
    insert_userinfo(userinfo)

if __name__ == '__main__':
    main()