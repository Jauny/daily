#!/usr/bin/env python

import dropbox_upload
import json
import time
import os

from dropbox_upload import MissingToken
from dropbox.exceptions import ApiError, AuthError

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(DIR_PATH, "log.json")
BACKUP_PATH = "/log.json"


def get_user_input(query):
    """Ask `query` to user and get input."""
    return raw_input(query + "\n")


def get_things(thing, i=3):
    """Asks user `i` times for `thing`."""
    things = []

    for i in range(i):
        input = get_user_input(
                    "What is the #{} {}?".format(i+1, thing))
        things.append(input)

    return things


def backup_to_dropbox():
    """Backup `file` to dropbox."""
    print "Backing up log to Dropbox..."""
    log_file = open(LOG_PATH)

    try:
        dropbox_upload.upload_file(log_file, BACKUP_PATH)
    except MissingToken:
        print "Couldn't find Dropbox token." \
              "Make sure you have added your token into a `config.yaml` file."
    except ApiError as e:
        print "An error occured during upload: " + e.user_message_text
    except AuthError as e:
        print "It seems like your Dropbox token is invalid."


def main(*args, **kwargs):
    """Run the program."""
    date = time.strftime("%Y-%m-%d")

    print ("Welcome to the daily writings.\n"
           "You'll be asked for 3 things you are grateful for and 3 ideas.\n")

    ideas = get_things("idea")
    grateful_things = get_things("grateful thing")

    daily_log = dict(
        date=date,
        ideas=ideas,
        grateful_things=grateful_things)

    log = open(LOG_PATH, 'a+')
    json.dump(daily_log, log)
    log.write("\n")
    log.close()

    backup_to_dropbox()


if __name__ == '__main__':
    main()
