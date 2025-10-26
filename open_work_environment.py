#!/usr/bin/env python3
import i3ipc
import time

# Verbindung zu i3 herstellen
i3 = i3ipc.Connection()

def wait_for_window(class_name, timeout=15):
    """Warte, bis ein Fenster mit einer bestimmten Klasse auftaucht."""
    start = time.time()
    while time.time() - start < timeout:
        for win in i3.get_tree().leaves():
            if win.window_class and class_name.lower() in win.window_class.lower():
                return win
        time.sleep(0.2)
    return None

def open_workenvironment():
    print("Starting VSCode...")
    i3.command("exec code")
    code_win = wait_for_window("Code")
    if code_win:
        i3.command(f'[con_id="{code_win.id}"] move to workspace number 1')
        print("VSCode window found and moved.")

    print("Starting Firefox...")
    i3.command("exec firefox")
    ff_win = wait_for_window("Firefox")
    if ff_win:
        i3.command(f'[con_id="{ff_win.id}"] move to workspace number 2')
        print("Firefox window found and moved.")

    print("Starting Nautilus...")
    i3.command("exec nautilus")
    naut_win = wait_for_window("Nautilus")
    if naut_win:
        i3.command(f'[con_id="{naut_win.id}"] move to workspace number 3')
        print("Nautilus window found and moved.")

    print("Work environment ready 🚀")

if __name__ == "__main__":
    open_workenvironment()