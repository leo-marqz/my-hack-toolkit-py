import os
import sys
import requests

from dotenv import load_dotenv, set_key
from tools.colors.fncolors import Colors as colors
from tools.search.search_engine.result import Result

class SearchEngine:
    
    __engine_name:str = 'Crack Night Search Engine v1.0 [Google]'
    __link:str = 'https://www.googleapis.com/customsearch/v1'
    
    def __init__(self, api_key:str=None, api_id:str=None) -> None:
        load_dotenv()
        print( colors.bold( colors.yellow( SearchEngine.__engine_name ) ))
        
        if os.getenv('SEARCH_ENGINE_API_KEY') is None or os.getenv('.env', 'SEARCH_ENGINE_ID') is None:
            self.config()
        else:
            self.__api_key:str = os.getenv('SEARCH_ENGINE_API_KEY')
            self.__api_id:str = os.getenv('SEARCH_ENGINE_ID')
    
    def search(self, query:str, start_page:int=1, n_results:int=5, language:str='lang_en')->Result:
        try:
            link = f'{SearchEngine.__link}?key={self.__api_key}&cx={self.__api_id}&q={query}&start={start_page}&num={n_results}&lr={language}'
            response = requests.get(link)
            if response.status_code == 200:
                data = response.json()
                return Result(200, "OK", data, [])
            else:
                return Result(response.status_code, "Query error...", None, [])
        except Exception as e:
            print( colors.red(f'[ERROR]: {e}') )
            return Result(500, "Internal Application Error", None, None)
    
    def config(self)->None:
        print( colors.bold('Configuracion de API KEY') )
        api_key = input( colors.yellow('Ingrese su API KEY: ') )
        api_id = input( colors.yellow('Ingrese su API ID: ') )
        
        if api_key == '' or api_id == '':
            print( colors.red('[ERROR]: Configuracion invalida') )
            sys.exit(1)
        else:
            self.__api_key = api_key
            self.__api_id = api_id
            set_key('.env', 'SEARCH_ENGINE_API_KEY', api_key)
            set_key('.env', 'SEARCH_ENGINE_ID', api_id)
            # os.environ['SEARCH_ENGINE_API_KEY'] = api_key
            # os.environ['SEARCH_ENGINE_ID'] = api_id
            print( colors.green('[INFO]: Configuracion exitosa') )
    
    def clear_config(self)->None:
        self.__env.set_key('SEARCH_ENGINE_API_KEY', '')
        self.__env.set_key('SEARCH_ENGINE_ID', '')
        print( colors.green('[INFO]: Configuracion eliminada') )
            
        