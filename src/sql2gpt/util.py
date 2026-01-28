from urllib.parse import urlparse, urlsplit


def get_db_type(database_url):
    # Parse the URL
    parsed_url = urlparse(database_url)

    # Extract and return the database type (scheme)
    return parsed_url.scheme


def is_uri(string):
    # Split the string into URL components
    parsed_url = urlsplit(string)

    # Check if the URL has a valid scheme and netloc (network location)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)
