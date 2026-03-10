from dotenv import load_dotenv

from src.extract.myl import getCards,getBlock
from src.load.loadBd import loadDataCards,deleteDataCards

def main():
    block = getBlock(1)
    page = 1
    staticNumberCards = 500
    totalCards = block["cardCount"] 
    print(totalCards)


    deleteDataCards()

    while True:
        cards = getCards(page, staticNumberCards)
        cardsList = cards["data"]["CardCatalog"]["cards"]
        if not cardsList:
            break
        print(f"Página {page} - {len(cardsList)} cartas")
        loadDataCards(cardsList)
        page += 1

if __name__ == "__main__":
    main()