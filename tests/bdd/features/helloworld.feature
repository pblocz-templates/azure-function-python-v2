Feature: Hello world function
    A function that given a name it salutes you.

    Scenario: Query with a name
        Given A requet with the name "sample-name"
        When the request is received
        Then it should reply with a message containing "Hello, sample-name."

    Scenario: Query without a name parameter
        Given A requet without any parameter
        When the request is received
        Then it should reply with a message containing "Pass a name in the query string or in the request body"
