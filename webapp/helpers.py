
import os
from hashlib import md5


def versioned_static(filename):
    """
    Template function for generating URLs to static assets:
    Given the path for a static file, output a url path
    with a hex hash as a query string for versioning
    """

    filepath = os.path.join("static", filename)
    url = filepath

    if not os.path.isfile(filepath):
        # Could not find static file
        return url

    # Use MD5 as we care about speed a lot
    # and not security in this case
    file_hash = md5()
    with open(filepath, "rb") as file_contents:
        for chunk in iter(lambda: file_contents.read(4096), b""):
            file_hash.update(chunk)

    return url + "?v=" + file_hash.hexdigest()[:7]
