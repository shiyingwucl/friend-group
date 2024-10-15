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

#returns the max age
def max_age(friend_group):
    ages = []
    for person in friend_group:
        for name in person.values():
            age = name.get("age")
            ages.append(age)
    print(max(ages))

def mean_relation():
    pass
def max_age_with_relation():
    pass

max_age(my_group)