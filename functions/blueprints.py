from azure import functions as func

blueprint = func.Blueprint()


from .function_helloworld import test_function  # noqa: F401,E402
