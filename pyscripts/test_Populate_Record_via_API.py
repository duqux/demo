from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def insert_userinfo(userinfo):
    global cursor, conn
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


# User Story 1
def test_tc001():
    userinfo = [('TS100', 'Jun', 'M', '4000', '10061996', '10')]
    insert_userinfo(userinfo)


# User Story 2
def test_tc002():
    userinfo = [('TS101', 'Vernon', 'M', '3000', '18021998', '8'),
                ('TS102', 'Minghao', 'M', '7000', '07111997', '20'),
                ('TS103', 'Joshua', 'M', '2000', '30121995', '5')]
    insert_userinfo(userinfo)


def test_tc003():
    userinfo = [('TS100', 'Jun', 'M', '4000', '10061996', '10')]
    insert_userinfo(userinfo)


if __name__ == '__main__':
    test_tc001()
    test_tc002()
    test_tc003()
