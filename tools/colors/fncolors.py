
class Colors:
    __underline = '\033[4m'
    __italic = '\033[3m'
    __bold = '\033[1m'
    __blink = '\033[5m'
    __white = '\033[97m'
    __black = '\033[30m'
    __yellow = '\033[93m'
    __purple = '\033[95m'
    __blue = '\033[94m'
    __green = '\033[92m'
    __red = '\033[91m'
    __cyan = '\033[96m'
    __end = '\033[0m'

    @staticmethod
    def underline(text):
        return Colors.__underline + text + Colors.__end
    
    @staticmethod
    def italic(text):
        return Colors.__italic + text + Colors.__end
    
    @staticmethod
    def bold(text):
        return Colors.__bold + text + Colors.__end
    
    @staticmethod
    def blink(text):
        return Colors.__blink + text + Colors.__end
    
    @staticmethod
    def white(text):
        return Colors.__white + text + Colors.__end
    
    @staticmethod
    def black(text):
        return Colors.__black + text + Colors.__end
    
    @staticmethod
    def yellow(text):
        return Colors.__yellow + text + Colors.__end
    
    @staticmethod
    def purple(text):
        return Colors.__purple + text + Colors.__end
    
    @staticmethod
    def blue(text):
        return Colors.__blue + text + Colors.__end
    
    @staticmethod
    def green(text):
        return Colors.__green + text + Colors.__end
    
    @staticmethod
    def red(text):
        return Colors.__red + text + Colors.__end
    
    @staticmethod
    def cyan(text):
        return Colors.__cyan + text + Colors.__end
    
    @staticmethod
    def color(text, color):
        if color == 'white':
            return Colors.white(text)
        elif color == 'black':
            return Colors.black(text)
        elif color == 'yellow':
            return Colors.yellow(text)
        elif color == 'purple':
            return Colors.purple(text)
        elif color == 'blue':
            return Colors.blue(text)
        elif color == 'green':
            return Colors.green(text)
        elif color == 'red':
            return Colors.red(text)
        else:
            return text