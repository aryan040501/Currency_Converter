import tkinter as tk
from forex_python.converter import CurrencyRates

def show_tax(rate):
	x = amt.get()
	y = cf.get()
	z = ct.get()
	curr = CurrencyRates()
	a = curr.convert(y,z,x)
	net.set(format(a, '.2f'))

root = tk.Tk()
root.geometry('350x350')
root.title('Currency Converter')

amt = tk.IntVar()
cf = tk.StringVar()
ct = tk.StringVar()
net = tk.StringVar()

tk.Label(root, text='Input amount').grid(row=0, column=0, columnspan=5)

e = tk.Entry(root, textvariable=amt)
e.grid(row=1, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

tk.Label(root, text='Input Convert From (USD,INR,EUR,GBP etc)').grid(row=2, column=0, columnspan=5)

e = tk.Entry(root, textvariable=cf)
e.grid(row=3, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

tk.Label(root, text='Input Convert To (USD,INR,EUR,GBP etc)').grid(row=4, column=0, columnspan=5)

e = tk.Entry(root, textvariable=ct)
e.grid(row=5, column=1, columnspan=3, sticky='WE', padx=5, pady=5)


b = tk.Button(root, text='Convert', command=lambda r=1.08: show_tax(r))
b.grid(row=7, column=2, padx=5, pady=5)


# An empty Label to force row to be displayed
tk.Label(root).grid(row=9, column=0, columnspan=5)

tk.Label(root, text='Converted Amount %s').grid(row=10, column=2, columnspan=2, sticky='WE')

l = tk.Label(root, textvariable=net, relief='raised')
l.grid(row=11, column=2, columnspan=2, sticky='WE')


root.mainloop()
