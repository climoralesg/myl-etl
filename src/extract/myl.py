import requests

def getCards(page: int, limit: int) -> dict:
    URL = "https://api.mazos.cl/"

    data = {
        "operationName": "CardCatalog",
        "query": """query CardCatalog($CardCatalogInput: CardCatalogInput!) {
        CardCatalog(input: $CardCatalogInput) {
        cards {
          id
          slug
          name
          gameId
          editionId
          collectorCode
          deckBuilder
          effect
          flavor
          type
          cost
          attack
          imageUrl
          imageIlustrationUrl
          artist
          frequency
          mechanics
          race
          isUnique
          isMercenary
          isNew
          sortOrder
          createdAt
          isFavorite
          edition {
            id
            name
            slug
            __typename
          }
          game {
            name
            slug
            __typename
          }
          isFavorite
          __typename
        }
        total
        pages
        __typename
      }
    }""",
        "variables": {
            "CardCatalogInput": {
                "editionId": "",
                "featured": False,       # Booleano real
                "frecuency": None,       # null → None
                "gameId": "primer-bloque",
                "limit": limit,
                "mechanics": None,       # null → None
                "page": page,
                "productIds": None,      # null → None
                "races": None,           # null → None
                "search": "",
                "sortBy": "rarity",
                "type": None             # null → None
            }
        }
    }

    
    response = requests.post(URL, json=data)

    return response.json() #devuelve un diccionario
   
    
def getBlock(idBlock):
  URL = "https://api.mazos.cl/"
  data = {
     "operationName": "Games",
     "query": """query Games {  
        games {
          id 
          name    
          slug    
          description    
          epoca   
          sinceFrom    
          image    
          tags    
          cardCount    
          __typename
          editions {      
            id      
            cardCount      
            name      
            description      
            slug      
            pathFiles      
            imageCover      
            imageLogo      
            __typename    
          }      
        }
      }""",
     "variables": {}
  }
  response = requests.post(URL, json=data)

  gamesEdition = response.json()["data"]["games"]
  
  edition= next((u for u in gamesEdition if u["id"] == idBlock), None)
  
  return edition


