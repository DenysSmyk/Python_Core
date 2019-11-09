cap = 10
on = 5
wait =5
a=cap -on -wait
if cap-on >= 50:
    print("He can fit all {} passengers".format(wait))
else:
    print("He cant fit {} out of {} waiting".format(a, wait))