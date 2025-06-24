import socket
import tkinter
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except Exception as ex:
            print("Error Receiving the Message")
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message, "sock: ", sock)

def send():
    msg = my_msg.get()
    my_msg.set("")
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        window.close()


def onClosing():
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat Room")
window.configure(bg="green")

msg_frame = Frame(window, height=100, width=100, bg='red')
msg_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(msg_frame)
msg_list = Listbox(msg_frame, height=14, width=100, bg="cyan", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg='cyan', font='Arial', bg='red')
label.pack()

entryField = Entry(window, textvariable=my_msg, fg='red', width=50)
entryField.pack()
sendButton = Button(window, text="Send", font="Arial", fg='black', command=send)
sendButton.pack()
quitButton = Button(window, text="Quit", font="Arial", fg='black', command=onClosing)
quitButton.pack()



#host = 'localhost'
host = '192.168.0.2'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# message = sock.recv(1024)

# while message:
#     print("Message:", message.decode())
#     message = sock.recv(1024) 
receiveThread = Thread = Thread(target=receive)
receiveThread.start()

mainloop()


    