"""valid file formats"""
from Lib import FFD

formats_files = {

    FFD.IMAGE: ['jpg', 'jpeg', 'png', 'gif', ],
    FFD.VIDEO: ['mp4', ],
    FFD.AUDIO: ['mp3', ],
    FFD.FILES: ['txt', 'doc', 'docx', ],
}


def check_files_formats(fname, ftype=None):
    """Проверяет валидность формата файла"""

    correct_ext = False
    ext = fname.split('.')[-1]
    if ftype:
        if ext in formats_files[ftype]:
            correct_ext = True
    else:
        for key in formats_files.keys():
            if ext in formats_files[key]:
                correct_ext = True
    return correct_ext
