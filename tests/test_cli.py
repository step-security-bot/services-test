from services_test import cli


def test_hello_world():
    input_msg = "hello world"
    result = cli.hello_world(input_msg)
    output_msg = "HELLO WORLD"
    assert result == output_msg
