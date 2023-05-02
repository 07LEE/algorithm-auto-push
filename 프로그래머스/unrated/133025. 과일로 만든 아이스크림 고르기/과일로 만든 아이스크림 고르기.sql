SELECT i.flavor
from first_half f, icecream_info i
where f.flavor = i.flavor
      and i.ingredient_type = 'fruit_based'
      and f.total_order >= 3000;