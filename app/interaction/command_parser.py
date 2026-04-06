class CommandParser:

    def parse(self, text):

        text = text.lower()

        if "repeat" in text:
            return "repeat"

        if "example" in text:
            return "example"

        if "next" in text:
            return "next"

        if "did not understand" in text:
            return "repeat"

        return "question"