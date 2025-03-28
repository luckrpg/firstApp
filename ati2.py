
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
                    AppBar(title=Text("Cadastrar Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ElevatedButton(
                        text="Salvar e Navegar",
                        on_click=lambda _: save_and_navigate()
                    ),
                ],
            )

        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(value=f"Título: {input_titulo.value}"),
                        Text(value=f"Descrição: {input_descricao.value}"),
                        Text(value=f"Categoria: {input_categoria.value}"),
                        Text(value=f"Autor: {input_autor.value}")
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

    def save_and_navigate():
        page.go("/segunda")

    input_titulo = ft.TextField(label="Título", hint_text="Digite o título do livro")
    input_descricao = ft.TextField(label="Descrição", hint_text="Digite a descrição do livro")
    input_categoria = ft.TextField(label="Categoria", hint_text="Digite a categoria do livro")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor do livro")

ft.app(main)
