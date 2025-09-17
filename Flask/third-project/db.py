import pymysql as mysql
DB_HOST='localhost'
DB_USER="root"
DB_PASS="root@123"
DB_NAME='myflask'

def get_connection(db=None):
    return mysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=db,
        cursorclass=mysql.cursors.DictCursor
        )

def init_db():
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except Exception as e:
        print("Error :",e)
    finally:
        conn.close()
    
    conn=get_connection(DB_NAME)
    try:
        with conn.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS STUDENTS(
                    SID INT AUTO_INCREMENT PRIMARY KEY,
                    SFULL_NAME VARCHAR(100) NOT NULL,
                    SEMAIL VARCHAR(50) UNIQUE NOT NULL,
                    SPASS VARCHAR(20) NOT NULL);
                ''')
        conn.commit()

    except Exception as e:
        print("Error :",e)
    finally:
        conn.close()
