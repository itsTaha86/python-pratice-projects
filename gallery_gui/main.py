# Imports and global variables
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import os

# Make the gallery or get it's path
current_path = os.path.dirname(os.path.abspath(__file__))
gallery_path = os.path.join(current_path, "Kivy Gallery")
if not os.path.exists(gallery_path):
    os.makedirs(gallery_path)

# Checks the dir files formats
supported_formats = (".jpg", ".jpeg", ".png")
images = []
for f in os.listdir(gallery_path):
    if f.endswith(supported_formats):
        images.append(os.path.join(gallery_path, f))


# Main Gallery app
class GalleryApp(App):
    def build(self):

        # main_box contains picture_layout and buttons_layout
        main_box = BoxLayout(orientation="vertical")
        picture_layout = AnchorLayout(
            anchor_x="center", anchor_y="bottom", size_hint=(1, 0.8)
        )
        buttons_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))

        main_box.add_widget(picture_layout)
        main_box.add_widget(buttons_layout)

        # Picture number in gallery
        self.pic_num = 0

        # Kivy picture object
        # Condition to handle 0 photos error
        if len(images) != 0:
            current_picture = images[self.pic_num]
        else:
            current_picture = None
        self.picture = Image(
            source=current_picture, allow_stretch=True, keep_ratio=True
        )
        picture_layout.add_widget(self.picture)

        # Kivy button objects
        prev_button = Button(
            text="Previous",
            size_hint=(0.5, 0.8),
            background_color="6087cf",
            font_size="30sp",
        )
        next_button = Button(
            text="Next",
            size_hint=(0.5, 0.8),
            background_color="6087cf",
            font_size="30sp",
        )

        next_button.bind(on_press=self.next_pic)
        prev_button.bind(on_press=self.prev_pic)

        buttons_layout.add_widget(prev_button)
        buttons_layout.add_widget(next_button)

        return main_box

    # Buttons functions
    def next_pic(self, instance):
        self.pic_num += 1
        if self.pic_num >= len(images):
            self.pic_num = 0
        self.picture.source = images[self.pic_num]
        self.picture.reload()

    def prev_pic(self, instance):
        self.pic_num -= 1
        if self.pic_num < 0:
            self.pic_num = len(images) - 1
        self.picture.source = images[self.pic_num]
        self.picture.reload()


# Run the application
if __name__ == "__main__":
    GalleryApp().run()
