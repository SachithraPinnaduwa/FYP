import re

def extract_file_info(input_string):
    match = re.match(r'<reponame>(?P<author_username>[\w-]+)/(?P<repository_name>[\w-]+)<filename>(?P<file_name>.+)', input_string)
    if match:
        return {
            'repository_name': match.group('repository_name'),
            'author_username': match.group('author_username'),
            'file_name': match.group('file_name')
        }
    else:
        return None