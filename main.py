from utils.json_handler import read_menu,write_menu
from management.tab_handler import calculo_da_comanda

FILEPATH = 'menu.json'
    
item = { "name": "Bolo", "price": 10.0 }
table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    
def write_new_item(newItem : dict):
    database_data = read_menu(FILEPATH)
    id_key = len(database_data) + 1
    update_item = {'id' : id_key, 'name': newItem['name'],'price' : newItem['price']}
    database_data.append(update_item)
    write_menu(FILEPATH,database_data)

if __name__ == "__main__":
    print(read_menu(FILEPATH))
        
    write_new_item(item)
    print(calculo_da_comanda(table_1))

