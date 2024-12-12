import random
import string

def generate_password(length: int = 12) -> str:
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")
    
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = 12  # Define um valor padrão de 12 para a geração de senha.
    print(f"Generated Password: {generate_password(length)}")
