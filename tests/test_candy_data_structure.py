import pytest
from candy_problem.candy_problem import * 



def test_get_friends_favorite_candy_count_nominal_cases():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    # Act
    dict = get_friends_favorite_candy_count(friend_favorites)

    # Assert
    assert dict["lollipop"] == 2

def test_get_friends_favorite_candy_count_edge_cases():
    # Arrange
    friend_favorites = [
        
    ]
    # Act
    dict = get_friends_favorite_candy_count(friend_favorites)

    # Assert
    assert dict == {}


def test_create_candy_data_structure_type_nominal_cases():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
# Add your own assertions to the test below
    # Assert
    assert type(new_candy_data) == dict

def test_create_candy_data_structure_type_edge_cases():
    # Arrange
    friend_favorites = [
       
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
# Add your own assertions to the test below
    # Assert
    assert type(new_candy_data) == dict

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    '''
    Add your assertions here!
    '''

    # Assert
    assert len(new_candy_data) == 8
'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
def test_get_friends_who_like_specific_candy_norminal_cases():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    candy = "lollipop"

    # Act
    friend_tuple = get_friends_who_like_specific_candy(friend_favorites, candy)
    
    # Assert
    assert friend_tuple == ("Sally","Bob")


def test_get_friends_who_like_specific_candy_edge_cases():

    # Arrange
    friend_favorites = [
        
    ]
    candy = "lollipop"

    # Act
    friend_tuple = get_friends_who_like_specific_candy(friend_favorites, candy)
    
    # Assert
    assert friend_tuple is None

def test_create_candy_set_norminal_cases():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
  

    # Act
    candy_set = create_candy_set(friend_favorites)
    
    # Assert
    assert candy_set == set( ["lollipop", "bubble gum", "laffy taffy","milky way", "licorice",
                        "chocolate bar","nerds", "sour patch kids"])
    
def test_create_candy_set_edge_cases():

    # Arrange
    friend_favorites = [
       
    ]
  

    # Act
    candy_set = create_candy_set(friend_favorites)
    
    # Assert
    assert candy_set == set()