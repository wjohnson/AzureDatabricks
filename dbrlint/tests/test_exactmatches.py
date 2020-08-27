from dbrlint.matchtypes import ExactMatch

def test_exact_literal():

    rule_string = "name: test"
    data = {"name": "test", "numeric_val": 0}

    match = ExactMatch("name","test")

    results = match.evaluate(data)
    assert(results == True)
    match_int = ExactMatch("numeric_val",0)

    results_int = match.evaluate(data)
    assert(results_int == True)

def test_exact_literal_missing():

    data = {"numeric_val": 0}

    match = ExactMatch("name","test")

    results = match.evaluate(data)
    assert(results == False)
    
def test_exact_nested_literal():

    rule_string = "name: test"
    data = {"new_cluster": {"num_workers":0}}

    match = ExactMatch("new_cluster.num_workers", 0)

    results = match.evaluate(data)
    assert(results == True)


def test_exact_array():

    data = {"name": ["test1","test2"]}

    match = ExactMatch("name",["test2","test1"])

    results = match.evaluate(data)
    assert(results == True)


def test_exact_nested_array():

    rule_string = "name: test"
    data = {"new_cluster": {"custom_tags":["mytag3","mytag2"], "emptyarray":[]}}

    matches = [
        ExactMatch("new_cluster.custom_tags", ["mytag3","mytag2"]),
        ExactMatch("new_cluster.emptyarray", [])
    ]

    for match in matches:
        results = match.evaluate(data)
        assert(results == True)


def test_exact_does_not_exist():

    data_exists = {"name": "test"}
    data_notexists = {"othername": "test2"}

    match = ExactMatch("name","")

    results_should_fail = match.evaluate(data_exists)
    results_should_pass = match.evaluate(data_notexists)
    assert(results_should_fail == False)
    assert(results_should_pass == True)
