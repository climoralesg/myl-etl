from dotenv import load_dotenv
import os
import asyncio

from src.extract.myl import getCards,getBlock
from src.load.loadBd import loadDataCards,deleteDataCards
def main():

    block = getBlock(1)
  
    totalCards = block["cardCount"] 
    print(totalCards)
    x = 10
    page = 1
    staticNumberCards = 500

    deleteDataCards()
    cards = getCards(page,staticNumberCards)
    

    while x <= totalCards:
        cards = getCards(page,staticNumberCards)
        loadDataCards(cards["data"]["CardCatalog"]["cards"])
        page+=1
        x +=100

if __name__ == "__main__":
    main()