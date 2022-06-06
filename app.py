
import os



def processar_resposta(resposta,nome):

        if resposta == '1':
            print(f'{os.linesep}mensagem{nome}mensagem{os.linesep}')
        elif resposta == '2':
            print(f'{os.linesep}mensagem{nome} mensagem{os.linesep}')
        elif resposta == '3':
            print(f'{os.linesep}mensagem{nome}mensagem{os.linesep}')
        else:
            print('Escola uma das opções 1, 2, 3')

def start():
        #Apresentar o chatbot
        print('mensagem')
        #Pedir nome
        nome = input('mensagem')
        while True:
            #Oferecer o menu de opções
            resposta = input(f'mensagem{nome}{os.linesep}[1] - mensagem{os.linesep}[2] - mensagem{os.linesep}[3] - mensagem{os.linesep}')
            
            #Processar a resposta enviada
            processar_resposta(resposta,nome)
            

if __name__ == '__main__':
 start()