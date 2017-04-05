import random
def score ():
    random_num = random.randint(60,100)
    message = ""
    if random_num <= 69 and random_num > 60:
        message += "Score: " + str(random_num) + "; Your garde is D.."
    elif random_num <= 79 and random_num >70:
        message += "Score: " + str(random_num) + "; Your garde is ..C"
    elif random_num <= 89 and random_num >= 80:
        message += "Score: " + str(random_num) + "; Your garde is ..B"
    else:
        message += "Score: " + str(random_num) + "; Your garde is .. A"
    print message
score()
