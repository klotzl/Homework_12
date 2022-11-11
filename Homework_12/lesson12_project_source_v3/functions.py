import logging
from json import JSONDecodeError
import json


def load_posts():
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'


def get_by_word(word):
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
