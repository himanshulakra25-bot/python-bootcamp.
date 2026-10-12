def lateFee(books,membership,day):
    if books == "y" or books == "yes":
        if day <= 5:
            amount = 5*5
        else:
            amount = 5*5 + ((day-5)*10)
    else:
        if day <= 5:
            amount = 5*5
        else:
            amount = 5*5 + ((day-5)*20)
    
    if membership == "y" or membership == "yes":
        total = amount - (amount*0.20)
    else:
        total = amount
    return total
print(lateFee(books,membership,day))
