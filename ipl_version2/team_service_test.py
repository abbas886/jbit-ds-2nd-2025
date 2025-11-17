import team_service as service


print(" All teams", service.get_all_teams())

print("team 2 details ",service.get_team_by_id(2))

# why it is not fetching?
print("team details for RCB", service.get_team_by_name("Royal Challengers Bangalore"))

new_team = {
    
    "id": "4",
      "name": "sunrisers hyderabad ",
      "abbreviation": "SRH",
      "city": "Hyderabad",
      "championshipsWon": 5
}
print("Adding new team: ", service.add_team(new_team))

team =  {
    
      "id": "4",
      "name": "sunrisers hyderabad ",
      "abbreviation": "SRH",
      "city": "Hyderabad",
      "championshipsWon": 6
}
#supposed to call service.update_team
service.update_team("4", team)
print("After update, team 4 details: ",service.get_team_by_id(3))
print("Deleting team 4:", service.delete_team("3"))

