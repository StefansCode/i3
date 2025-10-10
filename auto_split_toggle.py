#!/usr/bin/env python3
import i3ipc

i3 = i3ipc.Connection()

def on_window_new(i3, e):
    ws = i3.get_tree().find_focused().workspace()
    count = len([n for n in ws.leaves() if n.window])  # Fenster zählen
    if count % 2 == 0:
        i3.command("split v")  # gerade → vertikal
    else:
        i3.command("split h")  # ungerade → horizontal

i3.on("window::new", on_window_new)
i3.main()