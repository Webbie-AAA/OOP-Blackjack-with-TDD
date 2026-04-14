from datetime import datetime


def get_villain_name(birthdate: datetime) -> str:
    first = ["The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
             "The Disreputable", "The Atrocious", "The Twirling",  "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin",
            "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    first_name_index = birthdate.month
    if birthdate.day <= 9:
        second_name_index = birthdate.day
    else:
        second_name_index = int(str(birthdate.day)[1])

    return f"{first[first_name_index-1]} {last[second_name_index]}"


format_str = '%d/%m/%Y'
print(get_villain_name(datetime.strptime("1/1/2000", format_str)))
now = datetime.strptime("1/1/2000", format_str)
