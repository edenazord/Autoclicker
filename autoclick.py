
import time
import pyautogui
from pynput import mouse

# Variabile che tiene traccia dello stato (attivo o disattivo) dell'auto-click
auto_click_enabled = False

def on_click(x, y, button, pressed):
    """
    Callback chiamata ogni volta che viene cliccato un pulsante del mouse.
    x, y -> coordinate del mouse
    button -> bottone premuto (es: mouse.Button.left)
    pressed -> True se il pulsante viene premuto, False se viene rilasciato
    """
    global auto_click_enabled

    # Verifichiamo che si tratti del tasto sinistro e che l'evento sia "pressed"
    if button == mouse.Button.right and pressed:
        # Invertiamo lo stato dell'auto-click (toggle)
        auto_click_enabled = not auto_click_enabled
        if auto_click_enabled:
            print("Auto-click ATTIVATO")
        else:
            print("Auto-click DISATTIVATO")

# Creiamo un listener per gli eventi del mouse
listener = mouse.Listener(on_click=on_click)
listener.start()

try:
    # Ciclo principale: ogni 3 secondi, se auto_click_enabled è True, fa un click
    while True:
        if auto_click_enabled:
            pyautogui.click()
        time.sleep(3)
except KeyboardInterrupt:
    # Permette di chiudere il programma con Ctrl+C
    print("Programma terminato dall'utente.")
finally:
    listener.stop()
