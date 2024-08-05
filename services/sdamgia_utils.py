import requests
from sdamgia import SdamGIA
from services.svg_to_png import from_svg_to_png

sd = SdamGIA()


def get_png(subject: str, id: str) -> list:
    """Получаем изображения задания по предмету и айди, переводим в пнг формат

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        list: Список изображений
    """
    level = sd.get_problem_by_id(subject=subject, id=id)
    all_images = []
    for i in level["condition"]["images"]:
        svg_file = requests.get(i).text
        all_images.append(from_svg_to_png(svg=svg_file))
    return all_images


def get_answer(subject: str, id: str) -> str:
    """Получаем ответ для математических задач в строковом представлении

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Ответ
    """
    level = sd.get_problem_by_id(subject=subject, id=id)
    return (
        str(level["solution"]["text"])[
            level["solution"]["text"].find("Ответ:")
            + 6 : level["solution"]["text"].find("Ответ:")
            + 6
            + (
                str(level["solution"]["text"])[
                    level["solution"]["text"].find("Ответ:") + 6 :
                ].find(".")
            )
        ]
    ).strip()


def get_decision(subject: str, id: str) -> str:
    """Получаем решение задачи

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Решение
    """
    level = sd.get_problem_by_id(subject=subject, id=id)
    return str(level["solution"]["text"])


def get_decision_images(subject: str, id: str) -> str:
    """Получаем изображения решения по предмету и айди, переводим в пнг формат

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        list: Список изображений
    """
    level = sd.get_problem_by_id(subject=subject, id=id)
    all_images = []
    for i in level["solution"]["images"]:
        svg_file = requests.get(i).text
        all_images.append(from_svg_to_png(svg=svg_file))
    return all_images


def get_level(subject: str, id: str) -> str:
    """Получаем задание

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Задание
    """
    level = sd.get_problem_by_id(subject=subject, id=id)
    return level["condition"]["text"]