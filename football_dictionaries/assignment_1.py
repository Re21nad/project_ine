def players_as_dictionaries(squads_list):
    # List to dictionary
    player_list = []

    for item in squads_list:
        player_dic = {
            'number': item[0],
            'position': item[1],
            'name': item[2],
            'date_of_birth': item[3],
            'caps': item[4],
            'club': item[5],
            'country': item[6],
            'club_country': item[7],
            'year': item[8]
        }
        player_list.append(player_dic)
        
    return player_list