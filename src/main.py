import flet as ft
from func import date_format_validation
from src.logger import Logger

def main(page: ft.Page):
    # page setup
    page.title = 'BabySitter'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = False
    page.window_always_on_top = True

    img = ft.Image(
        src=f'/img/1.jpg',
        height=300,
        fit=ft.ImageFit.CONTAIN
    )

    img_row = ft.Row([img], alignment='center')

    usr_field = ft.TextField(label='Username', autofocus=True, width=500)
    pwd_field = ft.TextField(label='Password', password=True, can_reveal_password=True, width=500)
    start_date_field = ft.TextField(label='Start Date (YYYYMMDD)', width=500)
    end_date_field = ft.TextField(label='End Date (YYYYMMDD)', width=500)


    def start_log_time(e):
        usr = usr_field.value
        pwd = pwd_field.value
        start_date = start_date_field.value
        end_date = end_date_field.value

        Logger(usr, pwd, start_date, end_date).start_log_time()


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

        def close_confirmation_dlg(e):
            confirmation_dlg.open = False
            page.update()

        confirmation_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text('Are you sure?'),
            content=ft.Text(f'To log time from {start_date} to {end_date}?'),
            actions=[
                ft.TextButton('Yes', on_click=start_log_time),
                ft.TextButton('No', on_click=close_confirmation_dlg)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print('Dialog dismissed')
        )

        def open_confirmation_dlg(e):
            page.dialog = confirmation_dlg
            confirmation_dlg.open = True
            page.update()

        if len(usr_field.value) == 0:
            error_msg_snake_bar('Please enter your username')

        elif len(pwd_field.value) == 0:
            error_msg_snake_bar('Please enter your password')

        elif checking != True:
            error_msg_snake_bar(checking)
        
        else:
            open_confirmation_dlg(e)


    start_btn = ft.ElevatedButton('Start Logging', width=400, on_click=start_btn_action)



    page.add(
        img_row,
        usr_field,
        pwd_field,
        start_date_field,
        end_date_field,
        ft.Row([start_btn], alignment='center')
    )

ft.app(target=main, assets_dir='assets')
