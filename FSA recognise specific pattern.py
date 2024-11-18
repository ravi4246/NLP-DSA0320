
INITIAL_STATE = 'q0'
ACCEPTING_STATE = 'q2'
TRANSITIONS = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}

test_strings = ["ab", "aab", "bab", "bbaaab", "a", "b", "abc"]

for string in test_strings:
    current_state = INITIAL_STATE
    for char in string:
        current_state = TRANSITIONS[current_state].get(char, INITIAL_STATE)
    result = "accepted" if current_state == ACCEPTING_STATE else "not accepted"
    print(f"'{string}' is {result}.")
