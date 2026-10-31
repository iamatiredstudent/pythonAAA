
def add_attribute(data, field, function):
    result = []

    for record in data:
        new_record = record.copy()
        new_record[field] = function(record)
        result.append(new_record)

    return result