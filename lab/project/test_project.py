# it is necesary to put first this command export API_KEY=c1cccd9af9e325c1b9e0d7b41193b0bd in your CLI to test

from project import validate, get_interface, get_design, get_nmap_scanner, get_location
import pytest
from io import StringIO

def test_validate_True():
    assert validate(r"1.2.3.4") == True

def test_validate_False():
    assert validate(r"512.512.512.512") == False
    assert validate(r"1") == False
    assert validate(r"cat") == False
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1.") == False

# python project.py
number_inputs = StringIO('155.248.226.213\n')
def test_get_interface(monkeypatch):
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert get_interface() == "155.248.226.213"

number_input = StringIO('155.248.226.cat\n')
def test_get_interface_False(monkeypatch):
    monkeypatch.setattr('sys.stdin', number_input)
    with pytest.raises(SystemExit) as e:
        get_interface()
        assert e.type == SystemExit
        assert e.value.code == 1

def test_get_nmap_scanner():
    ip_address = "155.248.226.213"
    assert get_nmap_scanner(ip_address) == None


def test_get_location():
    ip_address = "155.248.226.213"
    assert get_location(ip_address) == None

