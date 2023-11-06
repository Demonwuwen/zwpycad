import tkinter as tk


# 定义一个处理函数
def process_input():
    user_input1 = input_entry1.get()
    user_input2 = input_entry2.get()
    user_input3 = input_entry3.get()

    result_label.config(text=f"输入1：{user_input1}\n输入2：{user_input2}\n输入3：{user_input3}")


# 创建主窗口
root = tk.Tk()
root.title("多个数据输入的UI示例")


# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#设置窗口大小和位置
window_width = 400
window_height = 200
x = (screen_width-window_width) //2  #计算窗口水平位置
y = (screen_height-window_height) //2  #计算窗口垂直位置

root.geometry(f"{window_width}x{window_height}+{x}+{y}" )


# 创建标签和文本输入框，并使用grid布局
label1 = tk.Label(root, text="输入1:")
label1.grid(row=0, column=0, padx=10, pady=5)

input_entry1 = tk.Entry(root)
input_entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="输入2:")
label2.grid(row=1, column=0, padx=10, pady=5)

input_entry2 = tk.Entry(root)
input_entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = tk.Label(root, text="输入3:")
label3.grid(row=2, column=0, padx=10, pady=5)

input_entry3 = tk.Entry(root)
input_entry3.grid(row=2, column=1, padx=10, pady=5)

# 创建按钮并关联处理函数
process_button = tk.Button(root, text="处理", command=process_input)
process_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 创建用于显示结果的标签
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# 运行主循环
root.mainloop()
