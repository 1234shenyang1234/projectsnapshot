from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.utils import platform
from kivy.lang import Builder
import os
import datetime
import sqlite3

# 导入相机和定位相关库
from kivy.core.camera import Camera as CoreCamera
from plyer import gps, storagepath

# 加载KV文件
Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            text: '项目随手拍'
            font_size: '30sp'
            size_hint_y: 0.1
        
        GridLayout:
            cols: 3
            rows: 1
            size_hint_y: 0.8
            
            Button:
                text: '相册'
                font_size: '20sp'
                on_press: root.manager.current = 'album'
            
            Button:
                text: '拍照'
                font_size: '20sp'
                on_press: root.manager.current = 'camera'
            
            Button:
                text: '我的'
                font_size: '20sp'
                on_press: root.manager.current = 'profile'

<CameraScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '返回'
                on_press: root.manager.current = 'main'
            
            Label:
                text: '拍照'
                font_size: '20sp'
        
        BoxLayout:
            size_hint_y: 0.8
            Image:
                id: camera_image
                allow_stretch: True
                keep_ratio: True
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '拍照'
                on_press: root.capture_photo()

<AlbumScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '返回'
                on_press: root.manager.current = 'main'
            
            Label:
                text: '相册'
                font_size: '20sp'
        
        BoxLayout:
            size_hint_y: 0.8
            ScrollView:
                GridLayout:
                    id: photo_grid
                    cols: 2
                    size_hint_y: None
                    height: self.minimum_height
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '刷新'
                on_press: root.load_photos()

<ProfileScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '返回'
                on_press: root.manager.current = 'main'
            
            Label:
                text: '我的'
                font_size: '20sp'
        
        BoxLayout:
            size_hint_y: 0.8
            ScrollView:
                GridLayout:
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    
                    Button:
                        text: '水印设置'
                        size_hint_y: None
                        height: '50dp'
                        on_press: root.manager.current = 'watermark_settings'
                    
                    Button:
                        text: '关于我们'
                        size_hint_y: None
                        height: '50dp'
                    
                    Button:
                        text: '帮助与反馈'
                        size_hint_y: None
                        height: '50dp'

<WatermarkSettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            size_hint_y: 0.1
            Button:
                text: '返回'
                on_press: root.manager.current = 'profile'
            
            Label:
                text: '水印设置'
                font_size: '20sp'
        
        BoxLayout:
            size_hint_y: 0.8
            GridLayout:
                cols: 2
                rows: 4
                size_hint_y: None
                height: self.minimum_height
                
                Label:
                    text: '显示日期时间:'
                
                Button:
                    id: datetime_btn
                    text: '开启'
                    on_press: root.toggle_datetime()
                
                Label:
                    text: '显示位置:'
                
                Button:
                    id: location_btn
                    text: '开启'
                    on_press: root.toggle_location()
                
                Label:
                    text: '显示项目名称:'
                
                TextInput:
                    id: project_name
                    hint_text: '输入项目名称'
                
                Label:
                    text: '保存设置'
                    color: (0,0,0,0)
                
                Button:
                    text: '保存设置'
                    on_press: root.save_settings()
''')

class MainScreen(Screen):
    pass

class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.camera = CoreCamera(index=0, resolution=(640, 480))
        self.camera.play = True
        Clock.schedule_interval(self.update_camera, 1.0 / 30.0)
    
    def update_camera(self, dt):
        if self.camera.texture:
            self.ids.camera_image.texture = self.camera.texture
    
    def capture_photo(self):
        # 拍照并保存
        texture = self.camera.texture
        if texture:
            # 获取照片保存路径
            photo_dir = os.path.join(storagepath.get_pictures_dir(), 'ProjectSnapshot')
            if not os.path.exists(photo_dir):
                os.makedirs(photo_dir)
            
            # 生成照片文件名
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            photo_path = os.path.join(photo_dir, f'photo_{timestamp}.png')
            
            # 保存照片
            pixels = texture.pixels
            size = texture.size
            with open(photo_path, 'wb') as f:
                # 使用PIL保存为PNG
                from PIL import Image as PILImage
                img = PILImage.frombytes('RGBA', size, pixels)
                img.save(f, format='PNG')
            
            # 保存照片信息到数据库
            self.save_photo_info(photo_path)
    
    def save_photo_info(self, photo_path):
        # 创建数据库连接
        db_path = os.path.join(storagepath.get_documents_dir(), 'project_snapshot.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 创建照片表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS photos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT,
            timestamp TEXT,
            latitude REAL,
            longitude REAL,
            project_name TEXT
        )
        ''')
        
        # 插入照片信息
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
        INSERT INTO photos (path, timestamp, latitude, longitude, project_name) 
        VALUES (?, ?, ?, ?, ?)
        ''', (photo_path, timestamp, 0.0, 0.0, '默认项目'))
        
        conn.commit()
        conn.close()

class AlbumScreen(Screen):
    def on_enter(self):
        self.load_photos()
    
    def load_photos(self):
        # 清空照片网格
        self.ids.photo_grid.clear_widgets()
        
        # 获取照片路径
        photo_dir = os.path.join(storagepath.get_pictures_dir(), 'ProjectSnapshot')
        if os.path.exists(photo_dir):
            for filename in os.listdir(photo_dir):
                if filename.endswith('.png') or filename.endswith('.jpg'):
                    photo_path = os.path.join(photo_dir, filename)
                    
                    # 创建照片按钮
                    photo_btn = Button(size_hint_y=None, height='200dp')
                    # 这里可以添加照片缩略图
                    photo_btn.text = filename
                    self.ids.photo_grid.add_widget(photo_btn)

class ProfileScreen(Screen):
    pass

class WatermarkSettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(WatermarkSettingsScreen, self).__init__(**kwargs)
        self.datetime_enabled = True
        self.location_enabled = True
    
    def toggle_datetime(self):
        self.datetime_enabled = not self.datetime_enabled
        self.ids.datetime_btn.text = '开启' if self.datetime_enabled else '关闭'
    
    def toggle_location(self):
        self.location_enabled = not self.location_enabled
        self.ids.location_btn.text = '开启' if self.location_enabled else '关闭'
    
    def save_settings(self):
        # 保存设置到数据库或文件
        pass

class ProjectSnapshotApp(App):
    def build(self):
        # 创建屏幕管理器
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(AlbumScreen(name='album'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(WatermarkSettingsScreen(name='watermark_settings'))
        return sm

if __name__ == '__main__':
    ProjectSnapshotApp().run()
