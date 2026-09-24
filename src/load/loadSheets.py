import os
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def connectSheet():
    #Recordar como almacenar auth de google sheet
    credentials_info = json.loads(os.getenv("AUTH_GOOGLE"))

    credentials = Credentials.from_service_account_info(
        credentials_info,
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)



    return client

def loadSheetCards(cardsList, sheet):
    columns = [
        "id",
        "name",
        "collectorCode",
        "attack",
        "cost",
        "type",
        "frequency",
        "edition",
        "editionId",
        "game",
        "gameId",
        "race",
        "slug",
        "effect",
        "imageUrl",
        "imageIlustrationUrl",
        "createdAt",
        "sortOrder",
        "isFavorite",
        "isMercenary",
        "isNew",
        "isUnique",
        "deckBuilder"
    ]

    rows = []

    for card in cardsList:

        row = [
            card.get("id"),
            card.get("name"),
            card.get("collectorCode"),
            card.get("attack"),
            card.get("cost"),
            card.get("type"),
            card.get("frequency"),

            # edition
            card.get("edition", {}).get("name"),

            card.get("editionId"),

            # game
            card.get("game", {}).get("name"),

            card.get("gameId"),

            # race es una lista
            ", ".join(card.get("race", [])),

            card.get("slug"),
            card.get("effect"),
            card.get("imageUrl"),
            card.get("imageIlustrationUrl"),
            card.get("createdAt"),
            card.get("sortOrder"),
            card.get("isFavorite"),
            card.get("isMercenary"),
            card.get("isNew"),
            card.get("isUnique"),
            card.get("deckBuilder")
        ]

        rows.append(row)

    # Encabezados
    sheet.update(
        "A1",
        [columns]
    )

    # Datos
    if rows:
        sheet.append_rows(rows)

    #data = sheet.get_all_records()

    #print(cardsList)