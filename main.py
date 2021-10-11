from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"how many days did {name1} stay in the house during the bill period? "))

name2 = input("What is your name? ")
days_in_house2 = int(input(f"how many days did {name2} stay in the house during the bill period? "))


the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print("{name1} pays: ", flatmate1.pay(bill = the_bill, flatmate2 = flatmate2))
print("{name2} pays: ", flatmate2.pay(bill = the_bill, flatmate2 = flatmate1))

pdf_report = PdfReport(filename =f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1 = flatmate1, flatmate2 = flatmate2, bill = the_bill)


