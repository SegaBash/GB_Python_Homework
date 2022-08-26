# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def answer(question:str):
    bot_database = {
    'привет' : 'здравствуйте',
    'как тебя зовут' : 'у девочки нет имени'
    }
    question_list = list(bot_database)
    return bot_database[question.lower()]



user_input = input('Ваша фраза: ')
while (user_input.lower() != 'выход'):
    print(answer(user_input))
    user_input = input('Ваша фраза: ')