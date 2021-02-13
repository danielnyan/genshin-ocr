import json

# To be placed in an external file
def populate_inventory_indices(inventory_indices, inventory):
    for i in range(len(inventory)):
        inventory_indices[inventory[i]['item']] = i

def update_inventory(inventory, updater):
    # Should implement custom getters and setters in case
    # SEELIE save format changes
    inventory_indices = {}
    populate_inventory_indices(inventory_indices, inventory)
    
    for key, value in updater.items():
        index = inventory_indices.get(key, -1)
        if index == -1:
            if value != 0:
                template = item_templates[key]
                template["value"] = value
                inventory.append(template)
        else:
            if value != 0:
                inventory[index]["value"] = value
            else:
                del inventory[index]

def refresh_inventory(json_obj, inventory):
    json_obj["inventory"] = json.dumps(inventory)

def main():
    item_templates = json.loads(open("item-templates.json").read())
    json_obj = json.loads(open("seelie-backup.json").read())
    inventory = json.loads(json_obj["inventory"])

    # For testing
    update_inventory(inventory, {
        'everflame_seed' : 69,
        'prosperity' : 0
    })
    refresh_inventory(json_obj, inventory)

    with open("seelie-backup-output.json", "w") as f:
        f.write(json.dumps(json_obj))

main()

"""
item_templates = {}
for el in inventory:
    item_templates[el["item"]] = el
with open("item-templates.json", "w") as f:
    f.write(json.dumps(item_templates))
"""
