from welcome import print_welcome_message

from commands import CommandsProgram

print_welcome_message()

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
                CommandsProgram.command_create(command)
            case 'rename':
                ...
            case 'delete':
                ...
            case 'exit':
                CommandsProgram.command_exit()
            case _:
                print('Digite um comando válido')

command_terminal = MainCommandTerminal()
while True:
    command_terminal.main()
