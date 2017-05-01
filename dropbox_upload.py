"""
Dropbox module for backup.
"""

import config
import dropbox
from dropbox.files import WriteMode


def get_dropbox_client(token):
    """Return a dropbox client for `token`.

    Raise `AuthError` if token is invalid.
    """
    dbx = dropbox.Dropbox(token)

    dbx.users_get_current_account()
    return dbx


def upload_file(source_file, dest_path):
    """Overwrites `source` onto `dest`.

    Raise `ApiError` if upload issue.
    """
    dbx = get_dropbox_client(config.get("token"))
    dbx.files_upload(
        source_file.read(), dest_path, mode=WriteMode('overwrite', None))
