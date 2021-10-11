from flask import Flask
from flask import request

import labourstage
import HTML_Labour_Stage

app = Flask(__name__)


@app.route("/")
def index():
    option = request.args.get("option", "")
    previousStage = request.args.get("stage", "")
    if previousStage == None or previousStage == "":
        currentStage = -1
        options = options_from(currentStage)#options_from_start()

    else:
        previousStage = int(previousStage) #labourstage.calc_new_stage(lastStage, option)
        submittedOption = int(option)
        currentStage = roll_dice_for_next_stage(previousStage, submittedOption)
        options = options_from(currentStage)

    disabledBoolean = ""
    if (previousStage == "Birth!"):
        disabledBoolean = "disabled"

    stageName = get_stage_name(currentStage)

    return (
        get_style_html() + """<a href="/">Reset</a>
        <br>
        <br>
        <br>
        <h2>""" + stageName + "</h2>"
        + "<br><br>"
        + "<p1>Consider your options...</p1>"
        + options

        +"""<img src="static/resources/images/""" + get_stage_image(currentStage) + """" align="middle" />"""
    )

def get_stage_name(stage):
    return labourstage.get_stage_name(stage)

def get_stage_image(stage):
    return labourstage.get_image_name(stage)

def options_from(stage):
    """Seeing what comes next."""

    try:
        options = labourstage.get_options_from_stage(stage)
        result = "<br>"
        for option in options:
            result+= HTML_Labour_Stage.get_option_html(option, stage)

        return result
    except ValueError:
        return "invalid input"

def roll_dice_for_next_stage(stage, option):
    return labourstage.calc_new_stage(stage, option)[0]

def get_style_html() -> str:
    return HTML_Labour_Stage.get_styles_html()

#if __name__ == "__main__":
#    app.run(host='0.0.0.0',port="8400",debug=True)
    #app.run(host="127.0.0.1", port=8080, debug=True)