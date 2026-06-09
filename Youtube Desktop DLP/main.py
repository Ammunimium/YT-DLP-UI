import os
import subprocess
import time
try:
    import pyray as rl
except:
    os.system("pip install raylib")
    time.sleep(10)
    import pyray as rl
    

def main():
    export_path = "export"
    text_box_active = False
    text_box_text = ""
    rl.init_window(800, 600, f"Youtube Video Downloader")
    rl.set_target_fps(60)

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        #draw title
        rl.draw_text(f"Youtube Video Downloader  - current path: '/{export_path}/", 20, 20, 20, rl.LIGHTGRAY)
        #draw text box
        rl.draw_rectangle(20, 60, 760, 60, rl.GRAY)
        if text_box_text == "":
            rl.draw_text("Paste with CTRL V", 25, 65, 30, rl.DARKGRAY)
        else:
            rl.draw_text(text_box_text, 25, 65, 30, rl.LIGHTGRAY)
        if rl.check_collision_point_rec(rl.Vector2(rl.get_mouse_x(),rl.get_mouse_y()), rl.Rectangle(20, 60, 760, 60)) and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            text_box_active = True
        elif rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            text_box_active = False
        
        if text_box_active:
            if rl.is_key_pressed(rl.KEY_BACKSPACE):
                text_box_text = ""
            else:
                if rl.is_key_pressed(rl.KEY_V) and rl.is_key_down(rl.KEY_LEFT_CONTROL):
                    setup_clipboard = rl.get_clipboard_text()
                    # if link contains & nuke it and everything after
                    setup_clipboard = setup_clipboard.split("&")[0]
                    text_box_text = setup_clipboard

        #draw button for dlp export
        rl.draw_rectangle(20, 140, 200, 50, rl.GRAY)
        rl.draw_text("Download Video", 30, 150, 20, rl.DARKGRAY)
        if rl.check_collision_point_rec(rl.Vector2(rl.get_mouse_x(),rl.get_mouse_y()), rl.Rectangle(20, 140, 200, 50)) and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            if text_box_text != "":
                print("downloading")
                subprocess.run([
                    "yt-dlp",
                    "-f", "best",
                    "-o", f"{export_path}/%(title)s.%(ext)s",
                    text_box_text
                ])
                
        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()