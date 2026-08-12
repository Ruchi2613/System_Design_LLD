'''2. Each type of coffee should have a specific price and recipe (ingredients and their quantities).'''

from coffe_type_enum import CoffeeBean, CoffeeMilk, CoffeeSugar
from abc import ABC, abstractmethod


class CoffeeRecipe(ABC):
    @abstractmethod
    def prepare_ingredients(self,milk: CoffeeMilk, sugar: CoffeeSugar, bean: CoffeeBean):
        pass
    @abstractmethod
    def making_coffee(self):
        print("Making coffee...")
    @abstractmethod
    def serve_coffee(self):
        print("Coffee is ready!")


class EspressoRecipe(CoffeeRecipe):
    def prepare_ingredients(self, milk, sugar, bean):
        return super().prepare_ingredients(milk, sugar, bean)

    def making_coffee(self):
        print("Making espresso...")
    def serve_coffee(self):
        print("Espresso is ready!")


class CappuccinoRecipe(CoffeeRecipe):
    def prepare_ingredients(self, milk, sugar, bean):
        return super().prepare_ingredients(milk, sugar, bean)

    def making_coffee(self):
        print("Making cappuccino...")
    def serve_coffee(self):
        print("Cappuccino is ready!")


class LatteRecipe(CoffeeRecipe):
    def prepare_ingredients(self, milk, sugar, bean):
        return super().prepare_ingredients(milk, sugar, bean)

    def making_coffee(self):
        print("Making latte...")
    def serve_coffee(self):
        print("Latte is ready!")    




        