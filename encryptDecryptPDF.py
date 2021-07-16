# Author: sgrmshrsm7
# Package required: PyPDF2
# Installation: pip3 install PyPDF2

import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from PyPDF2 import PdfFileWriter, PdfFileReader

def encryptPDF():
	file1 = askopenfile(mode ='r', filetypes =[('PDF Files', '*.pdf')])
	if file1 is not None:
		filename = file1.name
		file = PdfFileReader(filename)

		if file.isEncrypted:
			ertext = 'File already encrypted!'
		elif password.get() == '':
			ertext = 'Empty password!'
		else:
			out = PdfFileWriter()
			for i in range(file.numPages):
				page = file.getPage(i)
				out.addPage(page)

			out.encrypt(password.get())

			with open(filename[:-4]+'_encrypted.pdf', "wb") as f:
				out.write(f)

			ertext = 'Encryption Successfull!'

		encryptionResult = Tk()
		encryptionResult.minsize(300, 120)
		encryptionResult.maxsize(300, 120)
		positionRight = int(encryptionResult.winfo_screenwidth() / 2 - 150)
		positionDown = int(encryptionResult.winfo_screenheight() / 2 - 60)
		encryptionResult.geometry('+{}+{}'.format(positionRight, positionDown))
		encryptionResult.configure(background='#1a1a1a')
		encryptionResult.title(ertext)
		
		erlabel = Label(encryptionResult, text = ertext, font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff')
		erlabel.place(relx = 0.5, y = 40, anchor = CENTER)

		erokbutton= Button(encryptionResult, text = 'OK', font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff', command = encryptionResult.destroy)
		erokbutton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

		encryptionResult.mainloop()

def decryptPDF():
	file1 = askopenfile(mode ='r', filetypes =[('PDF Files', '*.pdf')])
	if file1 is not None:
		filename = file1.name
		file = PdfFileReader(filename)

		if file.isEncrypted:
			out = PdfFileWriter()
			try:
				file.decrypt(password.get())

				for i in range(file.numPages):
					page = file.getPage(i)
					out.addPage(page)

				with open(filename[:-4]+'_decrypted.pdf', "wb") as f:
					out.write(f)
				
				drtext = 'Decryption Successfull!'
			except:
				drtext = 'Wrong password!'
		else:
			drtext = 'File not encrypted!'

		decryptionResult = Tk()
		decryptionResult.minsize(300, 120)
		decryptionResult.maxsize(300, 120)
		positionRight = int(decryptionResult.winfo_screenwidth() / 2 - 150)
		positionDown = int(decryptionResult.winfo_screenheight() / 2 - 60)
		decryptionResult.geometry('+{}+{}'.format(positionRight, positionDown))
		decryptionResult.configure(background='#1a1a1a')
		decryptionResult.title(drtext)
		
		drlabel = Label(decryptionResult, text = drtext, font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff')
		drlabel.place(relx = 0.5, y = 40, anchor = CENTER)

		drokbutton= Button(decryptionResult, text = 'OK', font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff', command = decryptionResult.destroy)
		drokbutton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

		decryptionResult.mainloop()

encryptDecryptPDF = Tk()
encryptDecryptPDF.minsize(450, 490)
encryptDecryptPDF.maxsize(450, 490)
positionRight = int(encryptDecryptPDF.winfo_screenwidth() / 2 - 225)
positionDown = int(encryptDecryptPDF.winfo_screenheight() / 2 - 245)
encryptDecryptPDF.geometry('+{}+{}'.format(positionRight, positionDown))
encryptDecryptPDF.configure(background='#1a1a1a')
encryptDecryptPDF.title('Encrypt-Decrypt PDF')

password = StringVar()
password.set('')

btncolor = '#0080ff'
btntxt = '#ffffff'

passlabel = Label(encryptDecryptPDF, text = 'Password', font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff')
passlabel.place(x = 75, y = 50)

password_field = Entry(encryptDecryptPDF, show="*", borderwidth = 20, relief=tk.FLAT, textvariable = password, justify = 'left', fg = '#1a1a1a', bg = '#ffffff', font = 'Helvetica 15')
password_field.place(x = 75, y = 80, height = 50, width = 250)

showpass = 0

def show_password():
	global showpass
	if showpass == 0:
		password_field.config(show = '')
		showpass = 1
	else:
		password_field.config(show = '*')
		showpass = 0

clearButton = Button(encryptDecryptPDF, text = ';)', fg = btntxt, bg = btncolor, command = show_password, font = 'Helvetica 17', borderwidth = 0)
clearButton.place(x = 325, y = 80, height = 50, width = 50)

encryptButton = Button(encryptDecryptPDF, text = 'Encrypt PDF', fg = btntxt, bg = btncolor, command = encryptPDF, font = 'Helvetica 17', borderwidth = 0)
encryptButton.place(x = 100, y = 180, height = 60, width = 250)
decryptButton = Button(encryptDecryptPDF, text = 'Decrypt PDF', fg = btntxt, bg = btncolor, command = decryptPDF, font = 'Helvetica 17', borderwidth = 0)
decryptButton.place(x = 100, y = 280, height = 60, width = 250)
exitButton = Button(encryptDecryptPDF, text = 'Exit', fg = btntxt, bg = '#D11A2A', command = encryptDecryptPDF.destroy, font = 'Helvetica 17', borderwidth = 0)
exitButton.place(x = 100, y = 380, height = 60, width = 250)

encryptDecryptPDF.mainloop()