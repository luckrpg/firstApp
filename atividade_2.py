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


    num1_input = ft.TextField(label="digita numero:")
    num2_input = ft.TextField(label="digita numero:")
    submit_button1 = ft.TextButton(
        text="somar",
        on_click=somar
    )



    def dividir(e):
        dividi = int(num1_input.value) / int(num2_input.value)
        text_result.value = f"Resultado = {dividi}"
        page.update()


    num1_input = ft.TextField(label="digita numero:")
    num2_input = ft.TextField(label="digita numero:")
    submit_button2 = ft.FilledButton(
        text="dividir",
        on_click=dividir
    )

    def subtrair(e):
        menos = int(num1_input.value) - int(num2_input.value)
        text_result.value = f"Resultado = {menos}"
        page.update()


    num1_input = ft.TextField(label="digita numero:")
    num2_input = ft.TextField(label="digita numero:")
    submit_button3 = ft.TextButton(
        text="menos",
        on_click=subtrair
    )

    def mult(e):
        multiplicar = int(num1_input.value) * int(num2_input.value)
        text_result.value = f"Resultado = {multiplicar}"
        page.update()


    num1_input = ft.TextField(label="digita numero:")
    num2_input = ft.TextField(label="digita numero:")
    submit_button4 = ft.TextButton(
        text="multiplicar",
        on_click=mult
    )

    text_result = ft.Text(value="Resultado")

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    num1_input,
                    num2_input,
                    submit_button1,
                    submit_button2,
                    submit_button3,
                    submit_button4,
                    text_result,
                    somar,
                    mult,
                    subtrair,
                    dividir,
                ]
            ),
            expand=True
        )
    )

ft.app(main)
