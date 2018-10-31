from driver import Driver

if __name__ == "__main__":
    d = Driver()

    while True:
        d.menu_controller.updateView()
        key = d.menu_controller.getUserInput()
        d.keyPressed(key)
