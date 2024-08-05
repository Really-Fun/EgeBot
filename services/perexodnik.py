from cairosvg import svg2png

svg_code = """
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12" y2="16"/>
    </svg>
"""


def from_svg_to_png(svg: str, dpi: int = 300, antialiasing: int = 0.8):
    """Переводит svg изображение в png и улучшает качество

    Args:
        svg (str): Путь к svg файлу
        dpi (int, optional): Dpi. Defaults to 300.
        antialiasing (int, optional): Antialiasing - сглаживание. Defaults to 0.8.

    Returns:
        _type_: Возвращает png файл, размещенный в SchoolProjectBot/your_image.png
    """
    png_file = svg2png(bytestring=svg, dpi=dpi, scale=1/antialiasing)
    return png_file