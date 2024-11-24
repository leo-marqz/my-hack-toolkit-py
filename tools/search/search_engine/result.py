
class Result:
    
    def __init__(self, status_code:int, message:str, content, errors:list=list()) -> None:
        self.__status_code:int = status_code
        self.__message:str = message
        self.__content = content
        self.__errors:list = errors
    
    def is_success(self) -> bool:
        return self.__status_code == 200
    
    def get_status_code(self) -> int:
        return self.__status_code
    
    def get_message(self) -> str:
        return self.__message
    
    def get_content(self):
        return self.__content
    
    def get_errors(self) -> list:
        return self.__errors

