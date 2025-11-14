import player_service
import unittest

def test_get_all_players():
    players = player_service.get_all_players()
    print("All Players:", players)
    assert len(players) > 0 # Ensure that we have at least one player  

def test_get_player():
    player_id = 1
    player = player_service.get_player(player_id)
    print(f"Player with ID {player_id}:", player)
    print(player[0]['id'])
    #assert player_id == player[0]['id']  # Ensure the correct player is fetched
    assert player != []  # Ensure that the player exists    

def test_add_player():
    new_player_id = 500
    response = player_service.add_player(new_player_id, "Test Player", "Test Team")
    print("Add Player Response:", response.json())
    assert response.status_code == 201  # Ensure the player was created successfully  
    delete_response = player_service.delete_player(new_player_id)
    print("Cleanup - Delete Player Response:", delete_response.status_code)  

def test_update_player():
    player_id = 999
    response = player_service.update_player(player_id, "Updated Player", "Updated Team")
    print("Update Player Response:", response.json())
    assert response.status_code == 200  # Ensure the player was updated successfully

def test_delete_player():
    player_id = 999
    response = player_service.delete_player(player_id)
    print("Delete Player Response:", response.status_code)
    assert response.status_code == 200  # Ensure the player was deleted successfully

def test_move_player_to_team():
    player_id = 2
    new_team = "New Team"
    response = player_service.move_player_to_team(player_id, new_team)
    print("Move Player to New Team Response:", response.json())
    assert response.status_code == 200  # Ensure the player was moved successfully  

def run_tests():    
    test_get_all_players()
    test_get_player()
    test_add_player()

if __name__ == "__main__":
    run_tests()
