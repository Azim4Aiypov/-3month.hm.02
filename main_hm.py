import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'ToDo List'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_naximized = True

    task_list = ft.Column(spacing=10)

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, created_at, completed in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text, created_at, completed))
        page.update()

    def create_task_row(task_id, task_text, created_at, completed):
        task_field = ft.TextField(value=f"{task_text} - {created_at}", expand=True, dense=True, read_only=True)


        task_field.color = ft.Colors.YELLOW if completed else ft.Colors.WHITE
    
        def enable_edit(e):
            task_field.read_only = False
            page.update()

        def save_edit(e):
            main_db.update_task_db(task_id, task_field.value)
            task_field.read_only = True
            page.update()

        def done(e):
            main_db.done_task_(task_id)
            load_tasks()
            page.update

        return ft.Row([
                task_field,
                ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.YELLOW_400, on_click=enable_edit),
                ft.IconButton(ft.icons.SAVE, icon_color=ft.colors.GREEN_400, on_click=save_edit),
                ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED_400, on_click=lambda e: delete_task(task_id)),
                ft.IconButton(ft.icons.CHECK, icon_color=ft.colors.GREEN_400, on_click=done),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

    def add_task(e):
        if task_input.value.strip():
            task_id,task_input.value,created_at = main_db.add_task_db(task_input.value)
            task_list.controls.append(create_task_row(task_id, task_input.value, created_at))
            task_input.value = ""
            page.update()

    def delete_task(task_id):
        main_db.delete_task_db(task_id)
        load_tasks()

    def sort_date(e):
        task_list.controls.clear()
        for task_id, task_text, completed, created_at in main_db.sort_task_date():
            task_list.controls.append(create_task_row(task_id, task_text, completed, created_at))
        page.update()

    def sort_status(e):
        task_list.controls.clear()
        for task_id, task_text, completed, created_at in main_db.sort_task_status():
            task_list.controls.append(create_task_row(task_id, task_text, completed, created_at))
        page.update

    def clear_done(e):
        main_db.delete_done()
        load_tasks()
        page.update()

    clear = ft.ElevatedButton("Удалить выполненое",on_click=clear_done, icon=ft.icons.DELETE)
    task_input = ft.TextField(hint_text='добавить задачу',expand=True, dense=True ,on_submit=add_task)
    add_button = ft.ElevatedButton("добавить", on_click=add_task, icon=ft.icons.ADD)
    sort_by_date = ft.ElevatedButton("сортировать по дате", on_click=sort_date, icon=ft.icons.DATE_RANGE)
    sort_by_status = ft.ElevatedButton("сортировать по статутсу", on_click=sort_status, icon=ft.icons.CHECK_CIRCLE)


    content = ft.Container(
        content = ft.Column([clear,
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([sort_by_date, sort_by_status], alignment=ft.MainAxisAlignment.START),
            task_list
        ], alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        alignment = ft.alignment.center
    )
    background_image = ft.Image(
        src = '/home/admin12/to_do_list/image.png',
        fit = ft.ImageFit.FILL,
        width = page.width,
        height=page.height
    )
    background = ft. Stack([background_image, content])

    def on_resize(e):
        background_image.width = page.width
        background_image.height = page.height
        page.update()

    page.add(background)
    page.on_resized = on_resize


    load_tasks()

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)
