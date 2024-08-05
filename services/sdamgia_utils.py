import requests
from sdamgia import SdamGIA
from services.svg_to_png import from_svg_to_png

sd = SdamGIA()


def fetch_problem_data(subject: str, id: str) -> dict:
    """Получаем данные задания по предмету и айди.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        dict: Данные задания
    """
    return sd.get_problem_by_id(subject=subject, id=id)


def convert_images(images: list) -> list:
    """Конвертируем SVG изображения в PNG.

    Args:
        images (list): Список URL изображений в формате SVG

    Returns:
        list: Список изображений в формате PNG
    """
    all_images = []
    for image_url in images:
        svg_file = requests.get(image_url).text
        all_images.append(from_svg_to_png(svg=svg_file))
    return all_images


def get_png(subject: str, id: str) -> list:
    """Получаем изображения задания по предмету и айди, переводим в PNG формат.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        list: Список изображений
    """
    problem_data = fetch_problem_data(subject, id)
    return convert_images(problem_data["condition"]["images"])


def get_answer(subject: str, id: str) -> str:
    """Получаем ответ для математических задач в строковом представлении.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Ответ
    """
    problem_data = fetch_problem_data(subject, id)
    solution_text = problem_data["solution"]["text"]
    answer_start = solution_text.find("Ответ:") + 6
    answer_end = solution_text[answer_start:].find(".") + answer_start
    return solution_text[answer_start:answer_end].strip()


def get_decision(subject: str, id: str) -> str:
    """Получаем решение задачи.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Решение
    """
    problem_data = fetch_problem_data(subject, id)
    return problem_data["solution"]["text"]


def get_decision_images(subject: str, id: str) -> list:
    """Получаем изображения решения по предмету и айди, переводим в PNG формат.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        list: Список изображений
    """
    problem_data = fetch_problem_data(subject, id)
    return convert_images(problem_data["solution"]["images"])


def get_level(subject: str, id: str) -> str:
    """Получаем задание.

    Args:
        subject (str): Предмет изучения
        id (str): Айди задания

    Returns:
        str: Задание
    """
    problem_data = fetch_problem_data(subject, id)
    return problem_data["condition"]["text"]
