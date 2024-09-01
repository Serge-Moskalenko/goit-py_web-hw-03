import os
import shutil
import sys
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


def copy_file(file_path, target_dir):

    file = file_path.suffix[1:]
    if not file:
        return

    target_path = target_dir / file
    target_path.mkdir(parents=True, exist_ok=True)

    shutil.copy(file_path, target_path / file_path.name)
    logger.debug(f"Copied: {file_path} -> {target_path / file_path.name}")


def sorting_directory(source_dir, target_dir):

    with ThreadPoolExecutor() as executor:
        threads = []
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file
                threads.append(executor.submit(copy_file, file_path, target_dir))

        for thread in as_completed(threads):
            thread.result()


if __name__ == "__main__":

    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    if len(sys.argv) < 2:
        logging.debug("Need to use: python task1.py <source_dir> [<target_dir>]")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir.is_dir():
        logger.debug(f"Not found '{source_dir}' or not a directory.")
        sys.exit(1)

    sorting_directory(source_dir, target_dir)
    logger.debug("Sorting finished.")
