import psycopg2
from environment_manager import *


def compare_with_table(query: str, limit: int) -> list[tuple[any,...]]:
    """compares query string to db to find the (limit) closest entries

    returns the output of fetchall(): a list of tuples, where each tuple represents an entry in the db, sorted by symantic proximity to the query string
    """
    conn = psycopg2.connect(f"dbname={db} user={db_user} password={db_password}")
    cur = conn.cursor()

    vector_embedding = model.embed_query(query)

    sql_string = f"SELECT id, reference FROM {table} ORDER BY embedding {dist_function} \'{vector_embedding}\' LIMIT {limit}"

    cur.execute(sql_string)
    result = cur.fetchall()
    cur.close()
    conn.close()

    return result