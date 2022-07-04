from data import datas
from datetime import datetime
import datetime as d

from dateutil.parser import parse
import pytz




orders = datas["orders"]
# "123123123": {
#         "order_count": 0,
#         "fio": "asdasd",
#         "id": "asdasd"
#     }

drivers = {}
categories = {}
type = {}
status = {}

for order in orders:
    dr_id = order["driver_profile"].get("id", "")
    dr_name = order["driver_profile"]["name"]
    mileage = order.get("mileage", "0")
    dr_category = order.get("category", "")
    dr_car = order["car"].get("brand_model", "")
    dr_type = order["type"].get("name", "")
    cat_name = order.get("category", "")
    dr_status = order.get("status", "")
    created_at = order.get("created_at", "")
    booked_at = order.get("booked_at", "")
    # new_data = order.get("new_data", "")

    if dr_id not in drivers:
        drivers[dr_id] = {
                "order_count": 0,
                "fio": dr_name,
                "id": dr_id,
                "all_traffic": 0,
                "all_order_count": 0,
                "category": {},
                "model": dr_car,
                "type": {},
                "status": {},
                "created_at": created_at,
                "booked_at": booked_at,
                # "new_data": new_data,
            }
    dt = parse(created_at)
    dt1 = parse(booked_at)
    difference = dt1 - dt
    difference = ""
    print(dt.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))
    print(dt1.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))
    print("##########")
    dt2 = parse(difference)

    print(dt2.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))




    created_at1 = d.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f%z')
    booked_at1 = d.datetime.strptime(booked_at, '%Y-%m-%dT%H:%M:%S.%f%z')
    # difference = booked_at1 - created_at1

    if dr_category not in drivers[dr_id]["category"]:
        drivers[dr_id]["category"][dr_category] = 0
    drivers[dr_id]["category"][dr_category] += 1

    mileage = int(float(mileage))
    drivers[dr_id]["all_order_count"] += 1
    drivers[dr_id]["all_traffic"] += mileage
    # categories.add(order.get("category", ""))

    if dr_type not in drivers[dr_id]["type"]:
        drivers[dr_id]["type"][dr_type] = 0
    drivers[dr_id]["type"][dr_type] += 1

    if dr_status not in drivers[dr_id]["status"]:
        drivers[dr_id]["status"][dr_status] = 0
    drivers[dr_id]["status"][dr_status] += 1

    cat_count = 0
    if cat_name not in categories:
        categories[cat_name] = {
            "cat_name": cat_name,
            "count": 0
        }
    categories[cat_name]["count"] += 1

    if mileage > 2000:
        drivers[dr_id]["order_count"] += 1

#Obshiy
result = 'FIO\t > 0 km \t kms \t > 2km \n'
for d in drivers:
    dr = drivers[d]
    result += f'{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["order_count"]}\t{dr["model"]}\n'
#print(result)

#Type of taxi
type_result = 'FIO\t > 0 km \t kms \t > 2km \n'
for d in drivers:
    dr = drivers[d]
    type_result += f'{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["type"]}\n'
#print(type_result)

status_result = 'FIO\t > 0 km \t kms \t > 2km \n'
for d in drivers:
    dr = drivers[d]
    status_result += f'{dr["fio"]}\t{dr["all_order_count"]}\t{dr["all_traffic"]}\t{dr["status"]}\t{dr["created_at"]}\t{dr["booked_at"]}\n'
# print(status_result)


#Kategoriya soni
category_result = 'NAME\t COUNT\n'
for t in categories:
    dt = categories[t]
    category_result += f'{dt["cat_name"]}\t {dt["count"]}\n'
#print(category_result)

#Voditel i kategoriya
driver_result = 'FIO\t caategory\t count\n'
for d in drivers:
    dr = drivers[d]
    driver_result += f'{dr["fio"]}\t{dr["category"]}\n'

#print(driver_result)