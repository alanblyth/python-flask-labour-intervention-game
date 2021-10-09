import labourstage

def test_get_options_from_stage_0():
    print('Hello World!')
    stage = 0
    options = labourstage.get_options_from_stage(stage)
    print(str(options))

def test_calc_new_stage():

    print(labourstage.calc_new_stage(0, 0))

def test_get_stage_name_for_stage_0():
    
    print(labourstage.get_stage_name(0))