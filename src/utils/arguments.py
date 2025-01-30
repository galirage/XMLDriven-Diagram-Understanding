import argparse


def get_args():
    """Get args to run script

    Returns
    -------
    args : NamedTuple
        args from argparse
    """
    parser = argparse.ArgumentParser()

    # --------------------------------------------------
    # scripts
    # --------------------------------------------------
    parser.add_argument(
        "--w_xml", action="store_true",
        help="use xml",
    )

    parser.add_argument(
        "--w_vision", action="store_true",
        help="use vlm",
    )

    args = parser.parse_args()

    return args

