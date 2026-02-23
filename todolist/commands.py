import sys

class CommandsProgram():
    def __init__(self):
        self.tarefas = []

    def command_help():
        print
        (
            """
            Lista de comandos úteis:

            -> help-commands: Lista de todos os comandos do programa \n
            """
        )

    def help_commands():
        print
        (
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
        
        if len(tarefa) >= 2:
            self.tarefas.append(tarefa)

    def command_show_itens(self):
        if len(self.tarefas) == 0:
            print('Lista vazia')

        index_item = 0
        for i in self.tarefas:
            index_item = index_item + 1
            print(f'{index_item}. {i}')

    def command_rename(self):
        ...

    def command_delete(self):
        i = str(input('Qual item quer deletar? '))

        self.tarefas.remove(i)

    def command_exit():
        sys.exit('Programa encerrado')
