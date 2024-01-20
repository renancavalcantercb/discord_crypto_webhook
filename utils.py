import os

TMP_FOLDER = "tmp"


def ensure_tmp_folder_exists():
    if not os.path.exists(TMP_FOLDER):
        os.makedirs(TMP_FOLDER)
    _clean_TMP_FOLDER()


def _clean_TMP_FOLDER():
    for file in os.listdir(TMP_FOLDER):
        file_path = os.path.join(TMP_FOLDER, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def convert_datetime_to_string(datetime):
    datetime = datetime.strftime("%H:%M:%S %d/%m/%Y")
    return datetime
