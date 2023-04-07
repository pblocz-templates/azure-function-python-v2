from azure import functions as func

from functions import blueprint

app = func.FunctionApp()

app.register_functions(blueprint)
