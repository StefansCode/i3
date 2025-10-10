# My current i3 config
This is mainly a backup for when I want to reinstall Linux or when I want to use it on another device.


# Overview of all bindsym in this i3 config

## i3 config shortcuts
| Key Combination   | Command             | Description                   |
|------------------|----------------------|-------------------------------|
| $mod+Shift+c     | reload               | Reload i3 config              |
| $mod+Shift+r     | restart              | Restart i3                    |
| $mod+Shift+e     | exec "i3-nagbar ..." | Exit i3 (with confirmation)   |

## Application shortcuts
| Key Combination | Command                        | Description           |
|-----------------|--------------------------------|-----------------------|
| $mod+d          | exec --no-startup-id dmenu_run | Open program launcher |
| $mod+Return     | exec i3-sensible-terminal      | Open terminal         |

## Set fn keys
| Key Combination      | Command                          | Description                       |
|----------------------|----------------------------------|-----------------------------------|
| XF86MonBrightnessDown| exec brightnessctl set 10%-      | Decrease screen brightness        |
| XF86MonBrightnessUp  | exec brightnessctl set +10%      | Increase screen brightness        |
| XF86AudioMute        | exec amixer sset 'Master' toggle | Mute/unmute audio                 |
| XF86AudioLowerVolume | exec amixer sset 'Master' 5%-    | Decrease volume                   |
| XF86AudioRaiseVolume | exec amixer sset 'Master' 5%+    | Increase volume                   |

## Window management
### Change focus
| Key Combination  | Command      | Description                      |
|------------------|--------------|----------------------------------|
| $mod+Shift+q     | kill         | Close window                     |
| $mod+Left        | focus left   | Focus left (arrow key)           |
| $mod+Down        | focus down   | Focus down (arrow key)           |
| $mod+Up          | focus up     | Focus up (arrow key)             |
| $mod+Right       | focus right  | Focus right (arrow key)          |
| $mod+a           | focus parent | Focus parent container           |

### Move windows
| Key Combination     | Command      | Description                      |
|---------------------|--------------|----------------------------------|
| $mod+Shift+Left     | move left    | Move window left (arrow key)     |
| $mod+Shift+Down     | move down    | Move window down (arrow key)     |
| $mod+Shift+Up       | move up      | Move window up (arrow key)       |
| $mod+Shift+Right    | move right   | Move window right (arrow key)    |

### Layout
| Key Combination  | Command             | Description                      |
|------------------|---------------------|----------------------------------|
| $mod+h           | split h             | Split horizontally               |
| $mod+v           | split v             | Split vertically                 |
| $mod+f           | fullscreen toggle   | Toggle fullscreen                |
| $mod+s           | layout stacking     | Stacked window layout            |
| $mod+w           | layout tabbed       | Tabbed window layout             |
| $mod+e           | layout toggle split | Toggle split layout              |
| $mod+Shift+space | floating toggle     | Toggle floating/tiling window    |
| $mod+space       | focus mode_toggle   | Toggle focus between modes       |

### Resize mode
| Key Combination           | Command                   | Description                      |
|---------------------------|---------------------------|----------------------------------|
| $mod+r                    | mode "resize"             | Enter resize mode                |

#### Key Combination in resize mode:

| Key Combination     | Command                   | Description                      |
|---------------------|---------------------------|----------------------------------|
| Left                | resize shrink width 10 px | Decrease window width            |
| Down                | resize grow height 10 px  | Increase window height           |
| Up                  | resize shrink height 10 px| Decrease window height           |
| Right               | resize grow width 10 px   | Increase window width            |
| Return              | mode "default"            | Exit resize mode                 |
| Escape              | mode "default"            | Exit resize mode                 |
| $mod+r              | mode "default"            | Exit resize mode                 |

## Workspace management
| Key Combination    | Command                                   | Description                  |
|--------------------|-------------------------------------------|------------------------------|
| $mod+1             | workspace number $ws1                     | Switch to workspace 1 (also works for 2-9) |
| $mod+Shift+1       | move container to ws $ws1; workspace $ws1 | Move window to WS 1 and go there (also works for 2-9) |
| $mod+Control+Right | workspace next                            | Switch to next workspace     |
| $mod+Control+Left  | workspace prev                            | Switch to previous workspace |

## Power management
| Key Combination          | Command                         | Description                      |
|--------------------------|---------------------------------|----------------------------------|
| $mod+Escape              | mode "shift+s = shutdown...     | Open power mode                  |

#### Key Combination in power mode:
 
| Key Combination   | Command                         | Description                      |
|-------------------|---------------------------------|----------------------------------|
| Shift+s           | exec shutdown now               | Shut down                        |
| r                 | exec reboot                     | Reboot                           |
| l                 | exec --no-startup-id i3lock ... | Lock screen (i3lock-color)       |
| Escape            | mode "default"                  | Exit power mode                  |
| $mod+Escape       | mode "default"                  | Exit power mode                  |

# Notes
- odiaeresis is the keycode for ö.

# TODE
- Add the remaining fn keys.
- Fix auto_split_toggle, because I just did something to disable it. I also need to figure out what it was.