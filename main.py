def show_menu():
    print("""
========================
      Study Tracker
========================
欢迎使用Study Tracker
1. 添加学习记录
2. 查看学习记录
3. 退出

请选择：""", end="")


show_menu()
choice = input()

if choice == "1":
    study_content = input("请输入今天学习内容：")
    study_time = input("请输入今天学习时间：")
    print("今天学习内容：", study_content)
    print("今天学习时间：", study_time, "继续加油")
elif choice == "2":
    print("查看学习记录")
elif choice == "3":
    print("已退出")
else:
    print("无效选项，请重新输入。")