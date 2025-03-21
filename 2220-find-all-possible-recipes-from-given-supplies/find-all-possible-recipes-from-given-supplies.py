class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipe_map = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        memo = {}

        def dfs(recipe):
            if recipe in memo:
                return memo[recipe]
            if recipe not in recipe_map:
                return False
            memo[recipe] = False
            for ing in recipe_map[recipe]:
                if ing not in supply_set and not dfs(ing):
                    return False
            supply_set.add(recipe)
            memo[recipe] = True
            return True
        
        return [recipe for recipe in recipes if dfs(recipe)]
            
            