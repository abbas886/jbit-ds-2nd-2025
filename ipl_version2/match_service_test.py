import match_service as ms

print("all the matches:", ms.get_all_matches())

print("match details of id : 1 ->" ,ms.get_match_by_id(1))

print("............")
print("all matches of RCB team: ")
      
print(ms.get_matches_by_team("RCB"))

new_match = {
    "id": 5,
    "team1": "KKR",
    "team2": "SRH",
    "date": "2023-04-15",
    "venue": "Eden Gardens",
    "result": "pending...."
}

#"KKR won by 5 wickets
ms.add_match(new_match)

updated_match = {
    "team1": "KKR",
    "team2": "SRH",
    "date": "2023-04-15",
    "venue": "Eden Gardens",
    "result": "KKR won by 5 wickets"
}

print("updating match id 5 -> ", ms.update_match(5, updated_match))

print("deleting match id 5 ->",ms.delete_match(5))



