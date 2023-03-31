class Input():

    def __init__(self, name, value=None):
        self.name = name
        self.value = value


class TextInput(Input):

    def is_empty(self):
        return self.value == None


class EmailInput(TextInput):

    def check(self):
        has_at = self.value.count("@") == 1
        has_dot = self.value.count(".") >= 1
        if has_at and has_dot:
            return True
        return False


class PasswordInput(TextInput):

    def check(self):
        if len(self.value) < 8:
            return False


usermail = EmailInput("usermail", "me@sky.pro")
print(usermail.is_empty())
print(usermail.check())
