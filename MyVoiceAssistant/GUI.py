from tkinter import *
import time
import subprocess

root = Tk()
root.minsize(780, 450)
root.maxsize(780, 450)
root.config(bg='black')
root.title('Voice Assistant')

# Load background image
img = PhotoImage(file='D:\\New folder\\__pycache__\\background.png', master=root)
img_label = Label(root, image=img)
img_label.place(x=0, y=0)

# Create label to display digital clock
clock_label = Label(root, font=('Arial', 40), fg='#f70521', bg='#34084a')
clock_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Define function to update digital clock
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Start updating the digital clock
update_clock()
def start_func():
   global p
   p = subprocess.Popen(['python', 'assistant.py'])

def stop_func():
    print("exited")
    p.kill()

is_running = False
def toggle_func():
    global is_running
    if is_running:
        stop_func()
        start_button.config(image=start_button_img)
        is_running = False
    else:
        start_func()
        is_running = True


background_image = PhotoImage(file='D:\\New folder\\__pycache__\\gui.png')

line1 = Label(root, text="Try these commands :-", font=('Arial', 16), fg='white', bg='#2a0238',padx=5,pady=5)
line1.place(relx=1.0, y=20, anchor=NE)

line2 = Label(root, text="current weather....", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=5)
line2.place(relx=1.0, y=65, anchor=NE)

line3 = Label(root, text="play- 'song name'", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=15)
line3.place(relx=1.0, y=95, anchor=NE)

line4 = Label(root, text="google search ....", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=15)
line4.place(relx=1.0, y=125, anchor=NE)

line5 = Label(root, text="speak,fast,normal,slow", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=15)
line5.place(relx=1.0, y=155, anchor=NE)

line6 = Label(root, text="latest news", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=35)
line6.place(relx=1.0, y=185, anchor=NE)

line7 = Label(root, text="toss/flip the coin", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=20)
line7.place(relx=1.0, y=215, anchor=NE)

line8 = Label(root, text="where is (location)", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=10)
line8.place(relx=1.0, y=245, anchor=NE)

line9 = Label(root, text="tell me a joke", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=30)
line9.place(relx=1.0, y=275, anchor=NE)

line10 = Label(root, text="hibernate/shutdown/restart", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=5)
line10.place(relx=1.0, y=305, anchor=NE)

line11 = Label(root, text="change voice", font=('Arial', 12), fg='#f2e230', bg='#2a0238',padx=25)
line11.place(relx=1.0, y=335, anchor=NE)

start_button_img = PhotoImage(file='D:\\New folder\\__pycache__\\Untitled-1.png')
start_button = Button(root, image=start_button_img,height=50,width=180, borderwidth=0, command=toggle_func)
start_button.place(relx=0.5, rely=0.9, anchor=S)

exit_button = Button(root, text="Exit",bg='#2a0238',fg="#f2ea74",font=("cambria",16), command=root.destroy)
exit_button.place(x=10, y=2)


root.mainloop()
