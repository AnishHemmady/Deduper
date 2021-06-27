from typing import Callable, Generator, Union, Tuple, KeysView, ValuesView


class Deduper:
    name = "Dedups list of dictionaries based on key criteria"

    @classmethod
    def async_dedup_data(cls, data: list, func: Callable, matched_data_req=False) -> Generator:

        uniq_set = set()
        uniq_set_add = uniq_set.add

        for element in data:
            field_val = func(element)
            if field_val not in uniq_set:
                uniq_set_add(field_val)
                yield (field_val, element) if matched_data_req else field_val

    @classmethod
    def sync_dedup_data(cls, data: list, func: Callable, matched_data_req=False) -> Union[Tuple[KeysView, ValuesView], KeysView]:
        uniq_map = {}

        for element in data:
            field_val = func(element)
            if field_val not in uniq_map:
                uniq_map[field_val] = element

        return (uniq_map.keys(), uniq_map.values()) if matched_data_req else uniq_map.keys()
