# Import pandas
import pandas as pd
import matplotlib.pyplot as plt


# reading csv file 
df = pd.read_excel('Energygels.xlsx')


# Define categories with their associated keywords
flavor_categories = {
    'Citrus': ['lemon', 'lime', 'orange','citrus','shikuwasa','grapefruit','ao mikan'],
    'Berry': ['strawberry', 'raspberry', 'blueberry','blackcurrant','cherry','cassis','berry','strawberries','blueberries','berries'],
    'Tropical': ['mango', 'pineapple', 'tropical'],
    'Chocolate & Coffee': ['chocolate', 'mocha', 'coffee','cocoa','latte','espresso','cappucino','cold brew','machhiato'],
    'Nutty': ['peanut', 'hazelnut', 'almond','cashew'],
    'Fruit': ['apple','muscat','peach','rhubarb','grape','forest fruits','banana','fruit','green plum','watermelon','ume','kiwi','acai','pomegranate'],
    'Unflavoured': ['naked','unflavoured','neutral','nude','gel','original'],
    'Dessert': ['banoffee','tutti fruitti','birthday','campfire','vanilla','caramel','maple syrup','red bean', 'honey','cacao'],
    'Beverage-Inspired': ['cola','mojito','ramune','pear cider'],
}

flavor_categories_combined = {
    'Fruit': ['lemon', 'lime', 'orange','citrus','shikuwasa','grapefruit','ao mikan','strawberry', 'raspberry', 'blueberry','blackcurrant','cherry','cassis','berry','strawberries','blueberries','berries','mango', 'pineapple', 'tropical'],
    'Chocolate & Coffee': ['chocolate', 'mocha', 'coffee','cocoa','latte','espresso','cappucino','cold brew','machhiato'],
    'Nutty': ['peanut', 'hazelnut', 'almond','cashew'],
    'Fruit': ['apple','muscat','peach','rhubarb','grape','forest fruits','banana','fruit','green plum','watermelon','ume','kiwi','acai','pomegranate'],
    'Unflavoured': ['naked','unflavoured','neutral','nude','gel','original'],
    'Dessert': ['banoffee','tutti fruitti','birthday','campfire','vanilla','caramel','maple syrup'],
    'Beverage-Inspired': ['cola','mojito','ramune','pear cider'],
}


def categorize_flavor(flavor_name):
    if pd.isna(flavor_name):  # Check for NaN values
        return 'Unknown'  # Or any category you prefer for NaN values
    flavor_name = flavor_name.lower()  # Proceed with lowercasing
    for category, keywords in flavor_categories.items():
        if any(keyword in flavor_name for keyword in keywords):
            return category
    return 'Other'
    

# Apply the function to the DataFrame
df['Flavor Category'] = df['Flavours'].apply(categorize_flavor)

# View the categorized DataFrame
#print(df.columns)

# Count occurrences of each category
category_counts = df['Flavor Category'].value_counts()
#print(category_counts_two)
print(df.loc[df['Flavor Category'] == 'Unknown'])

nan_values = df[df['Flavours'].isna()]
print(nan_values)

brands = df['Brand'].value_counts()
print(brands)

# Calculate the average for each brand
#averages = df.groupby('Brand').agg({
#    'Calories': 'mean',
#    'Total Carbohydrates': 'mean',
#}).reset_index()

# Print the result
#print(averages)

carbs = df['Carb ratio'].value_counts()
print(carbs)

    
average_df = df.groupby('Name')[['Calories', 'Total Carbohydrates','Sodium','Caffeine']].mean().reset_index().dropna()
print(average_df)

flavour_cat = df.groupby('Flavor Category')[['Calories', 'Total Carbohydrates','Sodium','Caffeine']].mean().reset_index().dropna()
print(flavour_cat)

#gelcount = df['Country'].value_counts()
#print(gelcount)
print(category_counts)



category_counts.plot(kind='pie')
plt.show()


