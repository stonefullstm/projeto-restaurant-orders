import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.dishes_df = pd.read_csv(source_path)
        self.create_dishes()

    def create_dishes(self):
        previous_dish = self.dishes_df["dish"].loc[0]
        dish = Dish(
            self.dishes_df["dish"].loc[0],
            float(self.dishes_df["price"].loc[0])
            )
        for dish_name, price, ingredient, amount in self.dishes_df.itertuples(
                index=False):
            if dish_name != previous_dish:
                self.dishes.add(dish)
                previous_dish = dish_name
                dish = Dish(dish_name, float(price))
            dish.add_ingredient_dependency(Ingredient(ingredient), amount)
        self.dishes.add(dish)
