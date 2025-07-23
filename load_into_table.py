import psycopg2
from environment_manager import *



def load_data(data):
    conn = psycopg2.connect(f"dbname={db} user={db_user} password={db_password}")
    cur = conn.cursor()

    for i in range(len(data)):

        vector_embedding = model.embed_query(data[i])
        data[i] = data[i].replace("\'", "\'\'")
        sql_string = f"INSERT INTO {table} (embedding, reference) VALUES (\'{vector_embedding}\', \'{data[i]}\')"
        try:
            cur.execute(sql_string)
        except:
            print(f"query \'{data[i]}\' failed to be loaded into db")

    conn.commit()
    cur.close()
    conn.close()



