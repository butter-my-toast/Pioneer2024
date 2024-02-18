import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import time

class TimerT():
    def __init__(self, container, btn_timer, btn_set_timer):
        self.container = container

        self.btn_timer = btn_timer
        self.btn_set_timer = btn_set_timer
        

        self.timer_on = False
        self.timer_paused = False
        self.timer_start_time = None

    def set_label(self, timer_label):
       self.timer_label = timer_label

    def get_label(self):
        return self.timer_label

    def timer_btn_press(self):
        # If the timer rn is running
        if self.timer_on:
            self.stop_timer()
        else:
            self.start_timer()

    def update_timer(self):
        if not self.timer_start_time:
            return
        elapsed_time = time.time() - self.timer_start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = (seconds - int(seconds)) * 1000
        self.timer_label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds):03}")

    def start_timer(self):
        self.timer_on = True
        self.timer_start_time = time.time()
        self.btn_timer.config(text="Stop Timer")

        # Create the Timer Pause Button
        self.btn_timer_pause = ttk.Button(self.container, text="Pause Timer", command=self.pause_timer)
        self.btn_timer_pause.pack(side=tk.LEFT, padx=5, pady=5)
        self.timer_paused = False

    def stop_timer(self):
        self.timer_on = False
        self.btn_timer.config(text="Start Timer")
        self.btn_timer_pause.destroy()

        self.timer_label.config(text="Timer Text")

    def pause_timer(self):
        print("asfd")
        self.timer_paused = True
        self.btn_timer_pause.config(text="Unpause Timer", command=self.unpause_timer)

    def unpause_timer(self):
        self.timer_paused = False
        self.btn_timer_pause.config(text="Pause Timer", command=self.pause_timer)


    def set_timer(self):
        pass
