import requests
from sdamgia import SdamGIA
from services.perexodnik import from_svg_to_png

sd = SdamGIA()


def get_png(subject: str, id: str) -> list:
    level = sd.get_problem_by_id(subject=subject, id=id)
    all_images = []
    for i in level['condition']['images']:
        svg_file = requests.get(i).text
        all_images.append(from_svg_to_png(svg=svg_file))
    return all_images


def get_answer(subject: str, id: str) -> str:
    level = sd.get_problem_by_id(subject=subject, id=id)
    return (str(level['solution']['text'])[level['solution']['text'].find('Ответ:') + 6: level['solution']['text'].find('Ответ:') + 6 + (str(level['solution']['text'])[level['solution']['text'].find('Ответ:') + 6:].find('.'))]).strip()


def get_decision(subject: str, id: str) -> str:
    level = sd.get_problem_by_id(subject=subject, id=id)
    return str(level['solution']['text'])


def get_decision_images(subject: str, id: str) -> str:
    level = sd.get_problem_by_id(subject=subject, id=id)
    all_images = []
    for i in level['solution']['images']:
        svg_file = requests.get(i).text
        all_images.append(from_svg_to_png(svg=svg_file))
    return all_images


def get_level(subject: str, id: str) -> str:
    level = sd.get_problem_by_id(subject=subject, id=id)
    return level['condition']['text']
