from dbrlint.matchtypes import InputRequired

def test_inputRequired_literal():

    data = {"test": "something", "test_int": 10}
    ir1 = InputRequired("test", "?")
    ir2 = InputRequired("test_int", "?")
    assert(ir1.evaluate(data))
    assert(ir2.evaluate(data))

def test_inputRequired_nested_literal():

    data = {"test": {"subtest":"something"}, "test2":{"test_int": 10}}
    ir1 = InputRequired("test.subtest", "?")
    ir2 = InputRequired("test2.test_int", "?")
    assert(ir1.evaluate(data))
    assert(ir2.evaluate(data))


def test_inputRequired_array():

    data = {"test": ["something"], "test_int": 10}
    ir1 = InputRequired("test", [])
    assert(ir1.evaluate(data))

def test_inputRequired_empty_array():
    data = {"test": [], "test_int": 10}
    ir1 = InputRequired("test", [])
    assert(ir1.evaluate(data) == False)


def test_inputRequired_nested_array():

    data = {"test": {"subtest":["something"]}, "test2":{"test_int": [10]}}
    ir1 = InputRequired("test.subtest", [])
    ir2 = InputRequired("test2.test_int", [])
    assert(ir1.evaluate(data))