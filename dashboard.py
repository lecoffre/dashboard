import site
from pyvda import AppView, get_apps_by_z_order, VirtualDesktop, get_virtual_desktops
import win32gui, win32con
import os
from selenium import webdriver


dirname = os.path.dirname(__file__)
wallpapers = os.path.join(dirname, 'wallpapers')
w1 = os.path.join(wallpapers, 'kali.png')
w2 = os.path.join(wallpapers, 'windows.png')
w3 = os.path.join(wallpapers, 'wrkspace.png')
dashboard = 'http://127.0.0.1:8000/'

number_of_active_desktops = len(get_virtual_desktops())
print(f"{number_of_active_desktops} active desktops")

if number_of_active_desktops == 1 :
    VirtualDesktop.create()
elif number_of_active_desktops == 2 :
    VirtualDesktop.create()
    VirtualDesktop.create()

target_desktop = VirtualDesktop(2)
current_window = AppView.current()
current_window.move(target_desktop)


if number_of_active_desktops > 3 : 
    for vd in get_virtual_desktops()[3:len(get_virtual_desktops())]:
        for app in vd.apps_by_z_order():
            app.unpin()
        vd.remove()

for app in VirtualDesktop(3).apps_by_z_order():
    win32gui.PostMessage(app.hwnd,win32con.WM_CLOSE,0,0)
    #app.unpin()
VirtualDesktop(1).set_wallpaper(w1)
VirtualDesktop(2).set_wallpaper(w2)
VirtualDesktop(3).set_wallpaper(w3)




VirtualDesktop(3).go()
options = webdriver.ChromeOptions()
#options.add_argument("--kiosk")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(executable_path=r'dashboard/chromedriver.exe', chrome_options=options)



#start the react app

driver.get(dashboard)
driver.fullscreen_window()


"""
#open a new tab for notion
driver.execute_script("window.open('');")
# Switch to the new window and open URL B
driver.switch_to.window(driver.window_handles[1])
driver.get("https://notion.so")
# …Do something here
print("Current Page Title is : %s" %driver.title)


driver.switch_to.window(driver.window_handles[0])
print("Current Page Title is : %s" %driver.title)
"""


