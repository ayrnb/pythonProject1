card_list = []


def show_menu():
    """显示菜单
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0\n1. 新建名片\n2. 显示全部\n3. 查询名片\n\n0. 退出系统")
    print("*" * 50)


def new_card():
    """新建名片
    """
    print("-" * 50)
    print("功能：新建名片")
    name = input("输入您的姓名")
    phone = input("输入您的电话")
    qq = input("输入您的QQ")
    email = input("输入您的email")
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    card_list.append(card_dict)
    print("新建的名片为%s" % card_dict["name"])


def show_all():
    """显示全部
    """
    print("-" * 50)
    print("功能：显示全部")
    if len(card_list) == 0:
        print("名片夹中没有名片")
        return
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分隔线
    print("=" * 50)

    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片
    """
    print("-" * 50)
    print("功能：搜索名片")
    if len(card_list) == 0:
        print("名片夹中没有名片")
        return
    findname = input("请输入要搜索的名字")
    for card_dict in card_list:
        if card_dict["name"] == findname:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-" * 40)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            print("-" * 40)
            break
        else:
            print("没有%s的名片"%findname)
