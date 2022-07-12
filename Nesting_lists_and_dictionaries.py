# nesting list inside list
# list = [1,2,3,4,5,6,[7,8,9,[10,11,12]]]
# print(list[6][3][1])

# nesting list and dictionary
# trip = {
#     "Madhya Pradesh": ["Jabalpur", "Bhopal", "Indore"],
#     "Maharashtra": ["Mumbai", "Pune", "Nagpur"]
# }
# print(trip["Maharashtra"][1])

trip = {
    "Madhya Pradesh": {
        "cities_visited": ["Jabalpur", "Bhopal", "Indore"],
        "no_of_visits": 3
    },
    "Maharashtra": {
        "cities_visited": ["Mumbai", "Pune", "Nagpur"],
        "no_of_visits": 5
    }
}
# print(trip["Madhya Pradesh"]["no_of_visits"])
# chhattisgarh
# cities - "Durg", "Bilaspur"
# no_of_visits: 5

dict = {}
dict["cities_visited"] = ["Durg", "Bilaspur"]
dict["no_of_visits"] = 5

trip["Chhattisgarh"] = dict
print(trip)