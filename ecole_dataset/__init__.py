import os
import logging
from pathlib import Path
from cached_path import set_cache_dir

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("ecole_dataset")

CACHE_DIR = os.environ.get(
    "DATASETS_CACHE",
    (Path.home() / ".cache" / "ecole_dataset_cache").as_posix(),
)
logger.info(f"Using cache dir: {CACHE_DIR}\n")
logger.info("To change this, set the environment variable DATASETS_CACHE\n")
os.environ["HF_DATASETS_CACHE"] = (Path(CACHE_DIR) / "hf_datasets").as_posix()
set_cache_dir(Path(CACHE_DIR) / "cached_path")

from . import datasets
from . import registry
