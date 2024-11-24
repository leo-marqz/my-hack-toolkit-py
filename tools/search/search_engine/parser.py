import json
from pathlib import Path

from tools.colors.fncolors import Colors as colors

class ContentParser:
    def __init__(self, data):
        self.data = data
        self.__items = []
        
    def parser(self)->None:
        if self.data is not None:
            for item in self.data:
                self.__items.append({
                    'title': item.get('title'),
                    'snippet': item.get('snippet'),
                    'link': item.get('link')
                })
        else:
            print( colors.yellow('[WARNING]No data to parse...') )
            

    def parser_to_txt(self, path:str)->None:
        filepath = Path(path)
        if not filepath.exists():
            filepath.touch()
        with open(path, 'w') as file:
            for item in self.__items:
                file.write(f"Titulo: {item.get('title')}\n")
                file.write(f"Descripcion: {item.get('snippet')}\n")
                file.write(f"Enlace: {item.get('link')}\n")
                file.write('\n')
                file.write('-----------------------------------\n')
        print( colors.green(f'[INFO]: Archivo {path} creado exitosamente') )
    
    def parser_to_json(self, path:str)->None:
        filepath = Path(path)
        if not filepath.exists():
            filepath.touch()
        with open(path, 'w') as file:
            json.dump(self.__items, file, indent=4)
        print( colors.green(f'[INFO]: Archivo {path} creado exitosamente') )
        
    def parser_to_console(self)->None:
        print( colors.bold('\nResultados de la busqueda: \n') )
        for item in self.__items:
            print(f'{colors.bold('Titulo:')} {colors.yellow(item.get("title"))} \n'
                  f'{colors.bold('Descripcion:')} {colors.cyan(item.get("snippet"))} \n'
                  f'{colors.bold('Enlace:')} {colors.blue(item.get("link"))} \n'
                  )
           