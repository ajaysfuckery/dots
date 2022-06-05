#   ╋╋┏┓
#   ┏┳┫┗┳━┓ Name: XTC's QTile config
#   ┣┃┫┏┫━┫ Version: 1.0
#   ┗┻┻━┻━┛ Github: https://github.com/ajaysfuckery

import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# my applications and variables
mod = "mod4"
terminal = "alacritty"
backupTerm = "xfce4-terminal"
fileManager = "thunar"
browser = "firefox"
social = "telegram-desktop"
notes = "obsidian"
music = "spotify"
editor = "atom"
programLauncher = "rofi -modi drun -show drun -line-padding 4 -columns 2 -padding 50 -hide-scrollbar -terminal xfce4-terminal -show-icons -drun-icon-theme 'Papirus-Dark' -font 'Noto Sans Regular 10'"
office1 = "libreoffice"
office2 = "onlyoffice-desktopeditors"

# Launch autostart script
home = os.path.expanduser("~")
subprocess.call([home + "/.config/qtile/autostart.sh"])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Application Keybindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch Alacritty"),
    Key([mod], "x", "t", lazy.spawn(backupTerm), desc="Launch xfce term"),
    Key([mod, "shift"], "Return", lazy.spawn(fileManager), desc="Launch thunar"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch firefox"),
    Key([mod], "t", lazy.spawn(social), desc="Launch telegram"),
    Key([mod], "o", lazy.spawn(notes), desc="Launch obsidian"),
    Key([mod], "s", lazy.spawn(music), desc="Launch spotify"),
    Key([mod], "e", lazy.spawn(editor), desc="Launch atom"),
    Key([mod, "shift"], "l", lazy.spawn(office1), desc="Launch Libreoffice"),
    Key([mod, "shift"], "o", lazy.spawn(office2), desc="Launch Onlyoffice"),

    # Switch focus between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus right"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus to another window"),

    # Move focused window
    Key([mod, "shift"], "Left", lazy.shuffle_left(), desc="Move focused window left"),
    Key([mod, "shift"], "Right", lazy.shuffle_right(), desc="Move focused window right"),
    Key([mod, "shift"], "Up", lazy.shuffle_up(), desc="Move focused window up"),
    Key([mod, "shift"], "Down", lazy.shuffle_down(), desc="Move focused window up"),

    # Grow windows
    Key([mod, "control"], "Left", lazy.grow_left(), desc="Grow window left"),
    Key([mod, "control"], "Right", lazy.grow_right(), desc="Grow window right"),
    Key([mod, "control"], "Up", lazy.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Down", lazy.grow_down(), desc="Grow window down"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit
    # Split = all windows displayed
    # Unsplit = 1 Window displayed
    Key([mod, "shift"], "s", lazy.layout.toggle_split(), desc="Toggle split/unsplit"),

    # Toggle between different layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill focused window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Reload QTile config
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    # Exit qtile with other options
    Key([mod], "x", lazy.spawn("archlinux-logout"), desc="Launch archlinux-logout"),

    # ROFI (Program Launcher)
    Key([mod, "shift"], "d", lazy.spawn(programLauncher), desc="Launch rofi drun"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

            # Move focused window to another workspace and change to said workspace
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to another group {}".format(i.name)),
        ]
)

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("xtc's config", name="default"),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#     ),
# ]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
