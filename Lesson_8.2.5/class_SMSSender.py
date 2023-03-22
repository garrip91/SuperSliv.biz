class SMSSender():

    def send_sms(self, message):
        print("Отправим сообщение через смс:", message)


class PushSender():

    def send_push(self, message):
        print("Отправим сообщение через пуш-уведомления:", message)


class MailSender():

    def send_mail(self, message):
        print("Отправим сообщение через почту:", message)


class SuperSender(SMSSender, PushSender, MailSender):

    def send_all(self, message):
        self.send_sms(message)
        self.send_push(message)
        self.send_mail(message)


sender = SuperSender()
sender.send_all("Text message")
