import Option

def get_option_html(option: Option, currentStage: int) -> str:
    result= """
          <form action="" method="get"> 
                <input type="hidden" name="stage" value=\"""" + str(currentStage) + """\" />
                <input type="hidden" name="option" value=\"""" + str(option.getKey()) + """\" />
                <input type="submit" value=\"""" + option.getName() + """\" style="height:50px">
            </form>"""
    debug = False
    if debug:
        for outcome in option.getOutcomes():
            print(outcome.getLikelihood())
            result+= 'Potential Outcome: ' + outcome.getName() + '. Likelihood: ' + str(outcome.getLikelihood()) + '<br>'
    return result

def get_styles_html() -> str:
    return """
    <style>
    h2 {	Strong; 
	font-size:26px;
	margin-bottom:0;
	color: #000000;
    text-align: center;
    h3 { color: #000000;}
    p1 {
        text-align: center;
    }
    </style>
    """
