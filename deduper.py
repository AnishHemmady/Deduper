from typing import Callable, Generator


class Deduper:
    name = "Dedups list of dictionaries based on key criteria"

    @classmethod
    def dedup_data(cls, data: list, func: Callable, matched_data_req=False) -> Generator:

        uniq_set = set()
        uniq_set_add = uniq_set.add

        for element in data:
            field_val = func(element)
            if field_val not in uniq_set:
                uniq_set_add(field_val)
                yield (field_val, element) if matched_data_req else field_val


