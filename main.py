#--------------------------------------------------------
#--------------Libraries and Modules---------------------
#-------------------Mason Skinner------------------------
#-------------------April 1, 2022------------------------
#--------------------------------------------------------

from time import sleep
from followers import followerpresets
from followers import createfollowers

follower_list = followerpresets.followers

def main():
    print("Before you leave on your adventure, choose a companion to keep you company!(or make your own by typing new!)")
    i = 0
    for name in follower_list:
        print(follower_list[i])
        sleep(1)
        i = i + 1
    print("new")
    choice = input('> ').lower()
    if choice == 'ingrid':
        follower = followerpresets.ingrid
    elif choice == 'jeff':
        follower = followerpresets.jeff
    elif choice == 'seth':
        follower = followerpresets.seth
    elif choice == 'new':
        follower = createfollowers.create()
    sleep(2)
    print(f"{follower['name']} greets you warmly as they join you for the adventure!")


#-------Main---------------
main()