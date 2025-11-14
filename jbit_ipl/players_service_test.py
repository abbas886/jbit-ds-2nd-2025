import player_service as service    


print("All the plaers : " , service.get_players())

service.get_player_by_id(5)
print("Player by id 1 : ", service.get_player_by_id(1))

player = {
            "id": 101,
            "name": "Rohit Sharma",
            "team": "mumbai indians",
            "role": "Batsman",
            "matches_played": 200,
            "runs_scored": 10000,
            "wickets_taken": 20
        }

print("adding player->",service.add_player(player))
print("After adding player : ", service.get_player_by_id(101))

print(".......")
print("All the plaers : " , service.get_players())


player = {
            "id": 101,
            "matches_played": 202,
            "runs_scored": 10150,
            "wickets_taken": 25
        }
print("updating player -> " ,service.update_player(101, player))

print("Before updating player******* : ", service.get_player_by_id(101))
print("updating player -> " ,service.update_player(101, player))
print("After updating player******* : ", service.get_player_by_id(101))

print("Deleting player with id 101 -> ", service.delete_player(101))
print("After deleting player ####: ", service.get_player_by_id(101))
print("All the plaers#### : " , service.get_players())


