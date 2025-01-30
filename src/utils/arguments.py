import argparse
import yaml

from easydict import EasyDict as edict


def get_args():
    """Get args which has path to yaml.

    Returns
    -------
    args : NamedTuple
        args from argparse to load yaml file.
    """
    parser = argparse.ArgumentParser()

    # --------------------------------------------------
    # configurations
    # --------------------------------------------------

    parser.add_argument(
        "--yaml_path", type=str, default=None, required=True,
        help="yaml file path",
    )

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


def load_edict_config(args):
    """Load config in yaml specified in args.yaml_path.

    Parameters
    ----------
    args : NamedTuple
        MUST have args.yaml_path.

    Returns
    -------
    config : EasyDict
        EasyDict which has all parameters written in yaml file.
    """
    with open(args.yaml_path, "r") as fp:
        config = yaml.load(fp, Loader=yaml.SafeLoader)

    config = edict(config)

    return config
