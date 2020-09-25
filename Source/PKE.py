from tkinter import *
from tkinter import simpledialog, messagebox
from tkinter import ttk
def encrypt(message):
    enmessage = []
    emessage = []
    encrypted = []
    for counter in range(0, len(message)):
        enmessage.append(message[counter])
    
    for cc in enmessage:
        if cc == 'a':
            emessage.append(13)
        elif cc == 'b':
            emessage.append(14)
        elif cc == 'c':
            emessage.append(15)
        elif cc == 'd':
            emessage.append(16)
        elif cc == 'e':
            emessage.append(17)
        elif cc == 'f':
            emessage.append(18)
        elif cc == 'g':
            emessage.append(19)
        elif cc == 'h':
            emessage.append(20)
        elif cc == 'i':
            emessage.append(21)
        elif cc == 'j':
            emessage.append(22)
        elif cc == 'k':
            emessage.append(23)
        elif cc == 'l':
            emessage.append(24)
        elif cc == 'm':
            emessage.append(25)
        elif cc == 'n':
            emessage.append(26)
        elif cc == 'o':
            emessage.append(27)
        elif cc == 'p':
            emessage.append(28)
        elif cc == 'q':
            emessage.append(29)
        elif cc == 'r':
            emessage.append(30)
        elif cc == 's':
            emessage.append(31)
        elif cc == 't':
            emessage.append(32)
        elif cc == 'u':
            emessage.append(33)
        elif cc == 'v':
            emessage.append(34)
        elif cc == 'w':
            emessage.append(35)
        elif cc == 'x':
            emessage.append(36)
        elif cc == 'y':
            emessage.append(37)
        elif cc == 'z':
            emessage.append(38)
        elif cc == '1':
            emessage.append(3)
        elif cc == '2':
            emessage.append(4)
        elif cc == '3':
            emessage.append(5)
        elif cc == '4':
            emessage.append(6)
        elif cc == '5':
            emessage.append(7)
        elif cc == '6':
            emessage.append(8)
        elif cc == '7':
            emessage.append(9)
        elif cc == '8':
            emessage.append(10)
        elif cc == '9':
            emessage.append(11)
        elif cc == '0':
            emessage.append(12)
        elif cc == ' ':
            emessage.append(39)
        elif cc == '.':
            emessage.append(40)
        elif cc == ',':
            emessage.append(41)
        elif cc == ':':
            emessage.append(42)
        elif cc == '!':
            emessage.append(43)
        elif cc == '?':
            emessage.append(44)

    for thing in emessage:
        quotent = (thing**e)/(p*q)
        round_quotent = round(quotent)
        if round_quotent > quotent:
            round_quotent = round_quotent-1
        encrypted_char = round((quotent - round_quotent)*(p*q))
        encrypted.append(encrypted_char)
    return encrypted


def decrypt(message):
    demessage = []
    dmessage = []
    decrypted = []
    data = message.split()
    for temp in data:
        temp = int(temp)
        demessage.append(temp)
    for thing in demessage:
        quotent = (thing**d)/(p*q)
        round_quotent = round(quotent)
        if round_quotent > quotent:
            round_quotent = round_quotent-1
        decrypted_char = round((quotent - round_quotent)*(p*q))
        dmessage.append(decrypted_char)
    for cc in dmessage:
        if cc == 3:
            decrypted.append('1')
        if cc == 4:
            decrypted.append('2')
        if cc == 5:
            decrypted.append('3')
        if cc == 6:
            decrypted.append('4')
        if cc == 7:
            decrypted.append('5')
        if cc == 8:
            decrypted.append('6')
        if cc == 9:
            decrypted.append('7')
        if cc == 10:
            decrypted.append('8')
        if cc == 11:
            decrypted.append('9')
        if cc == 12:
            decrypted.append('0')
        if cc == 13:
            decrypted.append('a')
        if cc == 14:
            decrypted.append('b')
        if cc == 15:
            decrypted.append('c')
        if cc == 16:
            decrypted.append('d')
        if cc == 17:
            decrypted.append('e')
        if cc == 18:
            decrypted.append('f')
        if cc == 19:
            decrypted.append('g')
        if cc == 20:
            decrypted.append('h')
        if cc == 21:
            decrypted.append('i')
        if cc == 22:
            decrypted.append('j')
        if cc == 23:
            decrypted.append('k')
        if cc == 24:
            decrypted.append('l')
        if cc == 25:
            decrypted.append('m')
        if cc == 26:
            decrypted.append('n')
        if cc == 27:
            decrypted.append('o')
        if cc == 28:
            decrypted.append('p')
        if cc == 29:
            decrypted.append('q')
        if cc == 30:
            decrypted.append('r')
        if cc == 31:
            decrypted.append('s')
        if cc == 32:
            decrypted.append('t')
        if cc == 33:
            decrypted.append('u')
        if cc == 34:
            decrypted.append('v')
        if cc == 35:
            decrypted.append('w')
        if cc == 36:
            decrypted.append('x')
        if cc == 37:
            decrypted.append('y')
        if cc == 38:
            decrypted.append('z')
        if cc == 39:
            decrypted.append(' ')
        if cc == 40:
            decrypted.append('.')
        if cc == 41:
            decrypted.append(',')
        if cc == 42:
            decrypted.append(':')
        if cc == 43:
            decrypted.append('!')
        if cc == 44:
            decrypted.append('?')

    plaintext = ''.join(decrypted)       
    return plaintext
    
    
        

def get_task():
    task = simpledialog.askstring('Task', 'What do you want to do?  Type exit to exit.')
    return task

def get_messag():
    messag = simpledialog.askstring('Message', 'Enter what you want to encrypt: ')
    return messag

def get_message():
    message = simpledialog.askstring('Message', 'Enter what you want to decrypt: ')
    return message

def oken():
    outen.destroy()
    loop()
    

def okde():
    outde.destroy()
    loop()

def loop():
    task = get_task()
    if task == 'encrypt':
        messag = get_messag()
        encrypted = encrypt(messag)
        global outen
        outen = Toplevel(root)
        outen.title('Encrypted')
        enout = StringVar()
        labelen = Text(outen, width=20, height=8)
        labelen.grid(column=0, row=0, sticky=(W, E),  padx=10, pady=10, columnspan=2)
        encrypted = str(encrypted)
        encrypted = encrypted.replace(',', '')
        encrypted = encrypted.replace(']', '')
        encrypted = encrypted.replace('[', '')
        labelen.insert(END, '%s' % encrypted)
        labelen.configure(state="disabled")
        labelen.configure(wrap="word")
        ok = ttk.Button(outen, text='Ok', command=oken).grid(column=1, row=2, sticky=(E))
        exit = ttk.Button(outen, text='Exit', command=root.destroy).grid(column=2, row=2, sticky=(E))
    elif task == 'decrypt':
        message = get_message()
        decrypted = decrypt(message)
        global outde
        outde = Toplevel(root)
        outde.title('Decrypted')
        deout = StringVar()
        labelde = Text(outde, width=20, height=8)
        labelde.grid(column=0, row=0, sticky=(W, E),  padx=10, pady=10)
        decrypted = str(decrypted)
        decrypted = decrypted.replace(',', '')
        decrypted = decrypted.replace(']', '')
        decrypted = decrypted.replace('[', '')
        labelde.insert(END, '%s' % decrypted)
        labelde.configure(state="disabled")
        labelde.configure(wrap="word")
        ok = ttk.Button(outde, text='Ok', command=okde).grid(column=1, row=2, sticky=(E))
        exit = ttk.Button(outde, text='Exit', command=root.destroy).grid(column=2, row=2, sticky=(E))
    else:
        root.destroy()

root = Tk()
root.withdraw()
d = 9
e = 9
p = 5
q = 11

loop()
    
root.mainloop()
