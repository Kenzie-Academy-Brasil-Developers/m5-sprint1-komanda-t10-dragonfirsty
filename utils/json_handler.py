import ujson as json

def read_menu(menu_path : str) -> list[dict]:
        try:
            with open(menu_path,'r') as database:
                json_data = json.load(database)
             
        except (json.JSONDecodeError,FileNotFoundError,FileExistsError):        
            return []

        return json_data

def write_menu(menu_path : str,new_list: list):
    with open(menu_path,'w') as database:
        json.dump(new_list,database,indent=2)
