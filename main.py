import PySimpleGUI as sg
from Qrcode import criar_Qrcode

# Tema
sg.theme('Reddit')

#Layout
layout = [
    [sg.Text('Digite o nome do Qrcode que irá gerar')],
    [sg.Input(key='nome')],
    [sg.Text(key='nome_invalido')],
    [sg.Text('Digite ou cole o link que deseja converter para QRcode: ')],
    [sg.Input(key='link')],
    [sg.Text(key='link_invalido')],
    [sg.Button('Criar')]
]

# Janela
janela = sg.Window('Criar Qrcode', layout=layout)

# Eventos e valores
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Criar':
        if values['link'] == '':
            janela['link_invalido'].update('Preencher o campo com um link')
        elif values['nome'] == '':
            janela['nome_invalido'].update('Preencher o campo com um nome')
        else:
            criar_Qrcode(values['link'],values['nome'])
            janela['link_invalido'].update('')
            janela['nome_invalido'].update('')
            janela['link'].update('')
            janela['nome'].update('')