#Currency Convertor


import tkinter as tk
import tkinter.ttk as ttk
from forex_python.converter import CurrencyRates

def show_tax(rate):
	x = amt.get()
	y = cf.get()
	z = ct.get()
	curr = CurrencyRates()
	a = curr.convert(y,z,x)
	net.set(format(a, '.2f'))

root = tk.Tk()
root.geometry('400x440')
root.title('Currency Converter')
#root.configure(bg='light blue')

amt = tk.IntVar()
cf = tk.StringVar()
ct = tk.StringVar()
net = tk.StringVar()

ttk.Label(root, text='Input amount', font='Times').grid(row=0, column=0, columnspan=5)

e = ttk.Entry(root, textvariable=amt)
e.grid(row=1, column=1, columnspan=3, sticky='nsew', padx=5, pady=5)

ttk.Label(root, text='Input Convert From (USD,INR,EUR,GBP etc)',font='Times').grid(row=2, column=0, columnspan=5)

e = ttk.Entry(root, textvariable=cf)
e.grid(row=3, column=1, columnspan=3, sticky='NSEW', padx=5, pady=5)

ttk.Label(root, text='Input Convert To (USD,INR,EUR,GBP etc)',font='Times').grid(row=4, column=0, columnspan=5)

e = ttk.Entry(root, textvariable=ct)
e.grid(row=5, column=1, columnspan=3, sticky='nsew', padx=5, pady=5)


b = ttk.Button(root, text='Convert', command=lambda r=1.08: show_tax(r))
b.grid(row=7, column=2, padx=5, pady=5,sticky='nsew')


# An empty Label to force row to be displayed
ttk.Label(root).grid(row=9, column=0, columnspan=5)

ttk.Label(root, text='--Converted Amount--').grid(row=10, column=2, columnspan=4, sticky='nsew')

l = ttk.Label(root, textvariable=net, relief='groove')
l.grid(row=11, column=1, columnspan=3, sticky='nsew')


root.mainloop()
