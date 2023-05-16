import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (Ingredient, Restriction)


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("Sanduba", "10")
    with pytest.raises(ValueError):
        Dish("Sanduba", -10)
    dish0 = Dish("Sanduba", 10.0)
    dish1 = Dish("Sanduba", 10.0)
    dish2 = Dish("Lasanha", 30.0)
    dish2.add_ingredient_dependency(Ingredient("massa de lasanha"), 10)
    # dish2.add_ingredient_dependency(Ingredient("queijo mussarela"), 5)

    assert dish0.name == "Sanduba"
    assert dish0.price == 10.0

    assert repr(dish0) == "Dish('Sanduba', R$10.00)"
    assert hash(dish0) == hash(dish1)
    assert hash(dish0) != hash(dish2)
    assert dish0.__eq__(dish1) is True
    assert dish0.__eq__(dish2) is False

    assert dish2.recipe.get(Ingredient("massa de lasanha")) == 10
    assert dish2.get_ingredients() == {Ingredient('massa de lasanha')}
    assert dish2.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN
    }
