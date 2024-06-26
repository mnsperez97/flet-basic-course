import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title ="Flet counter example"
    page.vertical_alignment = "center"
    
    txt_number = TextField(value=0, text_align="right", width=100)
    
    def minus_click(e):
        if txt_number.value > 0:
            txt_number.value = int(txt_number.value) - 1
            page.update()
        else:
            txt_number.value = 0
        
    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()
        
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )
    
#MODO WEB
#flet.app(target=main, view=flet.WEB_BROWSER)

#MODO DESKTOP
#flet.app(target=main)