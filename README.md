## Gerador de QR Code

Este é um gerador de QR Code desenvolvido em Python utilizando as bibliotecas TKinter, QRCode e Pillow. O objetivo é gerar um QR Code para um determinado link ou texto fornecido pelo usuário.

### Requisitos:
- Python 3.x instalado no seu sistema.
- As bibliotecas TKinter, QRCode e Pillow instaladas. Caso você não tenha essas bibliotecas instaladas, pode instalá-las usando o pip, executando o seguinte comando no terminal:
```
pip install tk qrcode pillow
```

### Passo a passo:

1. Importe as bibliotecas necessárias:
```python
import tkinter as tk
import qrcode
from PIL import ImageTk, Image
```

2. Crie a interface gráfica utilizando a biblioteca TKinter:
```python
root = tk.Tk()
root.title("Gerador de QR Code")

# Código da interface gráfica
```

3. Crie a função que irá gerar o QR Code:
```python
def gerar_qrcode():
    # Obtenha a url ou texto digitado pelo usuário
    url = entrada.get()

    # Crie um objeto QRCode
        qr = qrcode.QRCode(
        version=1, 
        error_correction=nivel_correcao,
        box_size=tamanho_qrcode, 
        border=4,
    )

    # Adicione os dados ao QRCode
    qr.add_data(url)
    qr.make(fit=True)

    # Crie uma imagem PIL (Pillow) a partir do QRCode
    img = qr.make_image(fill_color=cor_qrcode, back_color=cor_fundoqrcode)

    # Salve a imagem temporariamente
    img_temp = "qrcode_temp.png"
    img.save(img_temp)

    # Exiba o QR Code na interface gráfica
    img_qrcode = ImageTk.PhotoImage(Image.open(img_temp))
    label_qrcode.configure(image=qr_code_img)
    label_qrcode.image = qr_code_img
```

4. Adicione os elementos da interface gráfica (entrada de texto, botão e área para exibir o QR Code):
```python
# Crie a entrada de texto
entry_texto = tk.Entry(root, width=50)
entry_texto.pack()

# Crie o botão para gerar o QR Code
button_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qrcode)
button_gerar.pack()

# Crie a área para exibir o QR Code
label_qrcode = tk.Label(root)
label_qrcode.pack()
```

5. Inicie a interface gráfica:
```python
root.mainloop()
```

### Execução:
- Salve o código em um arquivo com extensão ".py", por exemplo, "gerador_qrcode.py".
- Abra um terminal e navegue até o diretório onde o arquivo .py está salvo.
- Execute o arquivo com o comando:
```
python gerador_qrcode.py
```
- Uma janela será aberta com a interface gráfica do gerador de QR Code.
- Digite o link ou texto desejado na caixa de entrada de texto.
- Clique no botão "Gerar QR Code".
- O QR Code será exibido na área destinada.

### Link para assistir como foi feito:
Para assistir como foi feito esse gerador de QR Code, você pode acessar o seguinte link do Twitch: [https://www.twitch.tv/videos/1851110761](https://www.twitch.tv/videos/1851110761)

Nesse vídeo, você encontrará uma demonstração

 passo a passo do desenvolvimento do gerador de QR Code utilizando as bibliotecas mencionadas.
