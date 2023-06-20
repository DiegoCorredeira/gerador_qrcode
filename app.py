import tempfile
import qrcode
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import webbrowser

def gerar_qrcode():
    url = entrada.get()

    tamanho_qrcode = int(tamanho.get())


    correcao = [
        qrcode.constants.ERROR_CORRECT_L,
        qrcode.constants.ERROR_CORRECT_M,
        qrcode.constants.ERROR_CORRECT_Q,
        qrcode.constants.ERROR_CORRECT_H,
    ]
    opcao_correcao = ["Baixo", "Padrão", "Alto", "Máximo"]
    nivel_correcao = correcao[opcao_correcao.index(combo_correcao.get())]

    cor_qrcode = entrada_cor_qrcode.get()
    cor_fundoqrcode = entrada_cor_fundo.get()

    qr = qrcode.QRCode(
        version=1, 
        error_correction=nivel_correcao,
        box_size=tamanho_qrcode, 
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=cor_qrcode, back_color=cor_fundoqrcode)

    pil_img = img.convert("RGBA")
    pil_img.thumbnail((tamanho_qrcode, tamanho_qrcode))

    # Salvar a imagem temporariamente <chat gpt correction>
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
        pil_img.save(tmp_file.name, format='PNG')
        imagem_temporaria = tmp_file.name

    img_qrcode = ImageTk.PhotoImage(Image.open(imagem_temporaria))
    label_qrcode.config(image=img_qrcode)
    label_qrcode.image = img_qrcode

    compartilhar = messagebox.askyesno("Compartilhar", "Deseja compartilhar o QR Code gerado?")
    if compartilhar:
        webbrowser.open(imagem_temporaria)
    

root = tk.Tk()
root.title("Gerador de QR Code")

label_entrada = tk.Label(root, text="Texto ou URL")
label_entrada.pack()

entrada = tk.Entry(root, width=50)
entrada.pack()


label_tamanho = tk.Label(root, text="Tamanho do QRCODE")
label_tamanho.pack()

tamanho = tk.Entry(root, width=50)
tamanho.insert(tk.END, "250")
tamanho.pack()


opcao_correcao = ["Baixo", "Padrão", "Alto", "Máximo"]
combo_correcao = tk.StringVar(root)
combo_correcao.set(opcao_correcao[1])
menu_correcao = tk.OptionMenu(root, combo_correcao, *opcao_correcao)
menu_correcao.pack()


label_cor_qrcode = tk.Label(root, text="Cor do QRCODE")
label_cor_qrcode.pack()

entrada_cor_qrcode = tk.Entry(root, width=20)
entrada_cor_qrcode.insert(tk.END, "#000000")
entrada_cor_qrcode.pack()


label_cor_fundo = tk.Label(root, text="Cor do QRCODE")
label_cor_fundo.pack()

entrada_cor_fundo = tk.Entry(root, width=20)
entrada_cor_fundo.insert(tk.END, "#FFFFFF")
entrada_cor_fundo.pack()

botao_qrcode = tk.Button(root, text="Gerar QR CODE", command=gerar_qrcode)
botao_qrcode.pack()

label_qrcode = tk.Label(root)
label_qrcode.pack()

root.mainloop()