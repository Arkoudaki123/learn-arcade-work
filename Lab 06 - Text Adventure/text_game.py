# A text adventure game
class Room:
    """
    this class represents the rooms in the playing area
    """

    def __init__(self, name, descr, north, east, south, west, up, down):
        """ This is a method that sets up the variables in the object. """
        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


def main():
    """ This is my main program function """

    # this code populates the room info
    room_list = []
    names = ['Dining Room', 'Hall', 'Lounge', 'Library', 'Store', 'Kitchen', 'Attic', 'Bathroom', 'Secret tent']
    descriptions = [
        'You are in a dining room with chandeliers made of gold.You see a door to the west and the north',
        ' You are in a long hall with doors to your north, east,up and west',
        ' You are in a lounge with sofas surrounding you, you see a door to the north and to the east',
        ' You are in a library with books around you, you see a door to the south and to the west',
        'You are in a store filled with sodas and sandwiches, you see a door to the south and to the east',
        ' You are in a kitchen surrounded by knives and raw meat you see a door to the north',
        'You are in an attic a very boring attic you can only go down, up and east',
        'You are in a bathroom with a sink',
        'You are on top of the roof with your secret tent if you got yelled at by your parents'
    ]
    norths = [5, None, 3, None, None, None, None, None, None]
    easts = [1, 2, None, None, 3, 4, None, None, None]
    souths = [None, None, None, 2, None, 0, None, None, None]
    wests = [None, 0, 1, 4, 5, None, None, 6, None]
    ups = [None, 6, None, None, None, None, 8, None, None]
    downs = [None, None, None, None, None, None, 1, None, 6]
    for i in range(len(names)):
        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    # this code sets the game
    current_room = 1
    done = False
    while not done:
        print(room_list[current_room].description)
        answer = input('What do you want to do? Enter n for north, e for east, s for south, w for west, u for up, '
                       'd for down, q to quit: ')
        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == 'n':
            new_room = room_list[current_room].north
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'e':
            new_room = room_list[current_room].east
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'w':
            new_room = room_list[current_room].west
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 's':
            new_room = room_list[current_room].south
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'u':
            new_room = room_list[current_room].up
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'd':
            new_room = room_list[current_room].down
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room

        elif move == 'q':
            print('Goodbye. I hope you liked exploring the house.')
            done = True
        else:
            print('Sorry, I did not understand your answer')


main()
