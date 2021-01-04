import json

import recipesdatabase.dbhelper as db

positiveswipe = 1.3
negativeswipe = 0.8

def calculateingredientscores(ids, swipes, count):
    ingredientslist = []
    ingredientsvalues = []
    result = []
    values = []
    iterations = max(count, len(ids))
    for i in ids:
        ingredients = json.loads(db.get_recipe(i))["simple_ingredients"]
        for j in ingredients:
            if j not in ingredientslist:
                ingredientslist.append(j)
                ingredientsvalues.append(1)
            index = ingredientslist.index(j)
            if swipes[ids.index(i)] == "yes":
                ingredientsvalues[index] = ingredientsvalues[index] * positiveswipe
            else:
                ingredientsvalues[index] = ingredientsvalues[index] * negativeswipe

    for i in range(iterations):
        index = ingredientsvalues.index(max(ingredientsvalues))
        result.append(ingredientslist[index])
        values.append(ingredientsvalues[index])
        ingredientslist.pop(index)
        ingredientsvalues.pop(index)

    return result, values


def getbestrecipes(ids, swipes):
    bestingredients, values = calculateingredientscores(ids, swipes, len(ids))
    matches = db.best_matches(ingredient_list=bestingredients)

    id_list = []
    scores = []

    for match in matches:
        score = 0
        ingredients = match[1].replace("[","").replace("\"","").split(", ")
        for ingredient in ingredients:
            if ingredient in bestingredients:
                index = bestingredients.index(ingredient)
                score += values[index]-1
        scores.append(score)
        id_list.append(match[0])

    recipes = []

    for i in range(len(scores)):
        index = scores.index(max(scores))
        recipes.append(json.loads(db.get_recipe(id_list[index])))
        scores.pop(index)
        id_list.pop(index)

    return recipes
