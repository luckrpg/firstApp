import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "Minha aplicação do flet >=)"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def mostrar_resultado(e):
        current_date = datetime.datetime.now()
        aniversario_date = datetime.datetime(year=int(input_ano.value), month=int(input_mes.value), day=int(input_dia.value))
        difference = current_date - aniversario_date

        years = difference.days // 365
        months = (difference.days % 365) // 30
        days = (difference.days % 365) % 30

        txt_resultado.value = f"Sua idade é essa ai ->: {years} anos, {months} meses e {days} dias."
        page.update()

    input_ano = ft.TextField(label="Ano de nascimento", hint_text="Digita o ano em que tu nasceu")
    input_mes = ft.TextField(label="Mês de nascimento", hint_text="Digita um mes de 1 a 12")
    input_dia = ft.TextField(label="Dia de nascimento", hint_text="Digita um dia de 1 a 31")
    btn_calcular = ft.FilledButton(text="Calcular idade", on_click=mostrar_resultado)
    txt_resultado = ft.Text()

    page.add(
        ft.Column(
            [
                input_ano,
                input_mes,
                input_dia,
                btn_calcular,
                txt_resultado
            ]
        )
    )
ft.app(main)