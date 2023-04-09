Feature: Hello world function
    A function that given a name it salutes you.

    Scenario: Query with a name
        Given A requet with the name "sample-name"
        When the request is received
        Then it should reply with a message containing "Hello, sample-name."
