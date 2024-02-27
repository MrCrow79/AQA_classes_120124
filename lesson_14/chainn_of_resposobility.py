# Chain of Responsibility
# UI tests

class UIWindow:

    def open_window(self):
        print('Open window')
        return self

    def get_panel(self):
        print('return panel object')
        return self

    def get_sub_panel(self):
        print('return sub panel object')
        return self

    def click_button(self):
        print('Click button')
        return self

    def click_button2(self):
        print('Click button')
        return UIWindow()


# class HomePage():
#
#     def __init__(self):
#         self.locator = find_element('...')  # var 1
#         self.text_of_button = 'button_id'  # var 2
#         self.some_title = 'soem_title'  # var 2
#
#     def click_button(self):
#         find_element(self.text_of_button).click()
#         return self
#
#     def find_title_of_new_page(self):
#         find_element(self.some_title)
#
#
# class TestHomePage():
#
#     def setup_method(self):
#         self.home_page = HomePage()
#
#     def test_click_button(self):
#         self.home_page.click_button().find_title_of_new_page()


ui_window = UIWindow()

ui_window.open_window().get_panel().get_sub_panel().click_button()
# the same
ui_window.open_window()
ui_window.get_panel()
ui_window.get_sub_panel()
ui_window.click_button()
new_ui_window = ui_window.click_button2()

print(id(new_ui_window))
print(id(ui_window))

new_ui_window.open_window().get_panel().get_sub_panel().click_button()

#  Приклад на вбудованих функціях
#  print('asdasdasd'.replace('a', 'b').replace('s', 'x'))