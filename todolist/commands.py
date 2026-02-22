import sys

class CommandsProgram():
    def command_help():
        print(' ')
        print('Lista de comandos úteis:')
        print('-> help-commands: lista de todos os comandos do programa \n')

    def help_commands():
        print(' ')
        print('Lista de comandos:')
        print('- create: cria tarefa tarefa')
        print('- rename: renomeia a tarefa')
        print('- delete: deleta tarefa \n')

    def command_create(command):
        command = str(input('> ')).lower()


    def command_exit():
        print('Programa encerrado, até a próxima')
        sys.exit()
