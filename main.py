import flet as ft

def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def mostrar_nome(e):
        txt_resultado.value =  input_nome.value
        page.update()


    input_nome = ft.TextField(label="Nome", hint_text="Digita teu nome ae")

    btn_enviar = ft.FilledButton(text="Enviar", width=page.window.width, on_click=mostrar_nome)

    txt_resultado = ft.Text(value="Resultado")

    page.add(

        ft.Column([inp

ut_nome, btn_enviar, txt_resultado])
    )



ft.app(main)