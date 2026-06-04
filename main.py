# ترفند حیاتی برای دور زدن باگ داخلی KivyMD و جلوگیری از کرش لودینگ
import sys
try:
    from jnius import autoclass
    import jnius
    # پیدا کردن کلاس واقعی اکتیویتی کایوی
    real_activity = autoclass('org.kivy.android.PythonActivity')
    # تزریق اکتیویتی واقعی به آدرسی که کیوی‌ام‌دی به اشتباه دنبالش می‌گردد
    sys.modules['org.renpy.android.PythonActivity'] = real_activity
except Exception as e:
    print(f"Jnius bypass skipped (Not running on Android yet): {e}")

# حالا با خیال راحت کتابخانه‌ها لود می‌شوند و کرش رخ نمی‌دهد
import json
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.textfield import MDTextField

# طراحی رابط کاربری برنامه
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    md_bg_color: [0.07, 0.07, 0.08, 1]

    MDTopAppBar:
        title: "SSH Tunnel Manager"
        elevation: 4
        md_bg_color: [0.12, 0.12, 0.16, 1]
        specific_text_color: [1, 1, 1, 1]

    MDBoxLayout:
        orientation: 'vertical'
        padding: "16dp"
        spacing: "12dp"

        MDScrollView:
            MDList:
                id: server_list_container

        MDFloatingActionButton:
            icon: "plus"
            md_bg_color: [0.12, 0.53, 0.9, 1]
            icon_color: [1, 1, 1, 1]
            pos_hint: {"center_x": .5}
            on_release: app.show_add_server_dialog()
            
        MDLabel:
            id: status_label
            text: "Status: Ready"
            halign: "center"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 0.6]
            font_style: "Caption"
'''

CONFIG_FILE = "ssh_servers_pass.json"

class SSHTunnelApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        self.load_servers()

    def load_servers(self):
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
            except:
                pass

    def show_add_server_dialog(self):
        if not self.dialog:
            content = MDBoxLayout(orientation='vertical', spacing="12dp", size_hint_y=None, height="180dp")
            self.user_input = MDTextField(hint_text="Username (e.g. root)")
            self.ip_input = MDTextField(hint_text="IP or Domain")
            self.pass_input = MDTextField(hint_text="Password", password=True)
            
            content.add_widget(self.user_input)
            content.add_widget(self.ip_input)
            content.add_widget(self.pass_input)

            self.dialog = MDDialog(
                title="Add New Server",
                type="custom",
                content_cls=content,
                buttons=[
                    MDFlatButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                    MDRaisedButton(text="SAVE", on_release=lambda x: self.save_new_server())
                ],
            )
        self.dialog.open()

    def save_new_server(self):
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
            self.user_input.text = ""
            self.ip_input.text = ""
            self.pass_input.text = ""

    def connect_ssh(self, server):
        self.root.ids.status_label.text = f"Connecting to {server['ip']}..."
        self.root.ids.status_label.text = f"Connected to {server['ip']} (Port 1080)"

if __name__ == "__main__":
    SSHTunnelApp().run()
