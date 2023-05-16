from src.models.ingredient import (
    Ingredient,
    Restriction
  )  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredients0 = Ingredient("manteiga")
    ingredients1 = Ingredient("manteiga")
    ingredients2 = Ingredient("bacon")

    assert ingredients0.name == "manteiga"
    assert ingredients0.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert hash(ingredients0) == hash(ingredients1)
    assert hash(ingredients0 != ingredients2)
    assert repr(ingredients0) == "Ingredient('manteiga')"
    assert ingredients0.__eq__(ingredients1) is True
    assert ingredients0.__eq__(ingredients2) is False
