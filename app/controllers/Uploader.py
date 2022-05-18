class Uploader:

    def intToString(self, number):
        result = ''
        try:
            result = str(number)
        except:
            pass
        return result

    def addZeroToString(self, number):
        count_char = len(str(number))
        if (count_char < 11):
            result = number.zfill(11)
        else:
            result = number
        return result

    def validSnils(self, snils):
        value_string = self.intToString(snils)
        value = self.addZeroToString(value_string)
        return value

    def validString(self, str):
        value_string = self.intToString(str)
        value = value_string.strip()
        return value