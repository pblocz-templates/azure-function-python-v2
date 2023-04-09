from typing import Callable

from azure import functions as func
from pytest_bdd import given, parsers, scenarios, then, when

from functions.function_helloworld import (  # noqa: F401
    test_function as trigger_function,
)

# You can run a command to autogenerate missing steps
#     pytest --generate-missing --feature tests/bdd/features/ tests/bdd/steps_defs/
scenarios("../features/helloworld.feature")


@given(parsers.parse('A requet with the name "{name}"'), target_fixture="req")
def given_name(
    name: str,
    make_req: Callable[..., func.HttpRequest],
) -> func.HttpRequest:
    """A requet with the name "sample-name"."""

    return make_req(params={"name": name})


@given("A requet without any parameter", target_fixture="req")
def given_no_name(
    make_req: Callable[..., func.HttpRequest],
) -> func.HttpRequest:
    """A requet without any parameter."""

    return make_req(params={})


@when("the request is received", target_fixture="resp")
def when_function_call(
    req: func.HttpRequest,
    func_call: Callable[[func.HttpRequest], func.HttpResponse],
) -> func.HttpResponse:
    """the request is received."""

    return func_call(req)


@then(parsers.parse('it should reply with a message containing "{response_text}"'))
def should_contain_hello(response_text: str, resp: func.HttpRequest) -> None:
    """it should reply with a message containing "Hello, sample-name."."""

    assert response_text in resp.get_body().decode()
