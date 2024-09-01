def players_by_position(squads_list):
    
    player_dic = {}
    for item in squads_list:
        position = item['position']
        # print(position)
        if position not in player_dic:
            player_dic[position] = []
        player_dic[position].append(item)
         
    return player_dic
