import random
import uuid
from datetime import datetime

n_users = 500
n_records = 1000000

fn = open("first_names.txt","r")
ln = open("last_names.txt","r")
first_names = []
last_names = []
for line in fn:
    first_names.append(line[:-1])
for line in ln:
    last_names.append(line[:-1])


def get_users(n):
    users = []
    for i in range(n):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        id = uuid.uuid4().hex
        users.append({"name":"{0} {1}".format(first_name, last_name), "id":id})
    return users

users = get_users(n_users)
items = {"Weapons":["Arrow","Bow","Bullet","AK47","Sword","Dagger","Mace"],
         "Clothing":["Jumper","Hoodie","Jeans","T-Shirt","Shorts","Skirt","Blazer","Dress","Trousers"],
         "Furniture":["Table","Chair","Sofa","Bed","Television","Lamp"],
         "Tech":["Television","Games Console","HiFi","Laptop","Computer"]}
categories = items.keys()
colours = ["Red","Yellow","Blue","Green","Orange","Black"]
materials = ["Wood","Iron","Steel","Tin","Wool","Titanium","Plastic","Nylon","Denim"]
def get_material():
    colour = random.choice(colours)
    material = random.choice(materials)
    return "{0} {1}".format(colour, material)
start_time = 1498867200
end_time = 1500508800
timeformat = "%Y-%m-%d %H:%M:%S"

def get_line():
    keyid = uuid.uuid4().hex
    region = "Europe"
    receive_time = datetime.fromtimestamp(random.randint(start_time, end_time)).strftime(timeformat)
    purchaser = random.choice(users)
    purchaser_id = purchaser["id"]
    purchaser_name = purchaser["name"]
    category = random.choice(categories)
    item_name = random.choice(items[category])
    primary_material = get_material()
    secondary_material, tertiary_material, quaternary_material = "","",""
    if random.randint(0,5) > 2:
        secondary_material = get_material()
        if random.randint(0, 5) > 4:
            tertiary_material = get_material()
            if random.randint(0,10) > 9:
                quaternary_material = get_material()
    quantity_purchased = random.randint(1, 20)
    cost = random.randint(1, 60000)/100.0
    total_spent = quantity_purchased * cost
    return ",".join([keyid, region, receive_time, purchaser_id, purchaser_name, category, item_name, primary_material, secondary_material, tertiary_material, quaternary_material, str(quantity_purchased), str(total_spent)]) + "\n"

with open("data.csv","w") as file:
    for i in range(n_records):
        file.write(get_line())