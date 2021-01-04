class LoggerConfig:
    LOG_BASE_DIR = '/log/application/'
    LOG_FILES = {
        'error': os.path.join(LOG_BASE_DIR, 'error.log'),
        'info': os.path.join(LOG_BASE_DIR, 'info.log'),
    }
    # logging.basicConfig(
    #     format='[%(asctime)s] %(levelname)s pid:%(process)s tid:%(thread)d {%(funcName)s %(pathname)s:%(lineno)d} - %(message)s',
    #     level=logging.DEBUG,
    #     handlers=[
    #         logging.FileHandler("pelican.log"),
    #         logging.StreamHandler(),
    #     ],
    # )
    CONFIG = {
        'ERROR': {
            'logger_name': 'ERROR_LOG',
            'log_file': LOG_FILES.get("error"),
            'lever': 'DEBUG',

            'formatter': '%(asctime)s - %(levelname)s - %(funcName)s \n%(message)s',

            'backup_count': 7,
            'encoding': 'utf-8',
            'when': 'midnight',
            'interval': 1,
            'filemode': 'a',
        },
        'INFO': {
            'logger_name': 'info_log',
            'log_file': LOG_FILES.get("info"),
            'lever': 'DEBUG',

            'formatter': '%(asctime)s - %(levelname)s - %(funcName)s \n%(message)s',

            'backup_count': 7,
            'encoding': 'utf-8',
            'when': 'midnight',
            'interval': 1,
            'filemode': 'a',
        }
    }
