# modules
import time
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# Force fullscreen
#root.attributes("-fullscreen", True)

# Function to write errors locally
def local_log(data):
    with open('log.txt','a+') as f:
        f.write(data + '\n')

# function to send the key data
def write_report(report):   
    #try:
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
    #except:
    #    local_log("Couldn't open USB connection!")

# button press events
def button_click(caller):
    print("Button: {} was clicked, sending keypress".format(caller))

    # Define keys to be 'pressed'
    # a = 00400000
    # b = 00500000
    # USB encodings
    action = {
        "button1":"\0\0\4\0\0\0\0\0",
        "button2":"\0\0\5\0\0\0\0\0",
        "button3":"\0\0\6\0\0\0\0\0",
        "button4":"\0\0\7\0\0\0\0\0",
        "button5":"\0\0\10\0\0\0\0\0",
        "button6":"\0\0\11\0\0\0\0\0"
    }
    # NULL_CHAR*2+chr(4)+NULL_CHAR*5
    time.sleep(1)
    # Call function to send requested keys
    write_report(action[caller])

    # Wait and then clear keys
    time.sleep(0.2)
    write_report("\0\0\0\0\0\0\0\0")


# meh, gonna need a bank of better icons
# load icons
image = Image.open("a.png")
photoa = ImageTk.PhotoImage(image)

image = Image.open("b.png")
photob = ImageTk.PhotoImage(image)

image = Image.open("c.png")
photoc = ImageTk.PhotoImage(image)

image = Image.open("d.png")
photod = ImageTk.PhotoImage(image)

image = Image.open("e.png")
photoe = ImageTk.PhotoImage(image)

image = Image.open("f.png")
photof = ImageTk.PhotoImage(image)



# push buttons to gui and bind lambdas
button1 = tk.Button(root, compound=tk.CENTER, image=photoa, text="", command=lambda: button_click('button1'))
button1.grid(row=0, column=0)

button2 = tk.Button(root, compound=tk.CENTER, image=photob, text="", command=lambda: button_click('button2'))
button2.grid(row=0, column=1)

button3 = tk.Button(root, compound=tk.CENTER, image=photoc, text="", command=lambda: button_click('button3'))
button3.grid(row=0, column=2)

button4 = tk.Button(root, compound=tk.CENTER, image=photod, text="", command=lambda: button_click('button4'))
button4.grid(row=1, column=0)

button5 = tk.Button(root, compound=tk.CENTER, image=photoe, text="", command=lambda: button_click('button5'))
button5.grid(row=1, column=1)

button6 = tk.Button(root, compound=tk.CENTER, image=photof, text="", command=lambda: button_click('button6'))
button6.grid(row=1, column=2)


root.mainloop()