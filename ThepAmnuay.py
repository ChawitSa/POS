from tkinter import *
from tkinter import ttk, messagebox
from ProductList import *

############## GUI ##############
GUI = Tk()
GUI.title("ร้านเทพอำนวย")
width = GUI.winfo_screenwidth()
height =GUI.winfo_screenheight()
GUI.geometry("%dx%d" %(width, height))
GUI.iconbitmap('ThepAmnuay1.ico')

############ ttk.Style ###########
style = ttk.Style()
style.configure('TNotebook.Tab', font=('angsana new', '30'), width=15)
style.configure('TButton', font=('angsana new', '22'))



############## Tab ##############
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH, expand=True)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_tab1 = PhotoImage(file='icon_box.png')
icon_tab2 = PhotoImage(file='icon_barcode.png')
icon_tab3 = PhotoImage(file='icon_bill.png')

Tab.add(T1, text='ทะเบียนสินค้า', image=icon_tab1, compound='left')
Tab.add(T2, text='เขียนใบเสร็จ', image=icon_tab2, compound='left')
Tab.add(T3, text='ทะเบียนใบเสร็จ', image=icon_tab3, compound='left')

############ Product ###########
F = Frame(T1)
F.pack()

T1_header_name = ['รหัสสินค้า', 'ชื่อ', 'รหัสราคา', 'ราคา', 'บาร์โค้ด']
T1_header_width = [200, 400, 100, 100, 400]
style.configure('Treeview.Heading', font=('angsana new', '48'))
style.configure('Treeview.Column', font=('angsana new', '16'))
T1_table = ttk.Treeview(F, columns=T1_header_name, show='headings', height=20)
T1_table.pack(pady=20)
for hn, hw in zip(T1_header_name, T1_header_width):
    T1_table.heading(hn, text=hn)
    T1_table.column(hn, width=hw)

########## Check Bill ##########
FUL = Frame(T2)
FLL = Frame(T2)
FUL.grid(row=0, column=0, padx=10)
FLL.grid(row=1, column=0, padx=10)

img = PhotoImage(file='ThepAmnuay.png')
Label(FUL, text='ร้านเทพอำนวย', font=('angsana new', 48, 'bold')).pack()
Label(FUL, image=img, width=700, height=400).pack()

allmenu={}
def insert_order():
    if v_barcode.get() == True:
        table.insert()
    else:
        messagebox.askretrycancel("askretrycancel", "รหัสบาร์โค้ดไม่ถูกต้อง")

Label(FLL, text='รหัสสินค้า/บาร์โค้ด', font=('angsana new', 32, 'bold')).grid(row=0, column=0)
v_barcode = StringVar()
E1 = Entry(FLL, textvariable=v_barcode, font=('angsana new', 22, 'bold'), width=15)
E1.grid(row=0, column=1)
Label(FLL, text='จำนวนสินค้า', font=('angsana new', 32, 'bold')).grid(row=0, column=2)
v_piece = StringVar()
v_piece.set(1)
E2 = Entry(FLL, textvariable=v_piece, font=('angsana new', 28, 'bold'), width=4, justify='right')
E2.grid(row=0, column=3, ipadx=1)
Label(FLL, text='หน่วย', font=('angsana new', 32, 'bold')).grid(row=0, column=4)
T2_B = ttk.Button(FLL, text='เพิ่มสินค้า', command=insert_order).grid(row=0, column=5)
Label(FLL, text='รวม', font=('angsana new', 32, 'bold')).grid(row=1, column=0, ipady=40)

FUR = Frame(T2)
FUR.grid(row=0, column=1, padx=10)
header_name = ['ลำดับ', 'รายการสินค้า', 'จำนวน', 'หน่วย', 'ราคาหน่วย', 'จำนวนเงิน']
header_width = [50,300,50,50,100,100]
style.configure('Treeview.Heading', font=('angsana new', '16'))
style.configure('Treeview.Column', font=('angsana new', '16'))
table = ttk.Treeview(FUR, columns=header_name, show='headings', height=20)
table.pack()


for hd, hw in zip(header_name, header_width):
    table.heading(hd, text=hd)
    table.column(hd, width=hw)

GUI.mainloop()