import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from Homework_12.lesson12_project_source_v3.functions import get_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_1')


@main_blueprint.route("/")
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_key = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = get_by_word(search_key)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', request=search_key, posts=posts)
