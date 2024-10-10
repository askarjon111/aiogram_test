from contents import words


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


async def calculate(text: str):
    try:
        if '+' in text:
            ans = int(text.split('+')[0]) + int(text.split('+')[1])
        elif '-' in text:
            ans = int(text.split('-')[0]) - int(text.split('-')[1])
        elif '*' in text:
            ans = int(text.split('*')[0]) * int(text.split('*')[1])
        elif '/' in text:
            ans = int(text.split('/')[0]) / int(text.split('/')[1])
        return str(ans)
    except Exception as e:
        return f"{e}"


async def get_word(key, lang = 'uz'):
    word = words.get(key+ '-' + lang)
    return word
