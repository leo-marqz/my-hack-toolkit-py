import time
from rich.progress import Progress
from rich.table import Table
from rich.console import Console as RichConsole

class Console:
    @staticmethod
    def progress_bar(message:str='', total:int=100, delay:float=0.3, text_format:str='[normal white]' ):
        """_summary_
        Create a progress bar in the console.
        Args:
            message (str, optional): _description_. Defaults to ''.
            total (int, optional): _description_. Defaults to 100.
            delay (float, optional): _description_. Defaults to 0.3.
            text_format (str, optional): _description_. Defaults to '[normal white]'.
        """
        with Progress() as progress:
            task = progress.add_task(f'{text_format}{message}', total=total)
            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(delay)
    
    @staticmethod
    def print(message:str='', text_format:str='[normal white]'):
        """_summary_
        Print a message to the console.
        Args:
            message (str, optional): _description_. Defaults to ''.
            text_format (str, optional): _description_. Defaults to '[normal white]'.
        """
        print(f'{text_format}{message}')
        
    @staticmethod
    def input(message:str='', text_format:str='[normal white]'):
        """_summary_
        Get input from the console.
        Args:
            message (str, optional): _description_. Defaults to ''.
            text_format (str, optional): _description_. Defaults to '[normal white]'.
        """
        return input(f'{text_format}{message}')
    
    @staticmethod
    def table(title:str,headers:list, data:list, header_style:str, data_style:str)->None:
        """_summary_
        Create a table in the console.
        Args:
            headers (list): example. ['Id','Name','Email','Salary']
            data (list): example. [['1','John Doe','], ['2','Jane Doe',], ['3','John Smith',]]
            header_style (str): example. 'bold'
            data_style (str): example. 'normal'
        """
        table = Table()
        if headers is None or data is None:
            raise ValueError('Headers and data are required')
        
        for header in headers:
            table.add_column(header, style=header_style)
            
        for row in data:
            table.add_row(*row, style=data_style)
            
        RichConsole().print(table)
        
        