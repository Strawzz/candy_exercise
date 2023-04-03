'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_favorite_candy_count(friend_favorites):
    friend_favorite_candy_dict = {}
    
    for friend in friend_favorites:
        for candy in friend[1]:
            friend_favorite_candy_dict[candy] = friend_favorite_candy_dict.get(candy,0) +1
    return friend_favorite_candy_dict
    

'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(friend_favorites):
    candy_dict = {}

    for friend in friend_favorites:
        for candy in friend[1]:
            if candy in candy_dict:
                candy_dict[candy].append(friend[0])
            else:
                candy_dict[candy] = [friend[0]]
    return candy_dict
    

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(friend_favorites, candy_name):
    candy_dict = create_new_candy_data_structure(friend_favorites)
    if candy_dict:
        friend_list = candy_dict[candy_name]
        return tuple(friend_list)
    else:
        return None



'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    candy_dict = create_new_candy_data_structure(data)
    print(candy_dict.keys())
    print(set(candy_dict.keys()))
    return set(candy_dict.keys()) 

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

