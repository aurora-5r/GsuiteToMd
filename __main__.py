# -*- coding: utf-8 -*-
import getopt
import logging
import sys
from gstomd.settings import LoadSettingsFile
from gstomd.settings import SettingsError
from gstomd.settings import InvalidConfigError
from gstomd.settings import SetupLogging
from gstomd.corpus import Corpus


DEFAULT_SETTINGS = {
    'pydrive_settings': 'pydrive_settings.yaml',
    'dest_folder': './data',
    'root_folder_id': '',
    'root_folder_name': '',
    'drive_id': '',
    'collections': []
}


def main():
    SetupLogging()

    logger = logging.getLogger()
    logger.debug("Start")

    try:
        opts, _ = getopt.getopt(sys.argv[1:], '-c', [
            'config=',
        ])
    except getopt.GetoptError:
        sys.exit(2)
    settings_file = 'settings.yaml'
    for opt, arg in opts:

        if opt in ('-c', '--config'):
            settings_file = arg

    logging.debug("configfile : %s", settings_file)

    try:
        settings = LoadSettingsFile(settings_file)
    except SettingsError as err:
        logging.debug("incorrect config file : %s", err)
        settings = DEFAULT_SETTINGS
    else:
        if settings is None:
            settings = DEFAULT_SETTINGS

    corpus = Corpus(settings_file)
    logger.debug("Corpus Created")

    corpus.fetch()
    logger.debug("Corpus Fetched")

    for col in corpus.collections:
        logger.info(col.root_folder)
        corpus.to_disk()


if __name__ == "__main__":
    # execute only if run as a script
    main()
