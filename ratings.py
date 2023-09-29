"""Restaurant rating lister."""


def read_ratings(filename):
    restaurant_ratings = {}
    the_file = open(filename)
    for line in the_file:
        line = line.replace('\n', '')
        restaurant_entry = line.split(':')
        
        restaurant_name = restaurant_entry[0]
        rating = restaurant_entry[1]
        restaurant_ratings[restaurant_name] = int(rating)


    the_file.close()
    return restaurant_ratings

 
def print_sorted_ratings(rating_dictionary):
    rating_list = rating_dictionary.items()
    sorted_ratings = sorted(rating_list)

    for name, rating in sorted_ratings:
        print(f"{name} is rated at {rating}") 



def add_new_restaurant():
    decision_to_add = input("Would you like to add another restaurant? [y/n]")
    while True:
        if decision_to_add == 'y':

            restaurant_name = input("What's the name of your restaurant? ")
            restaurant_rating = input("What is the rating score? ")
            restaurant_rating = int(restaurant_rating)

            restaurant_ratings[restaurant_name] = restaurant_rating

            print_sorted_ratings(restaurant_ratings)
            return restaurant_ratings

        elif decision_to_add == 'n':
            print("Current list is:")
            print_sorted_ratings(restaurant_ratings)
            break
            
        else:
            decision_to_add = input("Please enter 'y' or 'n': ")




restaurant_ratings = read_ratings('scores.txt')
print_sorted_ratings(restaurant_ratings)

restaurant_ratings = add_new_restaurant()







