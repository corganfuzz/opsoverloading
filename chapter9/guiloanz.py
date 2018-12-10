from tkinter import *


class GuiLoanz:

    def __init__(self):
        window = Tk()
        window.title("Compare Interest Rates")

        Label(window, text='Loan Amount').grid(row=1, column=1)
        Label(window, text='Years').grid(row=1, column=3)

        self.loanAmount = StringVar()
        Entry(window, textvariable=self.loanAmount).grid(row=1, column=2)

        self.Years = StringVar()
        Entry(window, textvariable=self.Years).grid(row=1, column=4)

        Button(window, text="Calculate", command=self.printCalculation()).grid(row=1, column=5)

        Text(window, padx=5, pady=5, width=20, height=6).grid(row=2, column=1, padx=5, pady=5,  sticky=W)

        self.monthlyInterestRate = 0.05

        self.monthlyPayment = int(self.loanAmount.get()) * self.monthlyInterestRate / (
                1 - 1 / (1 + self.monthlyInterestRate) ** (int(self.Years.get()) * 12))

        window.mainloop()

    # def CalculateLoan(self):
    #     return

    def printCalculation(self):

        balance = self.loanAmount

        for i in range(24):
            interest = int(self.monthlyInterestRate * balance * 100) / 100
            mPay = int((self.monthlyPayment - interest) * 100) / 100
            balance = int((balance - mPay) * 100) / 100
            print(str(i) + "\t\t" + str(interest) + "\t\t" + str(mPay) + "\t\t" + str(balance))

        # def getMonthlyPayment(self, loanAmount, monthlyInterestRate, Years):
        #     monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (Years * 12))
        #     return monthlyPayment


GuiLoanz()

