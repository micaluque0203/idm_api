

def read_file(file_path, query_format=None):
    with open(file_path, 'r', encoding='utf-8') as info:
        query = "".join(info.readlines())
    if query_format is not None:
        query = query.format(iso_code=query_format)
    return query
