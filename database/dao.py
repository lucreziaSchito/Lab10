from database.DB_connect import DBConnect

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def read_banca():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT * FROM banca")
                result = []
                for row in cursor:
                    result.append(row)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()