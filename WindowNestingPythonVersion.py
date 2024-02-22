import tkinter as tk
import win32gui
import win32con

def embed_window(parent_handle, child_handle):
    win32gui.SetParent(child_handle, parent_handle)

def get_window_info(hwnd):
    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    return f"{hwnd}: {title if title else class_name}"

def get_all_window_info():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd):
            hwnds.append(get_window_info(hwnd))
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds

def display_window_info(result_text):
    window_info = get_all_window_info()
    result_text.delete(1.0, tk.END)
    for info in window_info:
        result_text.insert(tk.END, info + '\n')

def embed_windows(parent_entry, child_entry, status_label):
    parent_handle = int(parent_entry.get())
    child_handle = int(child_entry.get())
    embed_window(parent_handle, child_handle)
    status_label.config(text="子窗口已嵌套到父窗口中")

def main():
    window = tk.Tk()
    window.title("窗口嵌套程序")

    parent_label = tk.Label(window, text="父窗口句柄：")
    parent_label.pack()

    parent_entry = tk.Entry(window)
    parent_entry.pack()

    child_label = tk.Label(window, text="子窗口句柄：")
    child_label.pack()

    child_entry = tk.Entry(window)
    child_entry.pack()

    embed_button = tk.Button(window, text="嵌套窗口", command=lambda: embed_windows(parent_entry, child_entry, status_label))
    embed_button.pack()

    info_button = tk.Button(window, text="获取窗口信息", command=lambda: display_window_info(result_text))
    info_button.pack()

    result_text = tk.Text(window, height=10, width=50)
    result_text.pack()

    status_label = tk.Label(window, text="")
    status_label.pack()

    # 居中显示所有小部件
    for widget in (parent_label, parent_entry, child_label, child_entry, embed_button, info_button, result_text, status_label):
        widget.pack_configure(anchor="center")

    window.mainloop()

if __name__ == "__main__":
    main()
