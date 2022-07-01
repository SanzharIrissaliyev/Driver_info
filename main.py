from data import datas

orders = datas["orders"]
# "123123123": {
#         "order_count": 0,
#         "fio": "asdasd",
#         "id": "asdasd"
#     }

drivers = {

}

categories = set()

for order in orders:
    dr_id = order["driver_profile"].get("id", "")
    dr_name = order["driver_profile"]["name"]
    mileage = order.get("mileage", "0")

    if dr_id not in drivers:
        drivers[dr_id] = {
                "order_count": 0,
                "fio": dr_name,
                "id": dr_id,
                "all_traffic": 0,
                "all_order_count": 0
            }

    mileage = int(float(mileage))
    drivers[dr_id]["all_order_count"] += 1
    drivers[dr_id]["all_traffic"] += mileage
    categories.add(order.get("category", ""))

    if mileage > 2000:
        drivers[dr_id]["order_count"] += 1


result = 'FIO\t > 0 km \t kms \t > 2km \n'
for d in drivers:
    dr = drivers[d]
    result += f'{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["order_count"]}\n'

print(result)

print(categories)