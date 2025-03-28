import flet as ft
from flet import AppBar, ElevatedButton, Text, View
from flet.core import page
from flet.core.colors import Colors
from flet.core.outlined_button import OutlinedButton


def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(

            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="navegar", on_click=lambda _: page.go("/segunda")),
                ],

            )

        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f"ola {input_nome.value}")
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)

    page.update()
    input_nome = ft.TextField(label="Nome", hint_text="Digita teu nome ae")

ft.app(main)
