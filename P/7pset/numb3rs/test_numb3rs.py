from numb3rs import validate

def test_validate_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    for i in range(256):
        assert validate(f"{i}.0.0.0") == True
        assert validate(f"0.{i}.0.0") == True
        assert validate(f"0.0.{i}.0") == True
        assert validate(f"0.0.0.{i}") == True

def test_validate_false():
    assert validate("cat") == False
    assert validate("cat.dog.horse.lion") == False 
    assert validate("0") == False 
    assert validate("0.0") == False 
    assert validate("0.0.0") == False 
    assert validate("0.0.0.0.0") == False 
    