import tkinter as tk
import streamlit as st
import time
import winsound  # Windows専用（音を鳴らす）

work_time =25*60
break_time=5*60
remaining_seconds=0
set_count=0
sum_time=0
a = 0
 

def start_pomodoro():
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    restart_button.config(state="disabled")
    root.config(bg="cyan")
    a=0
    label.config(text="作業中...ファイト！")
    countdown(work_time, Break_time)

def Break_time():
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    restart_button.config(state="disabled")
    root.config(bg="lightpink")
    winsound.Beep(1000,500)
    label.config(text="休憩中...おつかれ！")
    countdown(break_time,finish)

def finish():
    global set_count , sum_time 
    start_button.config(state="normal")
    stop_button.config(state="disabled")
    restart_button.config(state="disabled")
    root.config(bg="lightgreen") 
    set_count += 1
    sum_time += 25
    winsound.Beep(1000,500)
    label.config(text="次にいこう！")
    start_button.config(text="もう１回")
    set_label.config(text=f"セット回数：{set_count}回，合計時間{sum_time}分")
    


def countdown(seconds, next_action):
    global remaining_seconds
    remaining_seconds = seconds
    run_countdown(next_action)
    
def run_countdown(next_action):
    global a, remaining_seconds

    if a == 1:
        label.config(text="止まっています")
        return  # 🔹 ここで止める！再呼び出ししない！

    mins, secs = divmod(remaining_seconds, 60)
    timer_text = f"{mins:02d}:{secs:02d}"
    time_display.config(text=timer_text)

    if remaining_seconds > 0:
        remaining_seconds -= 1
        root.after(1000, lambda: run_countdown(next_action))
    else:
        next_action()
            
def stop_pomodoro():
    global a
    start_button.config(state="disabled")
    stop_button.config(state="disabled")
    restart_button.config(state="normal")
    a = 1


def restart_pomodoro():
    global a
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    restart_button.config(state="disabled")
    a = 0
    current_bg=root.cget("bg")
    if current_bg == "cyan" :
        label.config(text="作業中...ファイト！")
        run_countdown(Break_time)
    else:
        label.config(text="休憩中...おつかれ！")
        run_countdown(finish)


root = tk.Tk()
root.title("ポモドーロタイマー")

label = tk.Label(root, text="スタートを押してね", font=("Helvetica", 16))
label.pack(pady=10)

set_label = tk.Label(root, text="セット回数：0回，合計時間：0分", font=("Helvetica", 14))
set_label.pack()

time_display = tk.Label(root, text="25:00", font=("Helvetica", 48))
time_display.pack(pady=10)

start_button = tk.Button(root, text="作業開始", command=start_pomodoro)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="一時停止", command=stop_pomodoro)
stop_button.pack(pady=10)

restart_button = tk.Button(root, text="再開", command=restart_pomodoro)
restart_button.pack(pady=10)

root.mainloop()
