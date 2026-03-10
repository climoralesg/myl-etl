from src.config.connection import Connection


def loadDataCards(cards):
    connection = Connection()
    handleDB = connection.connect()
    cursor = handleDB.cursor()
    query = """
    INSERT IGNORE INTO cards
    (id, name, attack, cost, effect, isUnique, imageUrl, type)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # Creamos una lista de tuplas, cada tupla = una fila
    values = []
    for card in cards:
        values.append((
            card["id"],
            card["name"],
            card["attack"],
            card["cost"],
            card["effect"],
            card["isUnique"],
            card["imageUrl"],
            card["type"]
        ))

    # Ejecutamos la inserción masiva
    cursor.executemany(query, values)
    handleDB.commit()

def deleteDataCards():
    connection = Connection()
    handleDB = connection.connect()
    cursor = handleDB.cursor()
    queryDelete = ("DELETE FROM cards")
    cursor.execute(queryDelete)
    handleDB.commit()
    cursor.close()
    handleDB.close()



