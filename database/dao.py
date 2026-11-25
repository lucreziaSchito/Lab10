from database.DB_connect import DBConnect
from model.filiale import Filiale
from model.bonifico import Bonifico

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def read_all_filiali():
        conn = DBConnect.get_connection()
        result = {}
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT * FROM filiale")
                for row in cursor:
                    filiale = Filiale(**row)
                    result[filiale.id] = filiale
            finally:
                cursor.close()
        finally:
            conn.close()
        return result

    @staticmethod
    def read_all_bonifici():
        conn = DBConnect.get_connection()
        result = {}
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT * FROM bonifico")
                for row in cursor:
                    bonifico = Bonifico(**row)
                    result[bonifico.id] = bonifico
            finally:
                cursor.close()
        finally:
            conn.close()
        return result