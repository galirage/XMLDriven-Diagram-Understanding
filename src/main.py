from utils import arguments
from utils.log_init import logger
from scripts.w_xml import run_w_xml
from scripts.w_img import run_w_img


def main():
    # logger
    logger.info("script start!")

    # arguments --> config
    args = arguments.get_args()

    # run script
    if args.w_xml:
        run_w_xml()
    elif args.w_img:
        run_w_img()
    else:
        logger.warning('You should specify one script such as `--w_xml` or `--w_img`.')


if __name__ == "__main__":
    main()
