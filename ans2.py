def get_file_type(extension_type_string, filenames):
    extension_type_map = {}
    for pair in extension_type_string.split(";"):
        extension, file_type = pair.split(":")
        extension_type_map[extension.lower()] = file_type

    file_types = {}
    for filename in filenames:
        dot_index = filename.rfind(".")
        if dot_index != -1:
            extension = filename[dot_index + 1:].lower()
            file_types[filename] = extension_type_map.get(extension, "unknown")
        else:
            file_types[filename] = "unknown"

    return file_types


if __name__ == "__main__":
    extension_type_string = "xls:spreadsheet;xlsx:spreadsheet;jpg:image"
    filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

    file_types = get_file_type(extension_type_string, filenames)

    print(file_types)

