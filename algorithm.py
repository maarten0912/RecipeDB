import PySimpleGUI as sg
# Each place in the array denotes a possible theme in the recipe
weightedModel = [1.3,1.1,0.9] # place holder


##############      functions                                   #
#                                                                   #
#####################################################################

# calculates the score of a recipe based on the current weightedModel
# Recipe vector will be an array as long as the weightedModel with a 1 or a 0 in each place depending on if the theme of the place applies to the recipe
def calculateScore(recipeVector):
    score = 0
    for i in range(len(weightedModel)):
        # only change the score for the themes that matter
        if(recipeVector[i] != 0):
            # multiply the weighted model value for each theme in the recipe.
            score += (weightedModel[i] * recipeVector[i]) - 1
    return score    

#testArray = [0,1,0]
#print(calculateScore(testArray))


"""
The recipevector parameter should indicated which theme belong to the swiped recipe, 1 at the position
dedicated to the theme means that that them applie to the recipe
The swipe variable should be a boolean indicated whether the swipe was positive(True) or negative(False)
"""
def calculatetheme(recipevector, swipe):
    # loop through all the theme's in the swiped recipe
    for i in range(len(recipevector)):
        # only if the recipe has a certain theme action needs to be taken
        if recipevector[i] == 1:
            # if the swipe indicated a positive opinion the theme-score should be improved
            if swipe:
                weightedmodel[i] = weightedmodel[i] * positiveswipe
            # if the swipe indicated a negative opinion the theme-score should be decreased
            else:
                weightedmodel[i] = weightedmodel[i] * negativeswipe

weightedmodel = [1, 1, 1, 1, 1]
samplerecipe1 = [1, 0, 0, 1, 1]
samplerecipe2 = [0, 1, 1, 1, 0]
positiveswipe = 1.3
negativeswipe = 0.8

# print(weightedmodel)
# calculatetheme(samplerecipe1, True)
# print(weightedmodel)
# calculatetheme(samplerecipe2, False)
# print(weightedmodel)

#####################################################################
#                                                                   #
#                           Windows                                 #
#                                                                   #
#####################################################################

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()