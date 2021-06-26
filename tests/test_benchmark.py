dedup_me = [{"name": "anish", "val": 12}, {"name": "rahul", "val": 17}, {"name": "anish", "val": 12},
            {"name": "anish", "val": 12}, {"name": "rahul", "val": 17}, {"name": "rahulp", "val": 19}]

big_list = [random.choice(dedup_me) for _ in range(0, 1000000)]
dedup_gen = Deduper.dedup_data(big_list, lambda x: (x.get("name")))
res = [r for r in dedup_gen]
