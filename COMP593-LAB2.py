def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'fullname' : 'Samuel Bronson',
        'student_id' : '10259648', 
        'pizza_toppings' : 
        [
            'PEPPERONI', 
            'MUSHROOMS', 
            'JALAPENOS',
        ],
        'movie' : 
        [
            {
            'title' : 'puss and boots: the last wish',
            'genre' : 'family friendly'
            },
            {
            'title' : 'the lighthouse (2019)',
            'genre' : 'horror'
            }
        ],
    }
    
    # TODO: Step 3 - Add another movie to the data structure\

    add_movies(about_me)
    
    # about_me['movie'].insert(1, {'title': 'the secret of walter mitty', 'genre' : 'comedy'})

    #Print

    print_student_name_and_id(about_me)
    
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me)
    print_pizza_toppings(about_me)


    print_movie_genres(about_me)
    
    print_movie_titles(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    firstname = about_me['fullname'].split()[0]
    print(f"My name is {about_me['fullname']} but you can call me {firstname}")
    print(f"My student ID is {about_me['student_id']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me):
    toppings = "bacon", "sausage"
    about_me['pizza_toppings'].extend(toppings)

    for i,p in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = p.lower()

    about_me['pizza_toppings'].sort()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy faviourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'- {p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def add_movies(about_me): 
    about_me['movie'].insert(1, {'title': 'the secret of walter mitty', 'genre' : 'comedy'})
    
def print_movie_genres(about_me):
    print('\nI like to watch ', end='')
#    for m,g in enumerate(about_me['genre']):
#       if m < len(about_me['genre']) - 1:
#           print(f"{g['genre']}, ", end='')
#       else:
#            print(f"{g['genre']}")

    for g in about_me['movie']:
        print(f"{g['genre']}", end=", ") 
    else: 
        print(f"and {g['genre']}")
    
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(about_me):
    print(f"\nSome of my favourite movies are ", end='')
#    for m,t in enumerate(about_me['title']):
#        if m < len(about_me['title']):
#            print(f"{t['title']}, ", end='')
#        else:
#            print(f"{t['title']}")

    for t in about_me['movie']:
        print(f"{t['title']}", end=", ") 
    else: 
        print(f"and {t['title']}")
    

    return
    
if __name__ == '__main__':
    main()