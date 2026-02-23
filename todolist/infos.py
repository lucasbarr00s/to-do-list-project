
from termcolor import cprint 
from pyfiglet import figlet_format

class InfosProgram():
       def print_welcome_message(self):
              cprint(figlet_format('TO DO LIST CLI', font='starwars'),
              'blue', 'on_black', attrs=['bold'])

              print('BEM VINDO AO SOFTWARE - TO DO LIST CLI')
              print('Digite help para mais informações 👌 \n')