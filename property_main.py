
import property_tools

while True:
    #显示功能菜单
    property_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是%s "% action_str)

    #使用成员变量in 及if-elif-else判断用户输入否正确，正确则提供相应功能，不正确则重新选择
    if action_str in ["1","2","3"]:

        if action_str == "1":
            property_tools.new_property()

        if action_str == "2":
            property_tools.show_all()

        if action_str == "3":
            property_tools.search_property()

    elif action_str == "0":
        print("欢迎再次使用【资产管理系统】")
        #当用户选择退出功能时，使用break退出循环
        break

    else:
        print("您输入的不正确，请从新选择")