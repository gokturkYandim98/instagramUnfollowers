# Please read the README file to how to use!
# YOU DONT NEED TO PROVIDE YOUR INSTAGRAM LOGIN CREDENTIALS TO USE THIS TOOL!
# Results may not be %100 correct, it might be a good idea to manually check some of them if you are not sure.

import re

followers = []
following = []
notFollowingBack = []


# This function iterates a text file (followers or following) and extracts peoples names
def iterate(fileName):
    file = open(fileName, encoding="utf8")

    nickName = '_aade\">'
    realName = '_aaeq">'
    
    # Loop through the file line by line
    for line in file:  
        for m in re.finditer(realName, line):
            start_index = m.end()
            end_index = line.find("<",start_index)
            followers.append(line[start_index:end_index])

    file.close() 


# This function compares followers and following people to find the people that does not follow you - Annoying people :)
def findNotFollowing():
    for i in following:
        if not i in followers:
            notFollowingBack.append(i)


# Main Function
if __name__ == "__main__":
    iterate("followers.txt")
    iterate("following.txt")
    findNotFollowing()

    print('Followers Count: ',len(followers))
    print('Following Count: ', len(following))
    print(', '.join(notFollowingBack))