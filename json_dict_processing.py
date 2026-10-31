def extract_nested_value(obj, keys):
    for key in keys:
        if not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj

def process_dictionary_with_config(dictionary, config):
    result = {}

    for field, rule in config.items():
        if isinstance(rule, tuple):
            keys, converter = rule
            value = extract_nested_value(dictionary, keys)

            if value is not None:
                value = converter(value)
        else:
            value = extract_nested_value(dictionary, rule)

        result[field] = value

    return result

def process_list_of_dicts_with_config(list_of_dicts, config):
    result = []

    if list_of_dicts is None:
        return result

    for dictionary in list_of_dicts:
        processed = process_dictionary_with_config(dictionary, config)
        result.append(processed)

    return result

def create_processor(config, list_processor=False):
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)
        return process_dictionary_with_config(data, config)

    return processor