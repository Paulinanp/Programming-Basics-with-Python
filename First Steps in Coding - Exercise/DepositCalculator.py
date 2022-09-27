amountDeposited = float(input())
termOfTheDeposit = int(input())
annualInterestRate = float(input())

sum = amountDeposited + termOfTheDeposit * ((amountDeposited * (annualInterestRate / 100) / 12))

print(sum)