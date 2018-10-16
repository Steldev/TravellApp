"""valid file formats"""

formats_files = {

    'IM': ['jpg', 'jpeg', 'png', 'gif', ],
    'VD': ['mp4', ],
    'AU': ['mp3', ],
    'FL': ['txt', 'doc', 'docx', ],
}


def check_files_formats(exts):
    """Проверяет валидность формата файла.
    Получает список расширеший и возвращает соответствующие им типы файла.
    В случае получения неподдерживаемого формата возвращает пустое значение
    """
    type_file = []
    for ext in exts:
        for key in formats_files.keys():
            if ext in formats_files[key]:
                type_file.append(key)

    if len(exts) != len(type_file):
        return None

    return type_file
