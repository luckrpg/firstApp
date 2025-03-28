import flet as ft


def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def verificar_paridade(e):
        par_impar = int(num1.value) % 2
        if par_impar == 0:
            text_resultado.value = f"par"
        else:
            text_resultado.value = f"impar"

        page.update()

    num1 = ft.TextField(label="digita numero:")
    submit_button = ft.FilledButton(text="verificar", on_click=verificar_paridade)

    text_resultado = ft.Text("")

    page.add(
        ft.Column(
            [
                num1,
                submit_button,
                text_resultado
            ]
        )
    )


ft.app(main)
