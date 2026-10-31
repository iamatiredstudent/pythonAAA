def count_missing(data):
    missing = {}

    # Собираем все поля, которые встречаются в записях.
    for record in data:
        for field in record:
            missing[field] = 0

    # Считаем пропуски каждого поля.
    for record in data:
        for field in missing:
            if record.get(field) in (None, "", []):
                missing[field] += 1

    return missing


def missing_share(data):
    counts = count_missing(data)
    shares = {}

    for field, count in counts.items():
        shares[field] = round(count / len(data), 4)

    return shares


def find_duplicate_ids(data):
    counts = {}

    for record in data:
        record_id = record["id"]
        counts[record_id] = counts.get(record_id, 0) + 1

    duplicates = {}

    for record_id, count in counts.items():
        if count > 1:
            duplicates[record_id] = count

    return duplicates


def find_id_gaps(data):
    ids = []

    for record in data:
        ids.append(record["id"])

    ids = sorted(set(ids))
    gaps = []

    for previous_id, current_id in zip(ids, ids[1:]):
        if current_id - previous_id > 1:
            gaps.append((previous_id, current_id))

    return gaps

def filter_by_value(data, field, value):
    result = []

    for record in data:
        if record.get(field) == value:
            result.append(record)

    return result


def group_by_attributes(data, attributes):
    groups = {}

    for record in data:
        key = []

        for attribute in attributes:
            key.append(record.get(attribute))

        key = tuple(key)

        if key not in groups:
            groups[key] = []

        groups[key].append(record)

    return groups