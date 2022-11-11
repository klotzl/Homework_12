import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from Homework_12.lesson12_project_source_v3.functions import save_picture, add_post

loader_blueprint: Blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_2')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или информации'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        logging.info('Загруженый файл не картинка')
        return 'Неверное расширение файла'

    try:
        picture_path = '/' + save_picture(picture)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    post = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)
