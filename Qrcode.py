import pyqrcode

def criar_Qrcode(link,nome):
    # Gerar QRcode
    url = pyqrcode.create(link)

    # Criar e salvar o arquivo como svg, exemplo: 'meu_perfil_linkedin.svg'
    url.svg(f'{nome}.svg', scale= 8)

    # Criar e salvar o arquivo como png, exemplo: 'meu_perfil_linkedin.png'
    url.png(f'{nome}.png', scale= 6)
