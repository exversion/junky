def check_for_missing_column(file_obj,delimiter=','):
    ind = 0
    for val in file_obj:
        if ind == 0:
            validated_length = len(val.split(delimiter))
            ind += 1
            continue
        if len(val.split(",")) < validated_length:
            return True
    return False
