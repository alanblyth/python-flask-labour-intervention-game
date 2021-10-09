from Option import Option

def test_setupOption():
    name = 'A Sample Option'
    option = Option(name)
    
    assert option.getName() == name