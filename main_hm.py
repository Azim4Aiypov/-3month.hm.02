# main.py

import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'ToDo List'
    page.padding = 40
    page.bg_color = ft.colors.GREY_600
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)
    sort_type = ft.Text(value="created_at DESC")

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, created_at, completed in main_db.get_tasks(sort_type.value):
            task_list.controls.append(create_task_row(task_id, task_text, created_at, completed))
        page.update()

    def create_task_row(task_id, task_text, created_at, completed):
        task_field = ft.TextField(value=task_text, expand=True, read_only=True)
        date_label = ft.Text(value=f"Создано: {created_at[:19]}", color=ft.colors.GREY_300, size=12)
        checkbox = ft.Checkbox(value=bool(completed), on_change=toggle_complete)

        def enable_edit(e):
            task_field.read_only = False
            task_field.update()

        def save_edit(e):
            main_db.update_task_db(task_id, task_field.value)
            task_field.read_only = True
            task_field.update()

        def toggle_complete(e):
            main_db.set_completed(task_id, checkbox.value)
            load_tasks()

        return ft.Column([
            ft.Row([
                checkbox,
                task_field,
                ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.YELLOW_400, on_click=enable_edit),
                ft.IconButton(ft.icons.SAVE, icon_color=ft.colors.GREEN_400, on_click=save_edit),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            date_label
        ])

    def add_task(e):
        if task_input.value.strip():
            task_id = main_db.add_task_db(task_input.value.strip())
            load_tasks()
            task_input.value = ""
            page.update()

    # Сортировка
    def sort_new_first(e): sort_type.value = "created_at DESC"; load_tasks()
    def sort_old_first(e): sort_type.value = "created_at ASC"; load_tasks()
    def sort_completed_last(e): sort_type.value = "completed ASC, created_at DESC"; load_tasks()
    def sort_completed_first(e): sort_type.value = "completed DESC, created_at DESC"; load_tasks()

    task_input = ft.TextField(hint_text="Добавьте задачу", expand=True, dense=True, on_submit=add_task)
    add_button = ft.ElevatedButton("Добавить", on_click=add_task, icon=ft.icons.ADD, icon_color=ft.colors.GREEN_400)

    sort_buttons = ft.Row([
        ft.Text("Сортировка:", color=ft.colors.WHITE),
        ft.TextButton("Новые выше", on_click=sort_new_first),
        ft.TextButton("Старые выше", on_click=sort_old_first),
        ft.TextButton("Выполненные внизу", on_click=sort_completed_last),
        ft.TextButton("Выполненные вверху", on_click=sort_completed_first),
    ])

    page.add(
        ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            sort_buttons,
            task_list
        ])
    )

    load_tasks()

if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)
