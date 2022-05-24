

class DatabaseController:

    def _add(self, conn, cursor, query):
        cursor.execute(query)
        conn.commit()

    def _get(self, conn, cursor, query):
        cursor.execute(query)
        return cursor.fetchall()


