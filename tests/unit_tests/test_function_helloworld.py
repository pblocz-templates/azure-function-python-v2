from typing import Callable

import pytest
from azure import functions as func

from functions.function_helloworld import test_function as trigger_function  # noqa F401

# ----
# Example of test building the test on the call
# ----


def test_request_with_name(
    make_req: Callable[..., func.HttpRequest],
    func_call: Callable[[func.HttpRequest], func.HttpResponse],
) -> None:
    name = "test-name"
    req = make_req(params={"name": name})
    response: func.HttpResponse = func_call(req)

    assert (
        response.get_body().decode()
        == f"Hello, {name}. This HTTP triggered function executed successfully."
    )


# ----
# Example of test using reusable fixture for the function calls
# ----


@pytest.fixture()
def template_call(
    make_req: Callable[..., func.HttpRequest],
    func_call: Callable[[func.HttpRequest], func.HttpResponse],
) -> Callable[..., func.HttpResponse]:
    def wrapper(**kwargs: str) -> func.HttpResponse:
        req = make_req(params=kwargs)
        outresp = func_call(req)

        return outresp

    return wrapper


def test_request_with_name_alt(template_call: Callable[..., func.HttpResponse]) -> None:
    name = "test-name"
    response = template_call(name=name)

    assert (
        response.get_body().decode()
        == f"Hello, {name}. This HTTP triggered function executed successfully."
    )


def test_request_without(template_call: Callable[..., func.HttpResponse]) -> None:
    response = template_call()

    assert response.get_body().decode() == (
        "This HTTP triggered function executed successfully."
        + "Pass a name in the query string or in the request body for a personalized response."
    )
