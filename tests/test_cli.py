from services_test import cli


def test_hello_world() -> None:
    input_msg = "hello world"
    actual = cli.hello_world(input_msg)
    expected = "HELLO WORLD"
    assert actual == expected
