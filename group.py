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
    all_relations = [name.get("connection") for person in friend_group for name in person.values() for connection in ]
    print(len(all_relations)/len(my_group))

def max_age_with_relation():
    pass

mean_relation(my_group)