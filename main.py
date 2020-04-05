import json
import os


class InfoHandler():
    """Class that asks user to input some info"""

    def __init__(self):
        """Initializes self"""

        # A dictionary to store the prompts that will be printed to the user
        self.required_info = {
            'name': 'What is your name?\n\t',
            'age': 'What is your age\n\t',
            'country': 'What country do you live in?\n\t',
            'battlecups': 'How many battle cups have you won?\n\t'
        }

        # Creates an empty dict to store users
        self.stored_users = {}
        # A list that specifies which answers need to intergers
        self.requires_int = ['age', 'battlecups']

    def check_if_int(self, answer):
        """Checks if user input an interger"""

        # Tries converting the answer to an int and back
        try:
            _ = int(answer)
            is_int = True
            return is_int

        except ValueError:
            print("\nPlease enter a number intead:")
            is_int = False
            return is_int

    def create_new_user(self):
        """Handles getting new inputs from users"""

        # creates an empty dict to store the inputs in
        user = {}

        # Loops through all the question in the required info dict and adds
        # them to a dict
        for key in self.required_info.keys():

            # Block that makes sure you put in numbers for stuff like age
            if key in self.requires_int:
                is_int = False
                # Loops asking for a new input as long as it isnt an int
                while is_int is False:
                    answer = input(self.required_info[key])
                    is_int = self.check_if_int(answer)

                # Stores the numbers after passing the loop
                user[key] = answer.lower()

            else:
                answer = input(self.required_info[key])
                user[key] = answer.lower()

        # Stores a user by name in the stored users dict
        self.stored_users[user['name']] = user
        print('\n Your information has been added')

    def save_stored_users(self):
        """Saves the stored_users dict to a Json"""

        with open('saved_users.json', 'w') as f:
            json.dump(self.stored_users, f)

    def load_stored_users(self):
        """loads the stored_users dict to a Json"""

        with open('saved_users.json') as f:
            self.stored_users = json.load(f)

    def get_stored_user(self):
        """gets the info on the requested user"""

        requested_info = \
            input('What is the name of the user you are looking for\n\t')

        # Checks if there is any user by the requested name in the dict
        try:
            requested_user = self.stored_users[requested_info.lower()]

            print('\nWe found a match! \n')
            for key, value in requested_user.items():
                print(key.title() + ': ' + value.title())

        except KeyError:
            print("\nI couldn't find any user by that name")

    def show_all_users(self):
        """shows the names of all the stored users"""

        print('\nHere are the names of all the user I have stored\n')

        for key, value in self.stored_users.items():
            print(key.title())

    def shutdown(self):
        """saves the stored user dict before shutting down"""

        # Saves the dict to the saved_users Json
        self.save_stored_users()
        print('\nShutting down')
        quit()


my_handler = InfoHandler()
keep_going = True

my_handler.load_stored_users()

# A loop that keeps the program running until the user calls for shutdown
while keep_going:

    with open(os.path.join("textfiles", "menu.txt")) as f:
        menu_text = f.read()

    # Gets the requested action from the user
    r_action = input(menu_text)

    if r_action == '1' or r_action.lower() == 'store a new user':
        my_handler.create_new_user()

    elif r_action == '2' or r_action.lower() == 'find an existing user':
        my_handler.get_stored_user()

    elif r_action == '3' or r_action.lower() == 'show all users':
        my_handler.show_all_users()

    elif r_action == '4' or r_action.lower() == 'shutdown':
        my_handler.shutdown()

    else:
        print('\nThat is not a valid input')
