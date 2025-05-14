from dataclasses import dataclass, field
from typing import List


@dataclass
class FoodRatings:
    def __init__(self):
        self.foods: [] = field(default_factory=list)
        self.ratings: {} = field(default_factory=dict)

    def get_ratings(self):
       for food in self.foods:
           while True:
               try:
                   rating = float(input(f"enter rating for {food}:"))
                   if 1 <= rating <= 5:
                       if food not in self.ratings:
                           self.ratings[food] = [rating]
                       else:
                           self.ratings[food].append(rating)
                   else:
                       print(f"rating is between 1 and 5")
               except ValueError as ve:
                   print(ve.with_traceback())
                   raise ve

    def get_highest_rating(self):
        max_rating = 0
        max_food = ""
        for food, rating in self.ratings.items():
            if max_rating < max(rating):
                max_food = food
                max_rating = max(rating)
        return max_food, max_rating
    



