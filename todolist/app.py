from infos import InfosProgram

from commands import CommandsProgram
infoss = InfosProgram()
infoss.print_welcome_message()

class MainCommandTerminal(CommandsProgram):
    def __init__(self):
        super().__init__()
        
    def main(self):
        command = str(input('> ')).lower()
    
        match(command):
            case 'help':
                CommandsProgram.command_help()    
            case 'help-commands':
                CommandsProgram.help_commands()
            case 'create':
                CommandsProgram.command_create(self)
            case 'show':
                CommandsProgram.command_show_itens(self)
            case 'rename':
                CommandsProgram.command_rename(self)
            case 'delete':
                resultado_lista = self.tarefas 
                if len(resultado_lista) >= 1:
                    print(resultado_lista)
                    CommandsProgram.command_delete(self)
                else:
                    print('Lista vazia!')
            case 'exit':
                CommandsProgram.command_exit()
            case _:
                print('Digite um comando válido')

command_terminal = MainCommandTerminal()
while True:
    command_terminal.main()
