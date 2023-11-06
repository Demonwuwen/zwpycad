import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# 创建主窗口
root = tk.Tk()
root.title("在UI中显示图片")

# 加载图片并创建PhotoImage对象
image = Image.open("C:\\Users\\demon\\Pictures\\myself\\微信图片_20230516172222.jpg")  # 替换为你的图片路径
photo = ImageTk.PhotoImage(image)

# 创建标签并显示图片
image_label = tk.Label(root, image=photo)
image_label.pack()

# 运行主循环
root.mainloop()
