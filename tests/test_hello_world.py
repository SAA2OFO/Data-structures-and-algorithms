# pylint: disable=missing-module-docstring

from src.basics.hello_world import main

def test_hello_world(): # pylint: disable=missing-function-docstring
    assert main() == "Hello, world!"
