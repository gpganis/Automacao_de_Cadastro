import flet as ft
from Automação import Verificar_Diretorio

def main(page: ft.page):
    page.title = "Menu Principal"
    page.window.Theme = ft.ThemeMode.LIGHT,
    page.window.width = 400
    page.window.height = 400
    page.window.center()
    page.window.to_front()
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = ft.colors.WHITE
    page.update()

    def btn_clicked(e):
        
        if txt1.value == '':
            txt1.error_text = "Campo Obrigatório"
        elif txt1.value.isnumeric() == False:
            txt1.error_text = "Digite Somente números"
        elif len(txt1.value) != 5:
            txt1.error_text = "O Código deve ter 5 digitos"	
        else:
            txt1.error_text = None

        if txt2.value == '':
            txt2.error_text = "Campo Obrigatório"
        elif txt2.value.isnumeric() == False:
            txt2.error_text = "Digite Somente números"
        elif len(txt2.value) != 5:
            txt2.error_text = "O Código deve ter 5 digitos"
        else:
            txt2.error_text = None
        
        if ((txt1.value != '' and txt1.value.isnumeric() == True and len(txt1.value) == 5) and 
              (txt2.value != '' and txt2.value.isnumeric() == True and len(txt2.value) == 5)):
            
            Verificar_Diretorio(int(txt1.value), int(txt2.value))      
        
        page.update()

    txt1 = ft.TextField(label="Último Código Fornecedor", width=300)
    txt2 = ft.TextField(label="Último Código Cliente", width=300)

    btn1 = ft.ElevatedButton(
        text="Iniciar",
        width=300,
        height=50,
        bgcolor=ft.colors.GREEN_500,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5)
        ),
        on_click=btn_clicked
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                txt1,
                txt2,
                btn1,                                                                 
            ],
            width=300,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        expand=True,
        width=500,
        alignment=ft.alignment.center
    )

    page.add(container)

ft.app(target=main)
