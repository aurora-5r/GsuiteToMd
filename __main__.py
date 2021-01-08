# -*- coding: utf-8 -*-
import getopt
import logging
import sys
from gstomd.settings import SetupLogging
from gstomd.corpus import GsuiteToMd


def main():
    SetupLogging()

    logger = logging.getLogger()
    logger.debug("Start")

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "-c", ["config="])
    except getopt.GetoptError:
        sys.exit(2)
    settings_file = "settings.yaml"
    for opt, arg in opts:

        if opt in ("-c", "--config"):
            settings_file = arg
        if opt in ("-f", "--folder"):
            folder_id = arg

    logging.debug("configfile : %s", settings_file)

    gstomd = GsuiteToMd(settings_file=settings_file)
    logger.debug("gsuiteTomd  Created")

    gstomd.Folder(
        folder_id=folder_id,
        dest_folder="doc_extracted",
        root_folder_name="newposts",
    )


if __name__ == "__main__":
    # execute only if run as a script
    main()
