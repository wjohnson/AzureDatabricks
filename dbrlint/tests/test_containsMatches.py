from dbrlint.matchtypes import ContainsMatch

def test_contains_array_strings():

    data = {"array_of_strings": ["required1", "required2", "optional1"]}

    match = ContainsMatch("array_of_strings",["required1","required2"])

    results = match.evaluate(data)
    assert(results == True)
    should_fail = ContainsMatch("array_of_strings",["required3"])
    should_fail2 = ContainsMatch("array_of_strings",["required1","required3"])

    should_fail_results = should_fail.evaluate(data)
    should_fail2_results = should_fail2.evaluate(data)
    assert(should_fail_results == False)
    assert(should_fail2_results == False)

def test_contains_array_int():
    data = {"array_of_ints": [1,2,3]}

    match = ContainsMatch("array_of_ints", [1,2])
    match2 = ContainsMatch("array_of_ints", [4])

    results = match.evaluate(data)
    assert(results == True)
    results_should_be_false = match2.evaluate(data)
    assert(results_should_be_false == False)

def test_contains_array_dict():
    data = {"array_of_dicts": [{"key":"test","value":"req"}, {"key":"test2","value":"optional"}]}

    match = ContainsMatch("array_of_dicts", [{"key":"test","value":"req"}])

    results = match.evaluate(data)
    assert(results == True)
