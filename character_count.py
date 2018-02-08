message='it was  a bright cold day in april, and the clocks were striking thirteen.'
count={}

for charecter in message:
    count.setdefault(charecter,0)
    count[charecter]=count[charecter]+1

print(count)
