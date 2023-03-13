import flet as ft
from func import date_format_validation

def main(page: ft.Page):
    # page setup
    page.title = 'BabySitter'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 520
    page.window_height = 430
    page.window_resizable = False
    page.window_always_on_top = True

    # img = ft.Image(src='/Users/jeter/ Dev/github/i_am_not_your_babysitter/img')

    usr_field = ft.TextField(label='Username', autofocus=True, width=500)
    pwd_field = ft.TextField(label='Password', password=True, can_reveal_password=True, width=500)
    start_date_field = ft.TextField(label='Start Date', width=500)
    end_date_field = ft.TextField(label='End Date', width=500)
    
    def start_btn_action(e):
        start_date = start_date_field.value
        end_date = end_date_field.value

        def error_msg_snake_bar(msg):
            page.snack_bar = ft.SnackBar(
                content=ft.Text(msg, color='yellow', weight='bold')
            )
            page.snack_bar.open = True
            page.snack_bar.bgcolor = 'red'
            page.update()

        checking = date_format_validation.start_date_and_end_date_validation(start_date, end_date)

        if checking != True:
            error_msg_snake_bar(checking)
        
        else:
            pass

    start_btn = ft.ElevatedButton('Start Logging', width=400, on_click=start_btn_action)



    page.add(
        usr_field,
        pwd_field,
        start_date_field,
        end_date_field,
        ft.Row([start_btn], alignment='center')
    )

ft.app(target=main)


class ImNotYourBabySitter:
    def __init__(self):
        