# Define

print('Welcome to the cafe!')
def coffee_bot():
    size = get_size()
    drink_type = get_drink_type()
    print('Alright, that\'s a {} {}!'.format(size, drink_type))
    name = input('Can I get your name please?: ')
    print('Thanks, {}! Your drink will be ready shortly.'.format(name))
    return

def print_message():
    return print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
        res = 'small'
        return res
    elif res == 'b':
        res = 'medium'
        return res
    elif res == 'c':
        res = 'large'
        return res
    else:
        print_message()
        return get_size()
    return 'ERROR'

def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% Milk \n[b] Non-Fat Milk \n[c] Soy Milk \n> ')
    if res == 'a':
        res = 'latte'
        return res
    elif res == 'b':
        res = 'non-fat latte'
        return res
    elif res == 'c':
        res = 'soy latte'
        return res
    else:
        print_message()
        return order_latte()
    return 'ERROR'

def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
        res = 'Brewed Coffee'
        return res
    elif res == 'b':
        res = 'Mocha'
        return res
    elif res == 'c':
        res = order_latte()
        return res
    else:
        print_message()
        return get_drink_type()
    return 'ERROR'

# Call

coffee_bot()