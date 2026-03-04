import time
import threading
from pynput import mouse, keyboard

events = []
recording = False
replaying = False
start_time = 0
mouse_listener = None
stop_replay = threading.Event()


def on_move(x, y):
    if recording:
        events.append((time.time() - start_time, "move", (x, y)))


def on_click(x, y, button, pressed):
    if recording:
        events.append((time.time() - start_time, "click", (x, y, button, pressed)))


def on_scroll(x, y, dx, dy):
    if recording:
        events.append((time.time() - start_time, "scroll", (x, y, dx, dy)))


def start_recording():
    global recording, start_time, mouse_listener, events

    events = []
    start_time = time.time()
    recording = True

    mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll,
    )
    mouse_listener.start()
    print("[GRAVANDO] Pressione G para parar...")


def stop_recording():
    global recording, mouse_listener

    recording = False
    if mouse_listener is not None:
        mouse_listener.stop()
        mouse_listener = None
    print(f"[GRAVAÇÃO ENCERRADA] {len(events)} eventos capturados.")


def replay():
    global replaying

    if not events:
        print("[ERRO] Nenhuma gravação disponível. Grave primeiro com G.")
        return

    replaying = True
    stop_replay.clear()
    print(f"[REPRODUZINDO EM LOOP] {len(events)} eventos. Pressione P para parar...")

    ctrl = mouse.Controller()
    loop_count = 0

    while not stop_replay.is_set():
        loop_count += 1
        prev_time = 0

        for timestamp, event_type, data in events:
            if stop_replay.is_set():
                break

            delay = timestamp - prev_time
            if delay > 0:
                stop_replay.wait(delay)
                if stop_replay.is_set():
                    break

            if event_type == "move":
                x, y = data
                ctrl.position = (x, y)
            elif event_type == "click":
                x, y, button, pressed = data
                ctrl.position = (x, y)
                if pressed:
                    ctrl.press(button)
                else:
                    ctrl.release(button)
            elif event_type == "scroll":
                x, y, dx, dy = data
                ctrl.position = (x, y)
                ctrl.scroll(dx, dy)

            prev_time = timestamp

    replaying = False
    print(f"[REPRODUÇÃO ENCERRADA] {loop_count} execuções realizadas.")


def on_key_press(key):
    global recording, replaying

    try:
        char = key.char
    except AttributeError:
        return

    if char == "g":
        if replaying:
            return
        if not recording:
            start_recording()
        else:
            stop_recording()

    elif char == "p":
        if recording:
            return
        if not replaying:
            threading.Thread(target=replay, daemon=True).start()
        else:
            stop_replay.set()


def main():
    print("=== Mouse Recorder ===")
    print("  G  -> Iniciar/Parar gravação")
    print("  P  -> Iniciar/Parar reprodução (loop contínuo)")
    print("  Ctrl+C -> Sair")
    print()

    with keyboard.Listener(on_press=on_key_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[ENCERRADO]")


if __name__ == "__main__":
    main()
