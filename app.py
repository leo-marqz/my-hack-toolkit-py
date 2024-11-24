import sys
import argparse
from dotenv import load_dotenv

from tools.console.fnconsole import Console
from tools.search.search_engine.engine import SearchEngine
from tools.search.search_engine.parser import ContentParser

def main(clinput = None)->None:
    load_dotenv(dotenv_path='.env')
    
    arguments = clinput.parse_args()
    
    if arguments.google and arguments.search:
        engine = SearchEngine()
        result = engine.search(arguments.search, arguments.page or 1, arguments.nresults or 10, arguments.language or 'lang_es')
        if result.get_status_code() == 200:
            parser = ContentParser( result.get_content().get('items') )
            parser.parser()
            if arguments.export_json:
                parser.parser_to_json(arguments.export_json)
            if arguments.export_txt:
                parser.parser_to_txt(arguments.export_txt)
            if arguments.show_console:
                parser.parser_to_console()
        else:
            print(f"Error: {result.get_status_code()} => {result.get_message()}")
            
    elif arguments.openai and arguments.search:
        print(f'OpenAI: {arguments.search}')
    else:
        clinput.print_help()
        sys.exit(1)


if __name__ == '__main__':
    clinput = argparse.ArgumentParser(description='Crack Night Tools')
    clinput.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    
    # Google Search Engine
    gsearch = clinput.add_argument_group('Google Search Engine')
    gsearch.add_argument('-g', '--google', action='store_true', help='Google API')
    gsearch.add_argument('-s', '--search', type=str, help='Query to search')
    gsearch.add_argument('-p', '--page', type=int, help='Page to search')
    gsearch.add_argument('-n', '--nresults', type=int, help='Number of results')
    gsearch.add_argument('-l', '--language', type=str, help='Language to search')
    gsearch.add_argument('-ej', '--export-json', type=str, help='Export to JSON (path)')
    gsearch.add_argument('-et', '--export-txt', type=str, help='Export to TXT (path)')
    gsearch.add_argument('-sc', '--show-console', action='store_true', help='Show results in console')
    
    # OpenAI Search Engine
    aisearch = clinput.add_argument_group('AI Engine')
    aisearch.add_argument('-o', '--openai', action='store_true',  help='OpenAI API')
    aisearch.add_argument('-q', '--query', type=str, help='Query to search')
    
    main(clinput)
    
    


