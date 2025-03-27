import flet as ft

def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


def verificar paridade(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"


num = int(ft.ask())

ft.text(verificar)


ft.app(main)
