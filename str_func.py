# bad code
def text_to_upper(text):
    """
    :param text: текст
    :return: текст большими буквами
    """
    return text.upper()


def first_characters_text_to_upper(text):
    """
    :param text: текст
    :return: текст с заглавными буквами в каждом слове
    """
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)

