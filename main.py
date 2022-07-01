from data2 import datas


orders = datas["orders"]
# "123123123": {
#         "order_count": 0,
#         "fio": "asdasd",
#         "id": "asdasd"
#     }

drivers = {

}

categories = {}

for order in orders:
    dr_id = order["driver_profile"].get("id", "")
    dr_name = order["driver_profile"]["name"]
    mileage = order.get("mileage", "0")
    dr_category = order.get("category", "")

    if dr_id not in drivers:
        drivers[dr_id] = {
                "order_count": 0,
                "fio": dr_name,
                "id": dr_id,
                "all_traffic": 0,
                "all_order_count": 0,
                "category": {}
            }
    if dr_category not in drivers[dr_id]["category"]:
        drivers[dr_id]["category"][dr_category] = 0
    drivers[dr_id]["category"][dr_category] += 1

    mileage = int(float(mileage))
    drivers[dr_id]["all_order_count"] += 1
    drivers[dr_id]["all_traffic"] += mileage
    # categories.add(order.get("category", ""))
    cat_name = order.get("category", "")
    cat_count = 0
    if cat_name not in categories:
        categories[cat_name] = {
            "cat_name": cat_name,
            "count": 0
        }
    categories[cat_name]["count"] += 1

    if mileage > 2000:
        drivers[dr_id]["order_count"] += 1


result = 'FIO\t > 0 km \t kms \t > 2km \n'
for d in drivers:
    dr = drivers[d]
    result += f'{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["order_count"]}\n'

print(result)

category_result = 'NAME\t COUNT\n'
for t in categories:
    dt = categories[t]
    category_result += f'{dt["cat_name"]}\t {dt["count"]}\n'
print(category_result)

driver_result = 'FIO\t caategory\t count\n'
for d in drivers:
    dr = drivers[d]
    driver_result += f'{dr["fio"]}\t{dr["category"]}\n'

print(driver_result)