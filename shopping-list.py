# determines if a shopping list item is eligible for free shipping

# set the variables
def main():
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1
    eligible_items = "orange banana carrot"
    item_price = 2 # USD

    # Calculate subtotal
    subtotal = item_price * quantity

    # print subtotal
    print(f"item name: {item_name}, subtotal: {subtotal}")

    # initialize discount to 0
    discount = 0

    # check if item_name is in eligible_items string, is it eligible for discount
    if item_name in eligible_items:
        discount = subtotal * discount_rate

    #print discount
    print(f"discount: {discount}")

    # check f discount is applied
    was_discount_applied = discount > 0

    print(f"Was the discount applied? {was_discount_applied}")

    # check if free shipping should be applied, quantity > 5, item_name = 'banana'
    free_shipping = quantity >= 5 and item_name == 'banana'

    print(f"Is this item eligible for free shipping? {free_shipping}")


if __name__ == '__main__':
    main()