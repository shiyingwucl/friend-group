import json
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [{"Jill":{"age": 26,
                     "job": "biologist",
                     "connection":{"Zalika":"friend",
                                   "John":"partner"}
                                   }
                                   },
            {"Zalika":{"age": 28,
                       "job": "artist",
                       "connection":{"Jill":"friend"}
                       }
                       },
            {"John":{"age": 27,
                     "job": "writer",
                     "connection":{"Jill":"partner"}
                     }
                     },
            {"Nash":{"age": 34,
                     "job": "chef",
                     "connection":{"John":"cousin",
                                   "Zalika":"landlord"}
                                   }
                                   }]

def max_age(friend_group):
    """returns the max age"""
    ages = [name.get("age") for person in friend_group for name in person.values()]

    print(max(ages))

def mean_relation(friend_group):
    """mean number of the relations in the group"""
    total_relations = [connection for person in friend_group for name in person.values() for connection in name.get("connection")]

    print(len(total_relations)/len(friend_group))

def max_age_with_relation(friend_group):
    """maximum age of people with atleast one relation"""
    ages = [name.get("age") for person in friend_group for name in person.values() if len(name.get("connection"))>=1]

    print(max(ages))

def max_age_with_friend(friend_group):
    """maximum age of people with at least one friend"""
    with_friend = []
    for person in friend_group:
        for attribute in person.values():
            for name,connection in attribute.get("connection").items():
                if connection == "friend":
                    with_friend.append(person)
    ages = [name.get("age") for person in with_friend for name in person.values()]
    print(max(ages))

with open ("friend_group","w")as file:
    file.write(json.dumps(my_group))

with open("friend_group","r") as file:
    print(json.load(file))