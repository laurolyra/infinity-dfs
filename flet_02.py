import flet as ft

def main(page):
    campo_valores = ft.Text(value="", size=20, bgcolor=ft.colors.PINK)
    campo_resultado = ft.Text(value="", size=20, bgcolor=ft.colors.PINK)
    # Botões numéricos e de operações
    def calcular(e):
        #logica para os botões
        #caso o botão apertado seja "="
        if e.control.text == "=":
            #executar a operação matemática
            conta = eval(campo_valores.value)
            #trocar o valor de campo_resultado
            campo_resultado.value = conta
        elif e.control.text == "Limpar":
            campo_valores.value = ""
            campo_resultado.value = ""
        else:
            campo_valores.value = campo_valores.value + e.control.text
        campo_valores.update()
        campo_resultado.update()
    buttons = [
        ft.Row([
            ft.ElevatedButton("1", on_click=calcular, bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("2", on_click=calcular,bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("3", bgcolor=ft.colors.BLUE, on_click=calcular),
        ]),
        ft.Row([
            ft.ElevatedButton("4", on_click=calcular,bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("5", on_click=calcular,bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("6", on_click=calcular,bgcolor=ft.colors.BLUE),
        ]),
        ft.Row([
            ft.ElevatedButton("7", on_click=calcular,bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("8", on_click=calcular,bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("9", on_click=calcular, bgcolor=ft.colors.BLUE)
        ]),
        ft.Row([
            ft.ElevatedButton("0", on_click=calcular, bgcolor=ft.colors.BLUE)
        ]),
         ft.Row([
            ft.ElevatedButton("Limpar", on_click=calcular, bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("+", on_click=calcular, bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("-", on_click=calcular, bgcolor=ft.colors.BLUE),
            ft.ElevatedButton("=", on_click=calcular, bgcolor=ft.colors.BLUE)
        ]),
    ]

    # Layout da página com duas colunas
    page.add(
        ft.Container(
            width=600,
            bgcolor=ft.Colors.GREEN,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Row([
            ft.Container(content=ft.Column(buttons, spacing=10)),
            ft.Container(content=ft.Column([
                ft.Text("Valores"),
                campo_valores,
                ft.Text("Resultado"),
                campo_resultado
            ]))
        ])
        )
    )

ft.app(target=main)

'''
Exercícios:
1- Troque a cor dos botões que não sejam números (as operações matemáticas, o símbolo "=" e o "Limpar")
2- acrescente as operações de multiplicação e divisão - adapte a função calcular para fazer essas contas;

#BOA SORTE
separar todo o código em arquivos distintos, sendo um para os botões, um para a função calcular e um para os campos de valores;
#BOA SORTE + SPOILER
estude uma forma de não precisar repetir todos os argumentos dos botões de número
'''
