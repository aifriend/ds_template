"""Data-processing stub that turns raw data into processed data."""
import logging
from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """Turn raw data from INPUT_FILEPATH into cleaned data in OUTPUT_FILEPATH."""
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Not used in this stub but often useful for finding various files.
    project_dir = Path(__file__).resolve().parents[2]

    # Find .env by walking up directories, then load its entries as
    # environment variables.
    load_dotenv(find_dotenv())

    main()
