if __name__ == "__main__":
    from utils.json_handler import read_menu,write_menu

    FILEPATH = 'menu.json'
    
    read_menu(FILEPATH)

    item = { "name": "Bolo", "price": 10.0 }
    

    def write_new_item(newItem : dict):
        database_data = read_menu(FILEPATH)
        id_key = len(database_data) + 1
        newItem['id'] = id_key 
        update_item = {'id' : id_key, 'name': newItem['name'],'price' : newItem['price']}
        database_data.append(update_item)
        write_menu(FILEPATH,database_data)
        
    write_new_item(item)