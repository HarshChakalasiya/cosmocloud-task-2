import sys
import loguru

logger = loguru.logger
logger.remove()
logger.add(sys.stdout, format="<red>{time}</red> | {extra[request_id]} | <level>{level}</level> | <green>{name} {function} L:{line}</green> {message} ", level="DEBUG")