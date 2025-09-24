import secrets
import string
from dataclasses import dataclass
from typing import Any


@dataclass
class Password:
    length: int = 12
    use_uppercase: bool = True
    use_special_characters: bool = True

    base_characters: str = (
        string.ascii_lowercase + string.digits
    )  # Base password consisting of alphabets and digits

    def generate_password(self) -> str:
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_special_characters:
            self.base_characters += string.punctuation

        generated_password: str = "".join(
            secrets.choice(self.base_characters) for _ in range(self.length)
        )
        return generated_password

    def password_strength_calculator(self, password_to_check: str) -> list[str]:
        issues: list[str] = []
        if len(password_to_check) < 16:
            issues.append("Password should be 16 or more characters long.")
        if not any(char.isupper() for char in password_to_check) and not (
            any(char in string.punctuation for char in password_to_check)
        ):
            issues.append(
                "Password should contain both upper case and special characters."
            )
        return issues


if __name__ == "__main__":
    pwd: Password = Password(length=17, use_uppercase=True, use_special_characters=True)
    generated_pwd: str = pwd.generate_password()
    print(
        f"The generated password is : {generated_pwd} having {pwd.length} characters."
    )
    print("Lets evaluate the generated password.")
    issues: list[str] | Any = pwd.password_strength_calculator(generated_pwd)
    if issues:
        print("The generated password has the following issues!")
        for issue in issues:
            print(f"* {issue}")
    else:
        print("Hurrah! The generated password has no issues.")
