########### Imports ###########
import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer


########### Key Shortcuts ###########
#### Mod Keys ####
super       = "mod4"                                             # Super is the Windows Key
alt         = "mod1"
ctrl        = "control"

#### Special Characters ####
home        = os.path.expanduser('~')

#### Applications ####
browser     = "brave"                                            # Browser
code        = "emacs"                                            # Text Editing
files       = "thunar"                                           # File Manager
logout      = "arcolinux-logout"                                 # Logout Tool
run         = home + '/.config/rofi/Launcher/launcher.sh'        # Run Launcher
taskmanager = "alacritty -e'htop'"                               # Task Manager
terminal    = "alacritty"                                        # Terminal


########### Key Bindings ###########
keys = [
#### Layout Modifications ####
## Switching Between Open Applications ##
# Switch Up
Key([super], "Up", lazy.layout.up()),
# Switch Down
Key([super], "Down", lazy.layout.down()),
# Switch Left
Key([super], "Left", lazy.layout.left()),
# Switch Right
Key([super], "Right", lazy.layout.right()),
# Switch Between Apps
Key([super], "k", lazy.layout.next()),
# Switch Between Apps
Key([super], "j", lazy.layout.next()),
# Switch Between Apps
Key([alt], "Tab", lazy.layout.next()),
## Changing the Size of Open Applications ##
# Increase Size
Key([super], "l",
    lazy.layout.grow_right(),
    lazy.layout.grow(),
    lazy.layout.increase_ratio(),
    lazy.layout.delete(),
    ),
# Decrease Size
Key([super], "h",
    lazy.layout.grow_left(),
    lazy.layout.shrink(),
    lazy.layout.decrease_ratio(),
    lazy.layout.add(),
    ),
## Change the Layout ##
Key([super], "Tab", lazy.next_layout()),
## Toggle Fullscreen ##
Key([super, "shift"], "f", lazy.window.toggle_fullscreen()),
## Toggle Floating ##
Key([super, "shift"], "t", lazy.window.toggle_floating()),

#### Qtile ####
## Exiting and Restarting ##
# Retart Qtile
Key([super, "shift"], "r", lazy.restart()),
# Logout of Qtile
Key([super, "shift"], "q", lazy.shutdown()),
# Closing Applications
Key([super, "shift"], "c", lazy.window.kill()),

#### Applications ####
# Terminal
Key([super], "Return", lazy.spawn(terminal)),
Key([super], "KP_Enter", lazy.spawn(terminal)),
# Browser
Key([alt, "control"], "b", lazy.spawn(browser)),
# Text Editing
Key([alt, "control"], "c", lazy.spawn(code)),
# File Manager
Key([super], "e", lazy.spawn(files)),
# Logout Tool
Key([super], "x", lazy.spawn(logout)),
# X Kill
Key([super], "Escape", lazy.spawn('xkill')),
# Run Launcher
Key([super, "shift"], "Return", lazy.spawn(run)),
# Task Manager
Key([ctrl, "shift"], "Escape", lazy.spawn(taskmanager)),
# ScreenShots
Key([super], "Print", lazy.spawn("scrot 'Screenshot-%Y-%m-%d-%s.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'"))]


########### WorkSpaces ###########
#### WorkSpaces ####
group_names = [("Web", {'layout': 'max'}),
               ("Dev", {'layout': 'max'}),
               ("Sys", {'layout': 'monadtall'}),
               ("Chat", {'layout': 'max'}),
               ("Vbox", {'layout': 'max'}),
               ("Muisc", {'layout': 'max'}),
               ("Video", {'layout': 'max'}),
               ("Misc", {'layout': 'monadtall'})]
## Variable ##
groups = [Group(name, **kwargs) for name, kwargs in group_names]
#### To switch WorkSpaces ####
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([super], str(i), lazy.group[name].toscreen()))       
    keys.append(Key([super, "shift"], str(i), lazy.window.togroup(name)))


########### layouts ###########
layouts = [
    layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Floating(border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Max()]


########### Move Apps Automatically To Workspaces ###########
@hook.subscribe.client_new
def assign_app_group(client):
     d = {}
     #####################################################################################
     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
     #####################################################################################
     d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
     d[group_names[1]] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
     d[group_names[2]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
     d[group_names[3]] = ["Gimp", "gimp" ]
     d[group_names[4]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
     d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
     d[group_names[6]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
               "virtualbox manager", "virtualbox machine", "vmplayer", ]
     d[group_names[7]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
     d[group_names[8]] = ["Evolution", "Geary", "Mail", "Thunderbird",
               "evolution", "geary", "mail", "thunderbird" ]
     d[group_names[9]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
     ######################################################################################

wm_class = client.window.get_wm_class()[0]

for i in range(len(d)):
    if wm_class in list(d.values())[i]:
        group = list(d.keys())[i]
        client.togroup(group)
        client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


# COLORS FOR THE BAR

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()




# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = -1,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               # widget.Net(
               #          font="Noto Sans",
               #          fontsize=12,
               #          interface="enp0s31f6",
               #          foreground=colors[2],
               #          background=colors[1],
               #          padding = 0,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.NetGraph(
               #          font="Noto Sans",
               #          fontsize=12,
               #          bandwidth="down",
               #          interface="auto",
               #          fill_color = colors[8],
               #          foreground=colors[2],
               #          background=colors[1],
               #          graph_color = colors[8],
               #          border_color = colors[2],
               #          padding = 0,
               #          border_width = 1,
               #          line_width = 1,
               #          ),
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # # do not activate in Virtualbox - will break qtile
               # widget.ThermalSensor(
               #          foreground = colors[5],
               #          foreground_alert = colors[6],
               #          background = colors[1],
               #          metric = True,
               #          padding = 3,
               #          threshold = 80
               #          ),
               # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # arcobattery.BatteryIcon(
               #          padding=0,
               #          scale=0.7,
               #          y_poss=2,
               #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
               #          update_interval = 5,
               #          background = colors[1]
               #          ),
               # # battery option 2  from Qtile
               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Battery(
               #          font="Noto Sans",
               #          update_interval = 10,
               #          fontsize = 12,
               #          foreground = colors[5],
               #          background = colors[1],
	           #          ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[6],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.CPUGraph(
                        border_color = colors[2],
                        fill_color = colors[8],
                        graph_color = colors[8],
                        background=colors[1],
                        border_width = 1,
                        line_width = 1,
                        core = "all",
                        type = "box"
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[4],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed}M/{MemTotal}M',
                        update_interval = 1,
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        fontsize=16
                        ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 12,
                        format="%Y-%m-%d %H:%M"
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([super], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([super], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
