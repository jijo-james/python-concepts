"""
def binary_search_tree(tree: dict) -> bool:
    for key, value in tree:
        if not "left" and "right":
            continue
        if value > tree["left"["value"]] and value < tree["right"["value"]]:
            continue




node = {"value": 10, "left": {"value": 5}, "right": {"value": 15}}


a with 10k
b with 1m
    
"""

"""
customers
orders: cust_id(f)

select customers.name 
from customers left join orders 
on customers.cust_id = orders.cust_id 
where count(orders.cust_id) >= 10

"""


def is_valid_BST(node):
    def valid(node, min_val, max_val):
        if node is None:
            return True

        if min_val < node["value"] < max_val:
            return valid(node.get("left"), min_val, node["value"]) and valid(
                node.get("right"), node["value"], max_val
            )

        return False

    return valid(node, float("-inf"), float("inf"))


# Given node structure
node = {
    "value": 10,
    "left": {"value": 5, "left": {"value": 1}, "right": {"value": 6}},
    "right": {"value": 15},
}

# Check if it's a valid BST
result = is_valid_BST(node)
print("Is the given structure a valid BST?", result)
