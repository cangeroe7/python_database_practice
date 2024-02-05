import psycopg2
from config import config

def get_parts(vendor_id):
    conn = None
    try:

        params = config()

        conn = psycopg2.connect(**params)

        curr = conn.cursor()

        curr.callproc('get_parts_by_vendors', (vendor_id,))

        row = curr.fetchone()
        while row:
            print(row)
            row = curr.fetchone()

        curr.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_parts(1)