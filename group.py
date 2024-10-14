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
                    "connection":{"Jill":"partner"}}
                    },
            {"Nash":{"age": 34,
                    "job": "chef",
                    "connection":{"John":"cousin",
                                  "Zalika":"landlord"}}
                    }]

print(my_group[1]["Zalika"])
