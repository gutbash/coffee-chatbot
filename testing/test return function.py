def bot():
    password = coffee()
    print(password)

def coffee():
    res = input('Password: ')
    if res == 'test':
        return res
    else:
        return coffee()

bot()