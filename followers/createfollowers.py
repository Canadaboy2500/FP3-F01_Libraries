


def create():
    print("What is their name?")
    name = input('> ')
    print("What is their race?")
    race = input('> ')
    print("What is their gender?")
    gender = input('> ')
    print("What level will they start at?")
    level = int(input('> '))
    print("What will their health start at?")
    health = int(input('> '))
    name = {'name':name, 'race':race, 'gender':gender, 'level':level, 'health':health}
    return(name)