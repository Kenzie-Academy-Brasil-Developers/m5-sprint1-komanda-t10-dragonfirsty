from datetime import date, time, datetime, timedelta, timezone

from utils.json_handler import read_menu

def calculo_da_comanda(listId : list[dict]) -> dict:
    menu_database = read_menu("menu.json")
    prices = []
    created_time = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    for listinha in listId:
        for cardapiozinho in menu_database:
            if listinha['id'] == cardapiozinho['id']:
                prices.append(listinha['amount'] * cardapiozinho['price'])
                break


    return {'amount' : sum(prices),'created_at' : created_time}            
        
                   