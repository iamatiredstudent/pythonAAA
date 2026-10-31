from operator import itemgetter
from statistics import mean, median

from dataset_helpers import group_by_attributes


def count_by_field(data, field):
    groups = group_by_attributes(data, [field])
    result = []

    for key, records in groups.items():
        result.append({
            field: key[0],
            "count": len(records),
        })

    return result


def top_n(data, field, n=5):
    sorted_data = sorted(data, key=itemgetter(field), reverse=True)
    return sorted_data[:n]


def calculate_statistics(data, field):
    values = []

    for record in data:
        value = record.get(field)

        if value is not None:
            values.append(value)

    if not values:
        return {
            "count": 0,
            "mean": None,
            "median": None,
            "max": None,
        }

    return {
        "count": len(values),
        "mean": round(mean(values), 2),
        "median": median(values),
        "max": max(values),
    }

def count_share(data, field, value):
    known_count = 0
    matching_count = 0

    for record in data:
        if record.get(field) is not None:
            known_count += 1

            if record[field] == value:
                matching_count += 1

    percent = None

    if known_count > 0:
        percent = round(matching_count / known_count * 100, 2)

    return {
        "count": matching_count,
        "percent": percent,
        "missing": len(data) - known_count,
    }