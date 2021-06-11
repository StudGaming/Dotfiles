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
super       = "mod4"
alt         = "mod1"
ctrl        = "control"
home        = os.path.expanduser('~')
run         = home + '/.config/rofi/Launcher/launcher.sh'
logout      = "arcolinux-logout"


keys = [

# FUNCTION KEYS

    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

# SUPER + FUNCTION KEYS

    Key([super], "e", lazy.spawn('atom')),
    Key([super], "c", lazy.spawn('conky-toggle')),
    Key([super], "f", lazy.window.toggle_fullscreen()),
    Key([super], "m", lazy.spawn('pragha')),
    Key([super], "q", lazy.window.kill()),
    Key([super], "r", lazy.spawn('rofi-theme-selector')),
    Key([super], "t", lazy.spawn('termite')),
    Key([super], "v", lazy.spawn('pavucontrol')),
    Key([super], "w", lazy.spawn('vivaldi-stable')),
    Key([super], "x", lazy.spawn(logout)),
    Key([super], "Escape", lazy.spawn('xkill')),
    Key([super], "Return", lazy.spawn('alacritty')),
    Key([super], "KP_Enter", lazy.spawn('termite')),
    Key([super], "F1", lazy.spawn('vivaldi-stable')),
    Key([super], "F2", lazy.spawn('atom')),
    Key([super], "F3", lazy.spawn('inkscape')),
    Key([super], "F4", lazy.spawn('gimp')),
    Key([super], "F5", lazy.spawn('meld')),
    Key([super], "F6", lazy.spawn('vlc --video-on-top')),
    Key([super], "F7", lazy.spawn('virtualbox')),
    Key([super], "F8", lazy.spawn('thunar')),
    Key([super], "F9", lazy.spawn('evolution')),
    Key([super], "F10", lazy.spawn("spotify")),
    Key([super], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([super], "F12", lazy.spawn('rofi -show run')),

# SUPER + SHIFT KEYS

    Key([super, "shift"], "Return", lazy.spawn('thunar')),
    Key([super, "shift"], "p", lazy.spawn(run)),
    Key([super, "shift"], "q", lazy.window.kill()),
    Key([super, "shift"], "r", lazy.restart()),
    Key([super, ctrl], "r", lazy.restart()),
    # Key([super, "shift"], "x", lazy.shutdown()),

# ctrl + ALT KEYS

    Key([alt, ctrl], "Next", lazy.spawn('conky-rotate -n')),
    Key([alt, ctrl], "Prior", lazy.spawn('conky-rotate -p')),
    Key([alt, ctrl], "a", lazy.spawn('xfce4-appfinder')),
    Key([alt, ctrl], "b", lazy.spawn('thunar')),
    Key([alt, ctrl], "c", lazy.spawn('catfish')),
    Key([alt, ctrl], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key([alt, ctrl], "f", lazy.spawn('firefox')),
    Key([alt, ctrl], "g", lazy.spawn('chromium -no-default-browser-check')),
    Key([alt, ctrl], "i", lazy.spawn('nitrogen')),
    Key([alt, ctrl], "k", lazy.spawn('slimlock')),
    Key([alt, ctrl], "m", lazy.spawn('xfce4-settings-manager')),
    Key([alt, ctrl], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key([alt, ctrl], "p", lazy.spawn('pamac-manager')),
    Key([alt, ctrl], "r", lazy.spawn('rofi-theme-selector')),
    Key([alt, ctrl], "s", lazy.spawn('spotify')),
    Key([alt, ctrl], "t", lazy.spawn('termite')),
    Key([alt, ctrl], "u", lazy.spawn('pavucontrol')),
    Key([alt, ctrl], "v", lazy.spawn('vivaldi-stable')),
    Key([alt, ctrl], "w", lazy.spawn('arcolinux-welcome-app')),
    Key([alt, ctrl], "Return", lazy.spawn('termite')),

# ALT + ... KEYS

    Key([alt], "k", lazy.spawn('slimlock')),
    Key([alt], "f", lazy.spawn('variety -f')),
    Key([alt], "h", lazy.spawn('urxvt -e htop')),
    Key([alt], "n", lazy.spawn('variety -n')),
    Key([alt], "p", lazy.spawn('variety -p')),
    Key([alt], "t", lazy.spawn('variety -t')),
    Key([alt], "Up", lazy.spawn('variety --pause')),
    Key([alt], "Down", lazy.spawn('variety --resume')),
    Key([alt], "Left", lazy.spawn('variety -p')),
    Key([alt], "Right", lazy.spawn('variety -n')),
    Key([alt], "F2", lazy.spawn('gmrun')),
    Key([alt], "F3", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    Key([alt, "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    Key([alt, "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    Key([alt, "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    Key([alt, "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# ctrl + SHIFT KEYS

    Key([ctrl, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([ctrl], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([ctrl, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([super], "n", lazy.layout.normalize()),
    Key([super], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([super], "Up", lazy.layout.up()),
    Key([super], "Down", lazy.layout.down()),
    Key([super], "Left", lazy.layout.left()),
    Key([super], "Right", lazy.layout.right()),
    Key([super], "k", lazy.layout.up()),
    Key([super], "j", lazy.layout.down()),
    Key([super], "h", lazy.layout.left()),
    Key([super], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([super, ctrl], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([super, ctrl], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([super, ctrl], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([super, ctrl], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([super, ctrl], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([super, ctrl], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([super, ctrl], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([super, ctrl], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([super, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([super, alt], "k", lazy.layout.flip_up()),
    Key([super, alt], "j", lazy.layout.flip_down()),
    Key([super, alt], "l", lazy.layout.flip_right()),
    Key([super, alt], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([super, "shift"], "k", lazy.layout.shuffle_up()),
    Key([super, "shift"], "j", lazy.layout.shuffle_down()),
    Key([super, "shift"], "h", lazy.layout.shuffle_left()),
    Key([super, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([super, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([super, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([super, "shift"], "Left", lazy.layout.swap_left()),
    Key([super, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([super, "shift"], "space", lazy.window.toggle_floating()),]


group_names = [("Web", {'layout': 'max'}),
               ("Dev", {'layout': 'max'}),
               ("Sys", {'layout': 'monadtall'}),
               ("Chat", {'layout': 'max'}),
               ("Vbox", {'layout': 'max'}),
               ("Muisc", {'layout': 'max'}),
               ("Video", {'layout': 'max'}),
               ("Misc", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([super], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([super, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]

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
