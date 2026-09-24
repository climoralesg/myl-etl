
from dotenv import load_dotenv

load_dotenv()

from src.extract.myl import getCards,getBlock
from src.load.loadBd import loadDataCards,deleteDataCards
from src.load.loadSheets import connectSheet,loadSheetCards

'''
para utilizar modo myl, primero se debe ingresar la base de datos en el script bd.myl
y descomentar las funciones indicadas en main

Si se utiliza el modo mysql comentar las funciones de ingreso a sheets de google
'''


def main():
    
    block = getBlock(1)
    page = 1
    
    totalCards = block["cardCount"] 
    print(totalCards)
    chunkNumberCards = 100

    #Funcion determinada para eliminar datos de cartas en MySql
    #deleteDataCards()
    clientConnected = connectSheet()
    sheet = clientConnected.open("myl-etl").sheet1

    while True:
        cards = getCards(page, chunkNumberCards)
        cardsList = cards["data"]["CardCatalog"]["cards"]
        if not cardsList:
            break
        print(f"Página {page} - {len(cardsList)} cartas")
        #Funcion determinada para ingresar datos de cartas en MySql
        #loadDataCards(cardsList)   
        loadSheetCards(cardsList, sheet)
        page += 1


    clientConnected.http_client.session.close()


if __name__ == "__main__":
    main()