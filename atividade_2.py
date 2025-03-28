import flet as ft


def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def somar(e):
        soma = int(num1_input.value) + int(num2_input.value)
        text_result.value = f"Resultado = {soma}"
        page.update()


    def dividir(e):
        dividi = int(num1_input.value) / int(num2_input.value)
        text_result.value = f"Resultado = {dividi}"
        page.update()


    def subtrair(e):
        menos = int(num1_input.value) - int(num2_input.value)
        text_result.value = f"Resultado = {menos}"
        page.update()


    def mult(e):
        multiplicar = int(num1_input.value) * int(num2_input.value)
        text_result.value = f"Resultado = {multiplicar}"
        page.update()


    num1_input = ft.TextField(label="digita numero:")
    num2_input = ft.TextField(label="digita numero:")
    btn_button = ft.FilledButton(text="somar", on_click=somar)
    btn_button2 = ft.FilledButton(text="subtrair", on_click=subtrair)
    btn_button3 = ft.FilledButton(text="multiplicar", on_click=mult)
    btn_button4 = ft.FilledButton(text="dividir", on_click=dividir)

    text_result = ft.Text("")

    page.add(
            ft.Column(
                [
                    num1_input,
                    num2_input,
                    btn_button,
                    btn_button2,
                    btn_button3,
                    btn_button4,
                    text_result,
                ]
        )
    )


ft.app(main)
