def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'fullname' : 'Samuel Bronson',
        'student id' : '10259648', 
        'pizza toppings' : ['PEPPERONI', 'MUSHROOMS', 'JALAPENOS'],
        'movie' : 
    [
        {
            'title' : 'puss and boots: the last wish',
            'genre' : ['family friendly', 'action', 'fantasy']
        },
        {
            'title' : 'the lighthouse (2019)',
            'genre' : ['horror','black and white', 'psychological']
        }
    ]
    }
    
    # TODO: Step 3 - Add another movie to the data structure
    
    about_me['movie'].insert(1, {'title': 'the secret of walter mitty'})

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    firstname = about_me['fullname'].split()[0]
    print(f"My name is {about_me['fullname']} but you can call me {firstname}")
    print(f"My student ID is {about_me['student id']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza toppings'].extend([toppings])
    toppings = ['bacon', 'sausage']
    for i,p in enumerate(about_me['pizza toppings']):
        about_me['pizza toppings'][i] = p.lower()

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy faviourite pizza toppings are:')
    for p in about_me['pizza toppings']:
        print(f'- {p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print('\nI like to watch ', end='')
    for m,g in enumerate(about_me['genre']):
        if m < len(about_me['genre']) - 1:
            print(f"{g['genre']}, ", end='')
        else:
            print(f"{g['genre']}")
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print(f"\n Some of my favourite movies are", end='')
    for m,t in enumerate(movie_list['title']):
    return
    
if __name__ == '__main__':
    main()