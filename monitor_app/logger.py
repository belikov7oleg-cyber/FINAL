import logging
import os

# ============================================================
# СОЗДАНИЕ ПАПКИ LOGS
# ============================================================

LOG_DIR = os.path.join(
    os.path.dirname(__file__),
    'logs'
)

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

# ============================================================
# ФАЙЛ ЛОГОВ
# ============================================================

LOG_FILE = os.path.join(
    LOG_DIR,
    'security_events.log'
)

# ============================================================
# НАСТРОЙКА LOGGER
# ============================================================

security_logger = logging.getLogger(
    'security_logger'
)

security_logger.setLevel(
    logging.INFO
)

# Защита от duplicate handlers
if not security_logger.handlers:

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding='utf-8'
    )

    formatter = logging.Formatter(
        '[%(asctime)s] '
        '[%(levelname)s] '
        '%(message)s'
    )

    file_handler.setFormatter(
        formatter
    )

    security_logger.addHandler(
        file_handler
    )

# ============================================================
# ФУНКЦИИ ЛОГИРОВАНИЯ
# ============================================================

def log_info(message):

    security_logger.info(message)


def log_warning(message):

    security_logger.warning(message)


def log_critical(message):

    security_logger.critical(message)