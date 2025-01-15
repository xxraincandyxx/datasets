# --- Experiment for Implementation of New Features ---
# ---

from pathlib import Path
import logging
import os

from src.datasets.arrow_dataset import Dataset


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(filename="EXP.log", mode="w", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def main():
    root_dir = Path(__file__).parent
    test_data_dir = os.path.join(root_dir, "test_data")
    logger.debug("test_data_dir: %s", test_data_dir)

    # dataset = Dataset.from_parquet()


if __name__ == "__main__":
    main()
