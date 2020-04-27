property_list = []

def show_menu():
    """
    显示欢迎页面及功能
    """
    print("*"*50)
    print("欢迎使用【资产管理系统】V1.0")
    print("")
    print("1.新增资产")
    print("2.显示全部")
    print("3.查询资产")
    print("")
    print("0.退出系统")
    print("*"*50)

def new_property():
    """新增资产"""
    print("*"*50)
    print("新增资产")

    #提示用户输入相关信息，并保存在变量中
    department_str = input("请输入部门：")
    room_str = input("请输入房间：")
    name_str = input("请输入姓名：")
    computer_str = input("请输入电脑型号：")
    IPAddress_str = input("请输入IP地址：")
    MACAddress_str = input("请输入MAC地址：")

    #将用户输入的内容保存在字典里
    property_dict = {"department": department_str,
                     "room": room_str,
                     "name": name_str,
                     "computer": computer_str,
                     "IP": IPAddress_str,
                     "MAC":MACAddress_str}
    #将字典添加进列表
    property_list.append(property_dict)
    print("添加%s的资产成功" % name_str)

def show_all():
    """显示所有资产信息"""
    print("-"*50)
    print("显示所有资产")
    """判断是否有资产信息，要是没有让用户新添加"""
    if len(property_list) == 0:
        print("当前没有任何资产信息，请先添加资产")

        return

    for name in ["部门","房间","姓名","电脑型号","IP地址","Mac地址"]:
        print(name,end="\t\t")
    print("")
    #打印分割线
    print("="*50)
    for proerty_dict in property_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" %(proerty_dict["department"],
                                                       proerty_dict["room"],
                                                       proerty_dict["name"],
                                                       proerty_dict["computer"],
                                                       proerty_dict["IP"],
                                                       proerty_dict["MAC"]))

def search_property():
    print("-"*50)
    print("查询资产")

    search_name = input("请输入要查询的姓名：")

    for property_dict in property_list:
        if property_dict["name"] == search_name:
            print("部门\t\t房间\t\t姓名\t\t电脑型号\t\tIP地址\t\tMac地址\t\t")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t" %(property_dict["department"],
                                                           property_dict["room"],
                                                           property_dict["name"],
                                                           property_dict["computer"],
                                                           property_dict["IP"],
                                                           property_dict["MAC"]))
            deal_property(property_dict)


            break

        else:
            print("抱歉，没有找到%s的资产信息"% search_name)

def deal_property(find_property):

    action_str = input("请选择要执行的操作"
          "【1】修改 【2】删除 【0】返回上级菜单")

    if action_str == "1":
        find_property["department"] = input_property_info(find_property["department"],"部门：")
        find_property["room"] = input_property_info(find_property["room"],"房间：")
        find_property["name"] = input_property_info(find_property["name"],"姓名：")
        find_property["computer"] = input_property_info(find_property["computer"],"电脑型号：")
        find_property["IP"] = input_property_info(find_property["IP"],"IP地址：")
        find_property["MAC"] = input_property_info(find_property["MAC"],"Mac地址：")

        print("修改资产信息完成！")

    elif action_str == "2":

        property_list.remove(find_property)

        print("删除资产信息成功！")

def input_property_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    #1。提示用户输入内容
    result_str = input(tip_message)

    #2，针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str

    #3。如果用户没有输入内容，返回字典中原有的值
    else:

        return dict_value




