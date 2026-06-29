import logging
from etl.config import LOGS_DIR

LOG_FILE = LOGS_DIR / "freshscan.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("FreshScanAI")