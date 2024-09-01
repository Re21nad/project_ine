def players_by_country_and_position(squads_list):
    
    country_dic = {}

    for position, players in squads_list.items():
        # print(position)
        for player in players:
            country = player['country']
            
            # Ensure the country is a key in the result dictionary
            if country not in country_dic:
                country_dic[country] = {
                    'GK': [],
                    'MF': [],
                    'FW': []
                }
    
            # Append the player dictionary to the appropriate list
            country_dic[country][position].append(player)
    
    return country_dic