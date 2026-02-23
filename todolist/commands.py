import sys

class CommandsProgram():
    def __init__(self):
        self.tarefas = []

    def command_help():
        print(
            """
            Lista de comandos úteis:

            -> help-commands: Lista de todos os comandos do programa \n
            """
        )

    def help_commands():
        print(
            """
            Lista de comandos:

            -> create-task: Cria tarefas
            -> show: Mostra lista de tarefas
            -> rename: Renomeia tarefas
            -> delete: Remove tarefas
            -> exit: Saí do programa
            """
        )

    def command_create(self):
        tarefa = str(input(''))

        self.tarefas.append(tarefa)

    def command_show_itens(self):
        for i in self.tarefas:
            print(i)

    def command_delete(self):
        i = int(input())
        self.tarefas.remove()

    def command_exit():
        sys.exit('Programa encerrado')
