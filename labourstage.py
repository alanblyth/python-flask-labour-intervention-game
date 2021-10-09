import yaml
from Option import Option
from Outcome import Outcome

#Open Stages
laboure_stages_file = 'LabourStages.yml'
stream = open(laboure_stages_file, "r")
stages_file = yaml.load(stream, Loader=yaml.FullLoader)
stream.close()

def get_stage_name(stageKey) -> str:

    stages = stages_file['Stages']
    stage = stages[stageKey]
    return stage['name']

def get_options_from_stage(stageKey):

    stages = stages_file['Stages']
    stage = stages[stageKey]

    resultOptions = []
    
    for option in stage['options']:

        newOption = Option(option['name'])
        newOption.setKey(option['key'])
        resultOptions.append(newOption)

        resultOutcomes = []

        for outcome in option['outcomes']:
            
            newOutcome = Outcome(outcome['name'])
            newOutcome.setLikelihood(outcome['likelihood'])
            newOutcome.setGoto(outcome['goto'])
            newOutcome.setKey = outcome['key']
            resultOutcomes.append(newOutcome)
        
        newOption.setOutcomes(resultOutcomes)

    return resultOptions

def calc_new_stage(stage, givenOption) -> int:

    options = get_options_from_stage(stage)
    for option in options:
        print(option.getKey())
        if option.getKey() == givenOption:
            selectionOption = option
    
    list_of_candidates = []
    number_of_items_to_pick = 1
    probability_distribution = []
    for outcome in selectionOption.getOutcomes():
        list_of_candidates.append(outcome.getGoto())
        probability_distribution.append(outcome.getLikelihood())

    from numpy.random import choice
    nextStage = choice(list_of_candidates, number_of_items_to_pick,p=probability_distribution)
    return nextStage

def get_image_name(stageKey: int) -> str:

    stages = stages_file['Stages']
    stage = stages[stageKey]
    print('Getting image for stage: ' + str(stageKey))
    return stage['image']