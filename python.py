from tkinter import Tk, Label, Frame, Button,Entry,messagebox,simpledialog,PhotoImage,filedialog
import re
import time
import sqlite3
from datetime import datetime 
import os
DB_PATH = os.path.join(os.path.dirname(__file__), 'mybank.sqlite')

# Link to SQL Table Creator File-----------------------------------------
import SQL_Table_Creator

# Link Generator File----------------------------------------------------
import generator
# Link EmailHandler------------------------------------------------------
import emailhandler

# Date and Time Update Function------------------------------------------
def update_time():
    curdate = time.strftime("%d-%b-%Y\n%r")
    date.config(text=curdate)
    date.after(1000, update_time)  # Update every second

# For Existing User Login Screen-----------------------------------------
def existuser_screen():
    def back():
        frm.destroy()
        main_screen()

        def fp_click():
            frm.destroy()

    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='green')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='black')
    back_button.place(relx=0, rely=0)

# If User are loign Welcome Screen----------------------------------------
def loginsuccess_screen(acn):
    def back():
        frm.destroy()
        main_screen()
    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='green')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='black')
    back_button.place(relx=0, rely=0)

# Forgot Password Screen---------------------------------------------------
def forgetpass_screen():
    def back():
        frm.destroy()
        main_screen()
    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='green')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='black')
    back_button.place(relx=0, rely=0)

#==============================================================================================================================================
# Main Screen---------------------------------------------------------------
#==============================================================================================================================================
def main_screen():
    def newuser_click():
        frm.destroy()
        newuser_screen()

    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='green')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    from PIL import Image, ImageTk
    img = Image.open("main1.png").resize((1531, 665), Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(img, master=root)
    lbl = Label(frm, image=imgtk)
    lbl.place(relx=0, rely=0)
    lbl.image = imgtk  # Keep a reference to avoid garbage collection
    lbl.lower()

    # New user Button------------------------------------------
    newuser_btn = Button(frm, text='Open New \nBank Account',font=('arial',15,'bold'),fg = 'black', bg = 'powder blue',width = 12,activebackground='powder blue',activeforeground='black',
                         command = newuser_click)
    newuser_btn.place(relx=.37, rely=0.15 )

    # Existing User Button------------------------------------------
    existinguser_btn = Button(frm, text='Existing User\nSign In',font=('arial',15,'bold'),fg = 'black',bg = 'powder blue',bd = 2.2,width = 12,activebackground='powder blue',activeforeground='black',
                         command = existuser_screen)
    existinguser_btn.place(relx=.53, rely=0.15 )

#==============================================================================================================================================
# New User Registration Screen---------------------------------------------
#==============================================================================================================================================
def newuser_screen():
    def back():
        frm.destroy()
        main_screen()

# After Enter all details send a Account Credentials and Update Successful Account Create !!--------------------------------------
    def create_account():
        if not name_entry.get().strip():
            messagebox.showerror('Input Error', 'Please enter a valid name.')
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_entry.get().strip()):
                messagebox.showerror('Input Error', 'Please enter a valid email address.')
                return  
        if not re.match(r"^\d{10}$", mobile_entry.get().strip()):
            messagebox.showerror('Input Error', 'Please enter a valid 10-digit mobile number.')
            return
        if not re.match(r'^\d{4}\s\d{4}\s\d{4}$', adhar_entry.get().strip()):
            messagebox.showerror('Input Error', 'Please enter a valid 12-digit Aadhar number in this format 0000 0000 0000')
            return
        name_val = name_entry.get()
        email_val = email_entry.get()
        mobile_val = mobile_entry.get()
        adhar_val = adhar_entry.get()
        bal = 0
        opendate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pwd = generator.generate_pass()
        query = '''insert into accounts values(?,?,?,?,?,?,?,?)'''
        conobj = sqlite3.connect(DB_PATH)
        curobj = conobj.cursor()
        curobj.execute(query,(None,name_val,pwd,mobile_val,email_val,adhar_val,bal,opendate))
        conobj.commit()
        conobj.close()
        
        conobj = sqlite3.connect(DB_PATH)
        curobj = conobj.cursor()
        query = '''select max(acn) from accounts'''
        curobj.execute(query)
        tup = curobj.fetchone()
        conobj.close()

        emailhandler.send_crendentials(email_val,name_val,tup[0],pwd)
        messagebox.showinfo('Account Creation','Your account is opened and we have mailed your credentials to given email.')

# end of Credentials---------------------------------------------------------------------------------------------------------
    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='green')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    # try to load a background image for the new-user screen
    from PIL import Image, ImageTk
    img = Image.open("New_user_background.png").resize((1532, 667), Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(img, master=root)
    lbl = Label(frm, image=imgtk)
    lbl.place(relx=0, rely=0)
    lbl.image = imgtk  # Keep a reference to avoid garbage collection
    lbl.lower()

    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='black')
    back_button.place(relx=0, rely=0)

    newuser_label = Label(frm, text="New User Registration",font=('arial',20,'bold','underline'), bg='green', fg='white')
    newuser_label.pack(pady=20)

    name = Label(frm, text="Enter a Name:", font=('arial',15,'bold'), bg='green', fg='white')
    name.place(relx=0.3, rely=0.2)
    name_entry = Entry(frm, font=('arial',15),width=25)
    name_entry.place(relx=0.5, rely=0.2)
    name_entry.focus()

    email = Label(frm, text="Enter an Email ID:", font=('arial',15,'bold'), bg='green', fg='white')
    email.place(relx=0.3, rely=0.3)    
    email_entry = Entry(frm, font=('arial',15),width=25,)
    email_entry.place(relx=0.5, rely=.3)

    mobile = Label(frm, text="Enter an Mobile No:", font=('arial',15,'bold'), bg='green', fg='white')
    mobile.place(relx=0.3, rely=0.4)    
    def mobile_validate(P):
        return (P.isdigit() or P == "") and len(P) <= 10
    vcmd = frm.register(mobile_validate)
    mobile_entry = Entry(frm, font=('arial',15), width=25, validate='key', validatecommand=(vcmd, '%P'))
    mobile_entry.place(relx=0.5, rely=.4)

    adhar = Label(frm, text="Enter your Aadhar No:", font=('arial',15,'bold'), bg='green', fg='white')
    adhar.place(relx=0.3, rely=0.5)
    adhar_entry = Entry(frm, font=('arial',15),width=25)
    adhar_entry.place(relx=0.5, rely=0.5)

    submit_button = Button(frm, text='Submit',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',
                           command= create_account)
    submit_button.place(relx=0.5, rely=0.6)

    reset_button = Button(frm, text='Reset',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',
                           command=lambda: [name_entry.delete(0,'end'), email_entry.delete(0,'end'), mobile_entry.delete(0,'end'), adhar_entry.delete(0,'end')])
    reset_button.place(relx=0.6, rely=0.6)

    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='powder blue',activeforeground='black',
                            command=lambda: [frm.destroy(), main_screen()])
    back_button.place(relx=0, rely=0)

#==============================================================================================================================================
# Existing User Login Screen------------------------------------------
#==============================================================================================================================================
def existuser_screen():
    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='orange')
    
    # try to load a background image for the new-user screen
    from PIL import Image, ImageTk
    img = Image.open("exit.png").resize((1532, 667), Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(img, master=root)
    lbl = Label(frm, image=imgtk)
    lbl.place(relx=0, rely=0)
    lbl.image = imgtk  # Keep a reference to avoid garbage collection
    lbl.lower()

    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)
    existuser_label = Label(frm, text="Existing User Login",font=('arial',20,'bold','underline'), bg='orange', fg='white')
    existuser_label.pack(pady=20)

    acc_number = Label(frm, text="Enter Account Number:", font=('arial',15,'bold'), bg='Orange', fg='white')
    acc_number.place(relx=0.3, rely=0.2)
    acc_number_entry = Entry(frm, font=('arial',15),width=25)
    acc_number_entry.place(relx=0.5, rely=0.2)
    acc_number_entry.focus()

    password = Label(frm, text="Enter Password:", font=('arial',15,'bold'), bg='orange', fg='white')
    password.place(relx=0.3, rely=0.3)
    password_entry = Entry(frm, font=('arial',15),width=25, show='*')
    password_entry.place(relx=0.5, rely=0.3)
    
# Do login ----------------------------------------------------------------------------------------------------------------
    def do_login():
            acct = login(acc_number_entry.get(), password_entry.get())
            if acct:
                frm.destroy()
                loginsuccess_screen(acct)

    login_button = Button(frm, text='Submit',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=do_login)
    login_button.place(relx=0.5, rely=0.4)

    forgotpass_button = Button(frm, text='Forgot Password',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command =forgetpass_screen)
    forgotpass_button.place(relx=0.6, rely=0.4,)

    #Back Button------------------------------------------------------
    back_button = Button(frm, text='Back',font=('arial',10,'bold'),bd = 5,fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',
                            command=lambda: [frm.destroy(), main_screen()])
    back_button.place(relx=0, rely=0)

def login(acn, password):
    acn = str(acn).strip()
    password = str(password).strip()

    if not acn or not password:
        messagebox.showerror("Error", "Please enter account number and password")
        return False
    try:
        conobj = sqlite3.connect(DB_PATH)
        cur = conobj.cursor()
        cur.execute("SELECT * FROM accounts WHERE acn=? AND password=?",(acn, password))
        tup = cur.fetchone()
        conobj.close()
        if tup== None:
            messagebox.showerror("Invalid", "Account No or Password wrong")
            return None
        else:
            acn = tup[0]
            return acn
    except Exception as e:
        return False

#================================================================================================================
# If you Login Welcome Successful Screen---------------------------------------------
#================================================================================================================
def loginsuccess_screen(acn=None):
    def logout():
        frm.destroy()
        main_screen()

    def home_screen():
        for child in list(getattr(frm, 'iframes', [])):
            try:
                child.destroy()
            except Exception:
                pass
        frm.iframes = []
        loginsuccess_screen(acn)
    
    conobj = sqlite3.connect(DB_PATH)
    curobj = conobj.cursor()
    query='''SELECT name FROM accounts WHERE acn=? '''
    curobj.execute(query,(acn,))
    tup = curobj.fetchone()
    conobj.close()

    def check_details():
        ifrm = Frame(frm,highlightbackground='black',highlightthickness=2)
        # register for bulk-destroy by Home
        if not hasattr(frm, 'iframes'):
            frm.iframes = []
        frm.iframes.append(ifrm)
        ifrm.configure(bg='white')
        ifrm.place(relx = .12, rely = 0.08, relwidth = 0.75, relheight = 0.85)

        title_lbl = Label(ifrm, text="This is Check Details Screen", font=('arial',15,'bold'), bg='white', fg='black')
        title_lbl.pack(pady=20)

        conobj = sqlite3.connect(DB_PATH)
        curobj = conobj.cursor()
        query='''SELECT acn,balance,adhar,email,opendate FROM accounts WHERE acn=? '''
        curobj.execute(query,(acn,))
        tup = curobj.fetchone()
        conobj.close()
    
        acc_no = tup[0]
        balance = f"₹ {tup[1]:,.2f}"
        aadhar = str(tup[2]).zfill(12)
        aadhar_fmt = f"{aadhar[:4]} {aadhar[4:8]} {aadhar[8:]}"
        email = tup[3]
        opened_on = tup[4]

        details = (f"Account No.         :    {acc_no}\n\n"f"Balance               :    {balance}\n\n"f"Aadhaar No.        :    {aadhar_fmt}\n\n"f"Email ID              :    {email}\n\n"f"Account Opened :    {opened_on}")
        details_lbl = Label(ifrm,text=details,font=("Arial", 18),bg="white",fg="black",justify='left')
        details_lbl.place(relx=0.55, rely=0.4, anchor="center")

    def update_screen():
        def update_details():
            name = name_entry.get().strip()
            password = password_entry.get().strip()
            email = email_entry.get().strip()
            mobile = mobile_entry.get().strip()
            
            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query='''UPDATE accounts SET name=?, password=?, email=?, mobile=? WHERE acn=? '''
            curobj.execute(query,(name,password,email,mobile,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Update Details','Your details have been updated successfully.')
            loginsuccess_screen(acn)
        
        conobj = sqlite3.connect(DB_PATH)
        curobj = conobj.cursor()
        query='''SELECT name,password,email,mobile FROM accounts WHERE acn=? '''
        curobj.execute(query,(acn,))
        tup = curobj.fetchone()
        conobj.close()

        ifrm = Frame(frm,highlightbackground='black',highlightthickness=2)
        if not hasattr(frm, 'iframes'):
            frm.iframes = []
        frm.iframes.append(ifrm)
        ifrm.configure(bg='white')
        ifrm.place(relx = .12, rely = 0.08, relwidth = 0.75, relheight = 0.85)

        title_lbl = Label(ifrm, text="This is Update Details Screen", font=('arial',15,'bold'), bg='white', fg='black')
        title_lbl.pack(pady=20)

        name = Label(ifrm, text="Name:", font=('arial',12,'bold'), bg='green', fg='white')
        name.place(relx=0.3, rely=0.2)
        name_entry = Entry(ifrm, font=('arial',12),width=25)
        name_entry.place(relx=0.5, rely=0.2)

        password = Label(ifrm, text="Password:", font=('arial',12,'bold'), bg='green', fg='white')
        password.place(relx=0.3, rely=0.3)
        password_entry = Entry(ifrm, font=('arial',12),width=25)
        password_entry.place(relx=0.5, rely=0.3)

        email = Label(ifrm, text="Email ID:", font=('arial',12,'bold'), bg='green', fg='white')
        email.place(relx=0.3, rely=0.4)    
        email_entry = Entry(ifrm, font=('arial',12),width=25)
        email_entry.place(relx=0.5, rely=.4)

        mobile = Label(ifrm, text="Mobile No:", font=('arial',12,'bold'), bg='green', fg='white')
        mobile.place(relx=0.3, rely=0.5)    
        mobile_entry = Entry(ifrm, font=('arial',12),width=25)
        mobile_entry.place(relx=0.5, rely=.5)

        name_entry.insert(0, tup[0])  # Pre-fill name
        email_entry.insert(0, tup[2])  # Pre-fill email
        mobile_entry.insert(0, tup[3])  # Pre-fill mobile number
        password_entry.insert(0, tup[1])  # Placeholder for password

        update_button = Button(ifrm, text='Update Details',font=('arial',10,'bold'), fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=update_details)
        update_button.place(relx=0.6, rely=0.6)

    def deposit_screen():
        def deposit_amount():
            amount_str = amount.get().strip()
            if not amount_str or not amount_str.isdigit():
                messagebox.showerror('Deposit Amount', 'Please enter a valid positive amount.')
                return
            amount_val = int(amount_str)
            if amount_val <= 0:
                messagebox.showerror('Deposit Amount', 'Please enter a positive amount greater than zero.')
                return
            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query = '''UPDATE accounts SET balance = balance + ? WHERE acn=? '''
            curobj.execute(query, (amount_val, acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Deposit Amount', f'Amount {amount_val} deposited successfully.')
            amount.delete(0, 'end')
            amount.focus()

        ifrm = Frame(frm,highlightbackground='black',highlightthickness=2)
        if not hasattr(frm, 'iframes'):
            frm.iframes = []
        frm.iframes.append(ifrm)
        ifrm.configure(bg='white')
        ifrm.place(relx = .12, rely = 0.08, relwidth = 0.75, relheight = 0.85)
    
        title_lbl = Label(ifrm, text="This is Deposit Amount Screen", font=('arial',15,'bold'), bg='white', fg='black')
        title_lbl.pack(pady=20)

        amount_lbl = Label(ifrm, text="Enter Amount to Deposit:", font=('arial',12,'bold'), bg='white', fg='black')
        amount_lbl.place(relx=0.3, rely=0.3)
        amount = Entry(ifrm, font=('arial',12),width=25)
        amount.place(relx=0.5, rely=0.3)
        amount.focus()

        deposit_button = Button(ifrm, text='Deposit',font=('arial',10,'bold'), fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=deposit_amount)
        deposit_button.place(relx=0.5, rely=0.4)

    def withdraw_screen():
        def withdrawal_otp():
            gen_otp = generator.withdraw_otp()
            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query = '''SELECT name,email FROM accounts WHERE acn=? '''
            curobj.execute(query,(acn,))
            tup = curobj.fetchone()
            conobj.close()
            emailhandler.Withdrawal_otp(tup[1], tup[0], gen_otp, withdraw.get().strip())
            user_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your email:")
            if user_otp and user_otp.strip() == str(gen_otp):
                withdraw_amount()
            else:
                messagebox.showerror('Withdraw Amount', 'Invalid OTP. Withdrawal cancelled.')

        def withdraw_amount():
            withdraw_str = withdraw.get().strip()

            if not withdraw_str or not withdraw_str.isdigit():
                messagebox.showerror('Withdraw Amount', 'Please enter a valid positive amount.')
                return
            amount_val = int(withdraw_str)
            if amount_val <= 0:
                messagebox.showerror('Withdraw Amount', 'Please enter a positive amount greater than zero.')
                return
            
            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query = '''SELECT balance FROM accounts WHERE acn=? '''
            curobj.execute(query, (acn,))
            tup = curobj.fetchone()
            if tup and tup[0] >= amount_val:
                query = '''UPDATE accounts SET balance = balance - ? WHERE acn=? '''
                curobj.execute(query, (amount_val, acn))
                conobj.commit()
                messagebox.showinfo('Withdraw Amount', f'Amount {amount_val} withdrawn successfully.')
            else:
                messagebox.showerror('Withdraw Amount', 'Insufficient balance.')
            conobj.close()
            withdraw.delete(0, 'end')
            withdraw.focus()

        ifrm = Frame(frm,highlightbackground='black',highlightthickness=2)
        if not hasattr(frm, 'iframes'):
            frm.iframes = []
        frm.iframes.append(ifrm)
        ifrm.configure(bg='white')
        ifrm.place(relx = .12, rely = 0.08, relwidth = 0.75, relheight = 0.85)

        title_lbl = Label(ifrm, text="This is Withdraw Amount Screen", font=('arial',15,'bold'), bg='white', fg='black')
        title_lbl.pack(pady=20)

        amount_lbl = Label(ifrm, text="Enter Amount to Withdraw:", font=('arial',12,'bold'), bg='white', fg='black')
        amount_lbl.place(relx=0.3, rely=0.3)
        withdraw = Entry(ifrm, font=('arial',12),width=25)
        withdraw.place(relx=0.5, rely=0.3)
        withdraw.focus()
        withdraw_button = Button(ifrm, text='Withdraw',font=('arial',10,'bold'), fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=withdrawal_otp)
        withdraw_button.place(relx=0.5, rely=0.4)
        
    def transfer_screen():
        def transfer_otp():
            gen_otp = generator.generate_otp()
            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query = '''SELECT name,email FROM accounts WHERE acn=? '''
            curobj.execute(query,(acn,))
            tup = curobj.fetchone()
            conobj.close()
            emailhandler.transfer_otp(tup[1], tup[0], gen_otp, Amount.get().strip(), Account.get().strip(), Mobile.get().strip())
            user_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your email:")
            if user_otp and user_otp.strip() == str(gen_otp):
                transfer_amount()
            else:
                messagebox.showerror('Transfer Amount', 'Invalid OTP. Transfer cancelled.')
        def transfer_amount():
            target_acn = Account.get().strip()
            target_mobile = Mobile.get().strip()
            amount_str = Amount.get().strip()

            if not target_acn or not target_mobile or not amount_str or not amount_str.isdigit():
                messagebox.showerror('Transfer Amount', 'Please enter valid details.')
                return
            amount_val = int(amount_str)
            if amount_val <= 0:
                messagebox.showerror('Transfer Amount', 'Please enter a positive amount greater than zero.')
                return

            conobj = sqlite3.connect(DB_PATH)
            curobj = conobj.cursor()
            query = '''SELECT balance FROM accounts WHERE acn=? AND mobile=? '''
            curobj.execute(query, (target_acn, target_mobile))
            tup = curobj.fetchone()
            if tup is None:
                messagebox.showerror('Transfer Amount', 'Target account not found.')
                conobj.close()
                return
            query = '''SELECT balance FROM accounts WHERE acn=? '''
            curobj.execute(query, (acn,))
            tup_source = curobj.fetchone()
            if tup_source and tup_source[0] >= amount_val:
                query = '''UPDATE accounts SET balance = balance - ? WHERE acn=? '''
                curobj.execute(query, (amount_val, acn))
                query = '''UPDATE accounts SET balance = balance + ? WHERE acn=? '''
                curobj.execute(query, (amount_val, target_acn))
                conobj.commit()
                messagebox.showinfo('Transfer Amount', f'Amount {amount_val} transferred successfully.')
            else:
                messagebox.showerror('Transfer Amount', 'Insufficient balance.')
            conobj.close()
            Account.delete(0, 'end')
            Mobile.delete(0, 'end')
            Amount.delete(0, 'end')
            Account.focus()

        ifrm = Frame(frm,highlightbackground='black',highlightthickness=2)
        if not hasattr(frm, 'iframes'):
            frm.iframes = []
        frm.iframes.append(ifrm)
        ifrm.configure(bg='white')
        ifrm.place(relx = .12, rely = 0.08, relwidth = 0.75, relheight = 0.85)

        title_lbl = Label(ifrm, text="This is Transfer Amount Screen", font=('arial',15,'bold'), bg='white', fg='black')
        title_lbl.pack(pady=20)

        Account_lbl = Label(ifrm, text="Enter Account Number:", font=('arial',12,'bold'), bg='white', fg='black')
        Account_lbl.place(relx=0.3, rely=0.2)
        Account = Entry(ifrm, font=('arial',12),width=25)
        Account.place(relx=0.5, rely=0.2)

        Mobile_lbl = Label(ifrm, text="Enter Mobile Number:", font=('arial',12,'bold'), bg='white', fg='black')
        Mobile_lbl.place(relx=0.3, rely=0.3)
        Mobile = Entry(ifrm, font=('arial',12),width=25)
        Mobile.place(relx=0.5, rely=0.3)
      
        Amount_lbl = Label(ifrm, text="Enter Amount:", font=('arial',12,'bold'), bg='white', fg='black')
        Amount_lbl.place(relx=0.3, rely=0.4)
        Amount = Entry(ifrm, font=('arial',12),width=25)
        Amount.place(relx=0.5, rely=0.4)

        transfer_button = Button(ifrm, text='Transfer',font=('arial',10,'bold'),fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=transfer_otp)
        transfer_button.place(relx=0.5, rely=0.5)

    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='orange')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    logout_button = Button(frm, text='Logout',font=('arial',10,'bold'), width = 15, bd = 5,fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=logout)
    logout_button.place(relx=0.01, rely=0.85)

    welcome_label = Label(frm, text=f'Welcome, {tup[0]}',font=('arial',18,'bold','underline'), bg='orange', fg='Black')
    welcome_label.place(relx=0.01, rely=0.01)

    def update_pic():
        path = filedialog.askopenfilename(title="Select Profile Picture", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if not path:
            return
        try:
            img = Image.open(path).resize((150, 150), Image.LANCZOS)
            save_path = os.path.join(os.path.dirname(__file__), f"profile_{acn}.png")
            img.save(save_path)
            imgtk_profile = ImageTk.PhotoImage(img, master=frm)
            if hasattr(frm, 'img_profile_label'):
                frm.img_profile_label.configure(image=imgtk_profile)
            else:
                frm.img_profile_label = Label(frm, image=imgtk_profile)
                frm.img_profile_label.place(relx=0.9, rely=0)
            frm.img_profile_label.image = imgtk_profile
        except Exception as e:
            messagebox.showerror('Image Error', f'Could not load/save image: {e}')

    profile_path = os.path.join(os.path.dirname(__file__), f"profile_{acn}.png")
    if os.path.exists(profile_path):
        img_profile = Image.open(profile_path).resize((150, 150), Image.LANCZOS)
    else:
        default_path = os.path.join(os.path.dirname(__file__), 'default.png')
        img_profile = Image.open(default_path).resize((150, 150), Image.LANCZOS)
    imgtk_profile = ImageTk.PhotoImage(img_profile, master=frm)
    frm.img_profile_label = Label(frm, image=imgtk_profile)
    frm.img_profile_label.place(relx=0.9, rely=0)
    frm.img_profile_label.image = imgtk_profile  # Keep a reference to avoid garbage collection
    frm.img_profile_label.lower()
        
    update_profile_button = Button(frm, text='Update Profile',font=('arial',10,'bold'),width = 15, bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=update_pic)
    update_profile_button.place(relx=0.906, rely=0.235)

    Home = Button(frm, text='Home',font=('arial',10,'bold'), bd = 5, fg='black',width = 15, bg='powder blue',activebackground='powder blue',activeforeground='black',command=home_screen)
    Home.place(relx=0.01, rely=0.08)
    
    check_details_button = Button(frm, text='Check Details',font=('arial',10,'bold'), width = 15, bd = 5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=check_details)
    check_details_button.place(relx=0.01, rely=0.18)
    
    update_details_button = Button(frm, text='Update Details',font=('arial',10,'bold'), width = 15, bd=5, fg='black', bg='powder blue',activebackground='powder blue',activeforeground='black',command=update_screen)
    update_details_button.place(relx=0.01, rely=0.28)

    deposit_button = Button(frm, text='Deposit Amount',font=('arial',10,'bold'), width = 15, bd=5, fg='black', bg='green',activebackground='purple',activeforeground='white',command=deposit_screen)
    deposit_button.place(relx=0.01, rely=0.38)

    withdraw_button = Button(frm, text='Withdraw Amount',font=('arial',10,'bold'), width = 15, bd=5, fg='black', bg='red',activebackground='purple',activeforeground='white',command=withdraw_screen)
    withdraw_button.place(relx=0.01, rely=0.48)  

    transfer_button = Button(frm, text='Transfer Amount',font=('arial',10,'bold'), width = 15, bd=5, fg='black', bg='blue',activebackground='purple',activeforeground='white',command=transfer_screen)
    transfer_button.place(relx=0.01, rely=0.58) 

#==============================================================================================================
# If you forgot your password Screen------------------------------------------
#==============================================================================================================
def forgetpass_screen():
    def back():
        frm.destroy()
        existuser_screen()

    def send_otp():
        gen_otp = generator.generate_otp()
        acn = acc_number_entry.get().strip()
        adhar = forget_adhar_entry.get().strip()

        conobj = sqlite3.connect(DB_PATH)
        curobj = conobj.cursor()
        query = '''Select name,email,password from accounts where acn = ? and adhar = ?'''
        curobj.execute(query,(acn,adhar))
        tup = curobj.fetchone()
        conobj.close()
        if not re.match(r'^\d{4}\s\d{4}\s\d{4}$', forget_adhar_entry.get().strip()):
            messagebox.showerror('Input Error', 'Please enter a valid 12-digit Aadhar number in this format 0000 0000 0000')
            return
        if not acn or not adhar:
                messagebox.showerror('Enter Details', 'Please enter valid details.')
                return
        if tup is None:
                messagebox.showerror('Forget Password','Record not found')
        else:
                emailhandler.send_otp(tup[1], tup[0], gen_otp)
                user_otp = simpledialog.askinteger("Password Recovery","Enter OTP")
                if gen_otp == user_otp:
                    messagebox.showinfo("Password Recovery",f"Your Password = {tup[2]}")
                else:
                 messagebox.showerror("Password Recovery","Invalid Otp")
                otp.configure(text = "Resend OTP")

    frm = Frame(root, highlightbackground="black", highlightthickness=2)
    frm.configure(bg='orange')
    frm.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.8)

    forgetpass_label = Label(frm, text="Forgot Password",font=('arial',20,'bold','underline'), bg='Orange', fg='white')
    forgetpass_label.pack(pady=20)

    acc_number = Label(frm, text="Enter Account Number:", font=('arial',15,'bold'), bg='Orange', fg='white')
    acc_number.place(relx=0.3, rely=0.2)
    acc_number_entry = Entry(frm, font=('arial',15),width=25)
    acc_number_entry.place(relx=0.5, rely=0.2)
    acc_number_entry.focus()

    forget_adhar = Label(frm, text="Enter Aadhar Number:", font=('arial',15,'bold'), bg='Orange', fg='white')
    forget_adhar.place(relx=0.3, rely=0.3)
    forget_adhar_entry = Entry(frm, font=('arial',15),width=25)
    forget_adhar_entry.place(relx=0.5, rely=0.3)

    otp =Button(frm, text='Send OTP',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='purple',activeforeground='white',command = send_otp)
    otp.place(relx=0.5, rely=0.4)
    
    reset_button = Button(frm, text='Reset',font=('arial',10,'bold'), bd=5, fg='black', bg='powder blue',activebackground='purple',activeforeground='white',
                          command=lambda: [acc_number_entry.delete(0,'end'), forget_adhar_entry.delete(0,'end')])
    reset_button.place(relx=0.6, rely=0.4)

    # Back Button------------------------------------------------------
    back_button = Button(frm, text='Back',
                            font=('arial',10,'bold'),bd = 5,fg = 'black', bg = 'powder blue',activebackground='purple',activeforeground='white',
                            command=lambda: [frm.destroy(), main_screen()])
    back_button.place(relx=0, rely=0)
#==============================================================================================================
#==============================================================================================================
root = Tk() #ye code top level window bnate ha
root.state('zoomed')  #to make full screen window
root.resizable(False, False)
root.config(bg='powder blue')
root.title("Digital Banking Management System")
from PIL import Image, ImageTk
img = Image.open("logo1.png").resize((150,90), Image.LANCZOS)
imgtk = ImageTk.PhotoImage(img,master=root)
logo_label = Label(root, image=imgtk, bg='powder blue')
logo_label.place(relx=0.01, rely=0.01)

title = Label(root, text="Digital Banking Management System",
              font= ('arial',28,'bold','underline'), bg='powder blue',fg ='navy blue')
sub_title = Label(root, text="Simulation of Real-World Banking Operations",
              font= ('arial',15), bg='powder blue',fg ='black')
sub_title.place(relx=0.37, rely=0.057)
mini_title = Label(root, text="(🔐 Secure • Reliable • Fast)",
              font= ('arial',12), bg='powder blue',fg ='black')
mini_title.place(relx=0.42, rely=0.095)

title.pack()

# For Date and Time--------------------------------------------------
curdate = time.strftime("%d-%b-%Y\n%r")
date = Label(root, text=curdate,
             font=('arial',15,'bold'), bg='powder blue',fg = 'black', justify='right')
date.place(relx=0.91, rely=0.03)
update_time()  # Start the time update loop

# For Footer--------------------------------------------------------
# create a footer frame at the bottom and place developer text left and contact info right
footer_frame = Frame(root, bg='powder blue')
footer_frame.pack(side='bottom', fill='x', pady=8)
dev_label = Label(footer_frame, text="Developed by: Harsh Rajput", font=('arial',18,'bold'), bg='powder blue')
dev_label.pack(side='left', padx=0)
contact_label = Label(footer_frame, text="Contact us: Harshrajput74177@gmail.com \n Mobile No. 7417709971", font=('arial',14,'bold'), bg='powder blue', justify='right')
contact_label.pack(side='right')

main_screen()
root.mainloop()   #TO make Window visible and run the application