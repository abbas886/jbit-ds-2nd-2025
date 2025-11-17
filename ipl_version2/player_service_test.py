import player_service as service


print(" All players: ",service.get_all_players())


print("player 3 details L",service.get_player_by_id(30))

print("All team members of RCB", service.get_player_by_team("RCB"))

new_player =  {
      "id": 5,
      "name": "Suresh Raina",
      "team": " CSK",
      "role": "Batsman",
      "matches":  150,       
      "runs": 5400,
      "average": 36
      }
print("Adding new player: ", service.add_player(new_player))    

player =  {
      "id": 4,
      "name": "Rohit Sharma",
      "team": "MI",
      "role": "Batsman",
      "matches": 202,
      "runs": 10090,
      "average": 54
      }
print("updating player 4:", service.update_player(4, player))
print("After update, player 4 details: ",service.get_player_by_id(4))
print("Deleting player 5:", service.delete_player(5))



