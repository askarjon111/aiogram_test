async def get_age(name):
    users = {
        'John': 12,
        'Asilbek': 23,
        'Azizbek': 20,
    }
    try:
        return str(users[name])
    except KeyError:
        return "Bunday foydalanuvchi bazada topilmadi."
