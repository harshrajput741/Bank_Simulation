import gmail
def send_crendentials(email,name,acn,pwd):
    con = gmail.GMail('harshrajput74177@gmail.com','caxy wbpo txjd noah')
    body = f'''Hello {name},

            Welcome to ABC Bank, Here is your crendentials

            Account No = {acn}
            Password = {pwd}
    
            Kindly change your password when you login first time.
    
            Artha Digital Bank
            Sector - 16, Noida '''

    msg = gmail.Message(to =email,subject='Your Crendentials for Operating Account',text=body)
    con.send(msg)


def send_otp(email,name,otp):
    con = gmail.GMail('harshrajput74177@gmail.com','htil ouex xmmf fegt')
    body = f'''Hello {name},

            Welcome to ABC Bank, Here is your otp to recover password.

            otp = {otp}
    
            Artha Digital Bank
            Sector - 16, Noida '''

    msg = gmail.Message(to =email,subject='Otp for Password Recovery',text=body)
    con.send(msg)

def Withdrawal_otp(email,name,otp,balance):
    con = gmail.GMail('harshrajput74177@gmail.com','htil ouex xmmf fegt')
    body = f'''Hello {name},

            Welcome to ABC Bank, Here is your otp to Withdraw Amount is {balance}.

            otp = {otp}
    
            Artha Digital Bank
            Sector - 16, Noida '''

    msg = gmail.Message(to =email,subject='Otp for Withdraw Amount',text=body)
    con.send(msg)

def transfer_otp(email,name,otp,balance,acn,mobile):
    con = gmail.GMail('harshrajput74177@gmail.com','htil ouex xmmf fegt')
    body = f'''Hello {name},

            Welcome to ABC Bank, 

            Transfer Amount is {balance}
            To Account No = {acn}
            To Mobile No = {mobile}

            Here is your otp = {otp}
    
            Artha Digital Bank
            Sector - 16, Noida '''

    msg = gmail.Message(to =email,subject='Otp for Withdraw Amount',text=body)
    con.send(msg)
