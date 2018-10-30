from user_controller import UserController
from driver import Driver

if __name__ == "__main__":
    # m = Menu("sample")
    # uc = UserController()
    # uc.updateView()
    d = Driver()
    d.user_controller.updateView()

    d.menu_controller.updateView()


