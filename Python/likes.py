#Python 3.10.9

#Challenge description here
# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items. W
# e want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"



def return_likes(names):
    match len(names):
        case 0:
            return 'no one likes this'
        case 1:
            return names[0]+' likes this'
        case 2:
            return names[0]+' and '+names[1]+' like this'
        case 3:
            return names[0]+', '+names[1]+' and '+names[2]+' like this'
        case _ if len(names) > 3:
            return names[0]+', '+names[1]+' and '+str(len(names)-2)+' others like this'


if __name__ == '__main__':
    return_likes([])
    return_likes(["Peter"])
    return_likes(["Jacob", "Alex"])
    return_likes(["Max", "John", "Mark"])
    return_likes(["Alex", "Jacob", "Mark", "Max"])
