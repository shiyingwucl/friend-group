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



mean_relation(my_group)