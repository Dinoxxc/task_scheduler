# ascii_art.py
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def print_ascii_art():
    """
    Menampilkan ASCII Art 'VM2025'
    """
    ascii_art = Fore.CYAN + Style.BRIGHT + r"""
__      __   __  __   
\ \    / /  |  \/  |  
 \ \  / /   | |\/| |  
  \ \/ /    | |  | |  
   \  /     | |  | |  
    \/      |_|  |_|    

      2  0  2  5
""" + Style.RESET_ALL

    print(ascii_art)
