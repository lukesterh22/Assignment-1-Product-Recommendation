
from product_data import products


# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_tags= set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products: 
    converted_products.append({
        "name":product ["name"],
        "tags": set(product["tags"])
    })



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    matches = product_tags.intersection(customer_tags)
    return len(matches)
    
'''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
'''
pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches

def recommend_products(products, customer_tags):
    recommendations = []
    for product in products: 
        product_set = set(product["tags"])
        match_count = count_matches(product['tags'], customer_tags)
        if match_count > 0:
            recommendations.append({"name": product["name"], "matches": match_count})
    return recommendations
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    pass



# TODO: Step 7 - Call your function and print the results
recommended = recommend_products(converted_products, customer_tags)
print("\nRecommended products based on your preferences:")
for item in recommended:
    print(item['name'], "- Matches:", item['matches'])



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
'''I used multiple core operations to be able to match user recommendations to products. One major operations were loops. 
I used them in step 4 and 5 to be able to go through the list of products and through the user input to get their preference. 
I also used the sets and intersection functions. The set function allowed me to convert a list to a set so no duplicates were involved. 
The intersection allowed me to count the number of tags that matched. I used the if function in step 6 to only display the product if it had one or more matches.
'''
# 2. How might this code change if you had 1000+ products?
"""This code might be different because if a user typed in multiple matches then a long list of their matches would pop up in a non numerical order. 
I would try and have a function that sorts the list from most matches to least, so the product that best matches their search pops up.
Another way this would change with more products is making the it operate slower. With the for loops, it will take a longer to loop through all of the products and preferences. 
Although I do not know how to do it with a for loop, that is something I will look into.
"""