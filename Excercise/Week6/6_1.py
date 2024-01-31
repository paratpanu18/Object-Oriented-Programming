from datetime import datetime

# Class Code

class Bank():
    def __init__(self):
        self.__users_list = []
        self.__atm_machines_list = []
    
    @property
    def users_list(self):
        return self.__users_list
    @users_list.setter
    def users_list(self, users_list):
        return self.__users_list
    
    @property
    def atm_machines_list(self):
        return self.__atm_machines_list
    @atm_machines_list.setter
    def atm_machines_list(self, atm_machines_list):
        return self.__atm_machines_list
    
    def get_account_by_atm_card(self, atm_card):
        for user in self.users_list:
            for account in user.accounts_list:
                if account.atm_card == atm_card:
                    return account
        return None
    
    def get_account_by_account_number(self, account_number: str):
        for user in self.users_list:
            for account in user.accounts_list:
                if account.account_number == account_number:
                    return account
        return None


class User():
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__accounts_list = []

    @property
    def accounts_list(self):
        return self.__accounts_list
    @accounts_list.setter
    def accounts_list(self, accounts_list):
        return self.__accounts_list

class AtmCard():
    def __init__(self, card_number: str, annual_fee: float, max_daily_withdraw: float, pin: str):
        self.__card_number = card_number
        self.__annual_fee = annual_fee
        self.__max_daily_withdraw = max_daily_withdraw
        self.__pin = pin

    @property
    def card_number(self):
        return self.__card_number

class Transaction:
    def __init__(self, transaction_type, amount, atm_machine, target_account = None):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__atm_machine = atm_machine
        self.__time_stamp = datetime.now()
        # self.__current_balance = None
        if transaction_type == 'T' and target_account is None:
            raise ValueError('Target account is required for transfer transaction')
        else:
            self.__target_account = target_account

    @property
    def time_stamp(self):
        return self.__time_stamp
    @time_stamp.setter
    def time_stamp(self, time_stamp):
        self.__time_stamp = time_stamp

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def amount(self):
        return self.__amount
    
    @property
    def target_account(self):
        return self.__target_account
    
    def get_data(self):
        return f'{self.__transaction_type}-{self.__atm_machine.atm_machine_id}-{self.__amount} '

class BankAccount():
    def __init__(self, owner: User, account_number: str, balance: float, atm_card: AtmCard):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance
        self.__atm_card = atm_card
        self.__transactions_list = []
    
    @property
    def account_number(self):
        return self.__account_number

    @property
    def atm_card(self):
        return self.__atm_card

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def perform_transaction(self, transaction: Transaction):
        # Deposit
        if transaction.transaction_type == 'D' and transaction.amount > 0:
            self.__balance += transaction.amount
            transaction.time_stamp = datetime.now()
            transaction.current_balance = self.__balance
            self.__transactions_list.append(transaction)
            return True
        # Withdraw
        elif transaction.transaction_type == 'W' and transaction.amount > 0 and transaction.amount <= self.__balance:
            self.__balance -= transaction.amount
            transaction.time_stamp = datetime.now()
            transaction.current_balance = self.__balance
            self.__transactions_list.append(transaction)
            return True
        # Transfer
        elif transaction.transaction_type == 'T' and transaction.amount > 0 and transaction.amount <= self.__balance:
            target_account = transaction.target_account
            if target_account is None:
                print("Target account not found")
                return False

            self.__balance -= transaction.amount
            target_account.balance += transaction.amount
            transaction.time_stamp = datetime.now()
            transaction.current_balance = self.__balance
            self.__transactions_list.append(transaction)
            return True 
        return False
    
    def get_data(self):
        return {
            'account_number': self.__account_number,
            'balance': self.__balance,
            'transactions': [transaction.get_data() for transaction in self.__transactions_list]
        }

class AtmMachine():
    def __init__(self, atm_machine_id: str, initial_cash_amount: float):
        self.__atm_machine_id = atm_machine_id
        self.__cash_amount = initial_cash_amount
    
    @property
    def atm_machine_id(self):
        return self.__atm_machine_id
    
    @property
    def cash_amount(self):
        return self.__cash_amount
    @cash_amount.setter
    def cash_amount(self, cash_amount):
        if cash_amount >= 0:
            self.__cash_amount = cash_amount
        else:
            return 'Error'


    # TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
    # TODO     2) atm_card เป็นหมายเลขของ atm_card
    # TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
    # TODO     ควรเป็น method ของเครื่อง ATM
    def insert_card(self, bank: Bank, atm_card: AtmCard):
        bank_account = bank.get_account_by_atm_card(atm_card)
        return bank_account if bank_account else None
    
    # TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0
    def deposit(self, bank_account: BankAccount, amount: float):
        transaction = Transaction(transaction_type='D', amount=amount, atm_machine=self)
        if bank_account.perform_transaction(transaction):
            self.cash_amount += amount
            return 'Success'
        else:
            return 'Error'

    #TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def withdraw(self, bank_account: BankAccount, amount: float):
        transaction = Transaction('W', amount, self)
        if bank_account.perform_transaction(transaction) and self.cash_amount >= amount:
            self.cash_amount -= amount
            return 'Success'
        else:
            return 'Error'

    #TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    def transfer(self, bank_account: BankAccount, target_account: BankAccount, amount: float):
        transaction = Transaction('T', amount, self, target_account)
        if bank_account.perform_transaction(transaction):
            return 'Success'
        else:
            return 'Error'


    
##################################################################################
# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890',20000, '12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321', 1000, '12346']}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

bank1 = Bank()                                                          
bank1.atm_machines_list.extend([AtmMachine('1001', 1000000), 
                                AtmMachine('1002', 200000)])                            # Add atm machine to bank

bank1.users_list.append(User('1-1101-12345-12', 'Harry Potter'))                        # Add user to bank
bank1.users_list[0].accounts_list.append(BankAccount(bank1.users_list[0], '1234567890', 20000, AtmCard('12345', 0, 10000, '1234'))) # Add account to user

bank1.users_list.append(User('1-1101-12345-13', 'Hermione Jean Granger'))               # Add user to bank
bank1.users_list[1].accounts_list.append(BankAccount(bank1.users_list[1], '0987654321', 1000, AtmCard('12346', 0, 10000, '1234'))) # Add account to user

##################################################################################
        

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1 :")

atm_machine1 = bank1.atm_machines_list[0]
harry = bank1.users_list[0]
harrys_account = harry.accounts_list[0]
harry_atm_card = harrys_account.atm_card
print("Ans :", atm_machine1.insert_card(bank1, harry_atm_card).get_data(), ", card_number:", harry_atm_card.card_number, sep=' ')


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
hermione = bank1.users_list[1]
hermiones_account = hermione.accounts_list[0]
print("\nTest case #2 :")
print("Hermione account before test :", hermiones_account.balance)

atm_machine1.deposit(hermiones_account, 1500) # Deposit 1000 to hermione account from atm_machine1

print("Hermione account after test :", hermiones_account.balance)



# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

depositment = atm_machine1.deposit(hermiones_account, -1)
print("\nTest case #3 :")
print("Hermione account after test :", hermiones_account.balance)


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print("\nTest case #4 :")
print("Hermione account before test :", hermiones_account.balance)
atm_machine1.withdraw(hermiones_account, 500) # Withdraw 500 from hermione account from atm_machine1
print("Hermione account after test :", hermiones_account.balance)


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print("\nTest case #5 :")
print("Hermione account before test :", hermiones_account.balance)
atm_machine1.withdraw(hermiones_account, 5000) # Withdraw 2000 from hermione account from atm_machine1
print("Hermione account after test :", hermiones_account.balance)

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print("\nTest case #6 :")
harrys_account = harry.accounts_list[0]
hermiones_account = hermione.accounts_list[0]
print("Harry account before test :", harrys_account.balance)
print("Hermione account before test :", hermiones_account.balance)

atm_machine1.transfer(hermiones_account, harrys_account, 1000) # Transfer 10000 from harry account to hermione account from atm_machine1

print("Harry account after test :", harrys_account.balance)
print("Hermione account after test :", hermiones_account.balance)


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500

print("\nTest case #7 :")
hermiones_transaction = hermiones_account.get_data()['transactions']
print("Hermione transaction :", [transaction for transaction in hermiones_transaction])