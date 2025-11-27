from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_tratte():
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Error di connessione con il database")
            return None
        cursor=cnx.cursor()
        #query che trova id degli hub usando least e greatest per creare adirezionalità,il valore totale delle merci con sum e il numero di spedizioni con count
        query="""SELECT
                 LEAST(s.id_hub_origine, s.id_hub_destinazione) AS hub_a,
                 GREATEST(s.id_hub_origine, s.id_hub_destinazione) AS hub_b,
                 COUNT(*) AS numero_spedizioni,
                 AVG(s.valore_merce) AS valore_medio
                 FROM spedizione s
                 WHERE s.id_hub_origine IS NOT NULL
                 AND s.id_hub_destinazione IS NOT NULL
                 GROUP BY
                 LEAST(s.id_hub_origine, s.id_hub_destinazione),
                 GREATEST(s.id_hub_origine, s.id_hub_destinazione);;;"""
        try:
            cursor.execute(query)
            rows = cursor.fetchall()  # ottieni tutte le righe

            tratte = []
            for row in rows:
                tratta = Tratta(hub_a=row[0], hub_b=row[1], valore=row[3],numero_spedizioni=row[2])
                tratte.append(tratta)

            return tratte

        finally:
            cursor.close()
            cnx.close()



    @staticmethod
    def get_hub():
        cnx=DBConnect.get_connection()
        if cnx is None:
            print("Error di connessione con il database")
            return None
        cursor=cnx.cursor()
        query="""SELECT * from hub"""
        try:
            cursor.execute(query)
            rows = cursor.fetchall()  # ottieni tutte le righe

            hubs = []
            for row in rows:
                hub = Hub(id=row[0],codice=row[1],nome=row[2],citta=row[2],stato=row[3],latitudine=row[4],longitudine=row[5])
                hubs.append(hub)

            return hubs

        finally:
            cursor.close()
            cnx.close()



if __name__ == "__main__":
    lista = DAO.get_tratte()
    for i in lista:
        print(i.valore)



