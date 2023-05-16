import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.dishes_df = pd.read_csv(source_path).itertuples(index=False)
        self.create_dishes()

    def create_dishes(self):
        previous_dish = None
        dish = None
        for dish_name, price, ingredient, amount in self.dishes_df:
            if previous_dish is None:
                previous_dish = dish_name
            if dish_name != previous_dish:
                self.dishes.add(dish)
                previous_dish = dish_name
            dish = Dish(dish_name, float(price))
            dish.add_ingredient_dependency(Ingredient(ingredient), amount)
        self.dishes.add(dish)
