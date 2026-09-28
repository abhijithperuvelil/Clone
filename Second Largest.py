number=[10,32,43,12,7,98]
largest=number[0]
second_largest=number[0]


for num in number:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num !=largest:
        second_largest=num

print('Largest: ',largest)
print('second Largest: ',second_largest)


# * * * * * * *
# *           *
# *           *
# * * * * * * *