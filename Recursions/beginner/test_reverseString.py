import pytest
from reverseString import reverseString

test_data = [
    ("siva", "avis"),
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("python", "nohtyp"),
    ("recursion", "noisrucer"),
    ("test", "tset"),
    ("12345", "54321"),
    ("a", "a"),
    ("", ""),
    ("madam", "madam"),
    ("level", "level"),
    ("radar", "radar"),
    ("civic", "civic"),
    ("noon", "noon"),
    ("kayak", "kayak"),
    ("deified", "deified"),
    ("rotor", "rotor"),
    ("refer", "refer")
]

@pytest.mark.parametrize("input_string, expected_output", test_data)
def test_reverseString(input_string, expected_output):
    assert reverseString(input_string) == expected_output, f"Test case for input_string='{input_string}' failed"
    print("All test cases passed!")
    
