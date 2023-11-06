import tkinter as tk

# 定义一个处理函数
def process_input():
    user_input = input_entry.get()  # 获取文本框中的输入数据
    result_label.config(text=f"你输入的数据是：{user_input}")  # 显示处理结果

# 创建主窗口
root = tk.Tk()
root.title("居中显示的UI示例")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小和位置
window_width = 400
window_height = 200
x = (screen_width - window_width) // 2  # 计算窗口的水平位置
y = (screen_height - window_height) // 2  # 计算窗口的垂直位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 创建标签
label = tk.Label(root, text="请输入数据:")
label.pack()

# 创建文本输入框
input_entry = tk.Entry(root)
input_entry.pack()

# 创建按钮并关联处理函数
process_button = tk.Button(root, text="处理", command=process_input)
process_button.pack()

# 创建用于显示结果的标签
result_label = tk.Label(root, text="")
result_label.pack()

# 运行主循环
root.mainloop()
