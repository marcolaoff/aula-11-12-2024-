import pytest
from app.password_generator import generate_password

def test_generate_password_length():
    password = generate_password()
    assert len(password) >= 6, "Password length should be at least 6 characters."

def test_generate_password_characters():
    password = generate_password()
    assert any(c.isdigit() for c in password), "Password should contain at least one digit."
    assert any(c.islower() for c in password), "Password should contain at least one lowercase letter."
    assert any(c.isupper() for c in password), "Password should contain at least one uppercase letter."
    assert any(c in string.punctuation for c in password), "Password should contain at least one special character."