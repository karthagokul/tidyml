from tidyml.parser import parse

def test_dummy():
    assert parse("key = value") == {"status": "Parser not implemented yet"}
