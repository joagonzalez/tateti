def banner():
    print("""
             _          _         _    _ 
            | |_  __ _ | |_  ___ | |_ (_)
            | __|/ _` || __|/ _ \| __|| |
            | |_| (_| || |_|  __/| |_ | |
            \__|\__,_| \__|\___| \__||_|
                                        
          """)

def instructions():
    print("""
              #### Board Positions ####
              
              (0,0)  | (1,0)  | (2,0)
             --------------------------
              (0,1)  | (1,1)  | (2,1) 
             --------------------------
              (0,2)  | (1,2)  | (2,2)
           """)

def new_player(players):
    _ok = False
    player = []
    # player name
    p_name = input("Player Name: ")
    player.append(p_name)
    # player type
    while not _ok:
        try:
            p_type = int(input("Player type [0 = Human, 1 = Computer]: "))
            if p_type == 1 or p_type == 0:
                player.append(p_type)
                _ok = True
            else:
                print("Insert a valid type!")    
        except Exception as e:
            print("Insert a valid type!")
    # player symbol
    if len(players) != 0:
        if players[0][2] == 0:
            p_symbol = 1
        else:
            p_symbol = 0
        player.append(p_symbol) 
    else: 
        _ok = False
        while not _ok:
            try:
                p_symbol = int(input("Player symbol [0 = 'X', 1 = 'O']: "))
                if p_symbol == 1 or p_symbol == 0:
                    player.append(p_symbol)
                    _ok = True
                else: 
                    print("Insert a valid symbol!")
            except Exception as e:
                print("Insert a valid symbol!")
    # player difficulty if computer type
    _ok = False
    if p_type == 1:
        while not _ok:
            try:
                p_difficulty = int(input("Player difficulty [0 = Easy, 1 = Difficult]: "))
                if p_difficulty == 0 or p_difficulty == 1:
                    player.append(p_difficulty)
                    _ok = True
                else:
                    print("Insert a valid difficulty!")
            except Exception as e:
                print("Insert a valid difficulty!")

    return player
        
def play_again():
    p_again = ''
    while p_again.upper() != 'Y' and p_again.upper() != 'N':
        p_again = input("Do you want to play again? [Y/N]")

    if p_again.upper() == 'Y':
        return True
    else:
        return False



        