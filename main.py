import json
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
from kivy.utils import platform

# ساختار گرافیکی برنامه با زبان KV
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: 0.1, 0.1, 0.12, 1  # تم تاریک شیک

    MDTopAppBar:
        title: "مدیریت و اتصال SSH"
        elevation: 4
        pos_hint: {"top": 1}
        md_bg_color: 0.2, 0.2, 0.25, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "15dp"

        MDScrollView:
            MDList:
                id: server_list_container

        MDFloatingActionButton:
            icon: "plus"
            md_bg_color: 0.2, 0.6, 0.8, 1
            pos_hint: {"center_x": .5}
            on_release: app.show_add_server_dialog()
            
        MDLabel:
            id: status_label
            text: "وضعیت: آماده اتصال"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.7
            font_style: "Caption"
'''

CONFIG_FILE = "ssh_servers_pass.json"

class SSHManagerApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        self.load_servers()

    def load_servers(self):
        """بارگذاری سرورها و نمایش در لیست"""
        self.root.ids.server_list_container.clear_widgets()
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    servers = json.load(f)
                    for srv in servers:
                        item = OneLineAvatarIconListItem(
                            text=f"{srv['user']}@{srv['ip']}",
                            on_release=lambda x, s=srv: self.connect_ssh(s)
                        )
                        item.add_widget(IconLeftWidget(icon="server"))
                        self.root.ids.server_list_container.add_widget(item)
            except Exception:
                pass

    def show_add_server_dialog(self):
        """نمایش پنجره افزودن سرور جدید"""
        if not self.dialog:
            # ساخت یک باکس برای ورودی‌ها
            content = MDBoxLayout(orientation='vertical', spacing="12dp", size_hint_y=None, height="180dp")
            
            from kivymd.uix.textfield import MDTextField
            self.user_input = MDTextField(hint_text="نام کاربری (مثل root)")
            self.ip_input = MDTextField(hint_text="آی‌پي یا دامنه")
            self.pass_input = MDTextField(hint_text="رمز عبور", password=True)
            
            content.add_widget(self.user_input)
            content.add_widget(self.ip_input)
            content.add_widget(self.pass_input)

            self.dialog = MDDialog(
                title="افزودن سرور جدید",
                type="custom",
                content_cls=content,
                buttons=[
                    MDFlatButton(text="لغو", on_release=lambda x: self.dialog.dismiss()),
                    MDRaisedButton(text="ذخیره", on_release=lambda x: self.save_new_server())
                ],
            )
        self.dialog.open()

    def save_new_server(self):
        """ذخیره اطلاعات سرور جدید"""
        user = self.user_input.text.strip()
        ip = self.ip_input.text.strip()
        password = self.pass_input.text.strip()

        if user and ip and password:
            servers = []
            if os.path.exists(CONFIG_FILE):
                try:
                    with open(CONFIG_FILE, "r") as f:
                        servers = json.load(f)
                except: pass
            
            servers.append({"user": user, "ip": ip, "password": password})
            
            with open(CONFIG_FILE, "w") as f:
                json.dump(servers, f, indent=4)
            
            self.dialog.dismiss()
            self.load_servers()
            
            # خالی کردن فرم
            self.user_input.text = ""
            self.ip_input.text = ""
            self.pass_input.text = ""

    def connect_ssh(self, server):
        """شبیه‌سازی فرآیند اتصال در اندروید"""
        self.root.ids.status_label.text = f"در حال اتصال به {server['ip']}..."
        # توجه: برای اتصال واقعی SSH تونل در اندروید، پایتون خام محدودیت دارد 
        # و معمولاً در نسخه‌های نهایی از پکیج‌های بومی یا سرویس‌های پروکسی اندروید استفاده می‌شود.
        self.root.ids.status_label.text = f"اتصال موفقیت‌آمیز به {server['ip']} (تونل شبیه‌سازی شده)"

if __name__ == "__main__":
    SSHManagerApp().run()
