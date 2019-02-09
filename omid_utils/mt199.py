import re
from datetime import date


class MT199:
    """
    Parses an MT199 standard banking format string into a string-like Python
    object so you can do things like `mt199.basic_header` or `print(mt199)`.

    Usage:

    mt199 = MT199("some-mt-199-string")
    print("basic header: {}, bank op code: {}, complete message: {}".format(
        mt199.basic_header,
        mt199.text.related_reference
        mt199
    ))

    With considerable help from:
    http://www.sepaforcorporates.com/swift-for-corporates/read-swift-message-structure/
    """

    MESSAGE_REGEX = re.compile(
        "^"
        "({1:(?P<basic_header>[^}]+)})?"
        "({2:(?P<application_header>I[^}]+)})?"
        "({3:(?P<user_header>({113:[A-Z]{4}})?({108:[A-Z0-9]{0,16}}))})?"
        "({4:\s*(?P<text>.+?)\s*-})?"
        "({5:(?P<trailer>[^}]+)})?"
        "$",
        re.DOTALL
    )

    def __init__(self, message):

        if message is None:
            message = ""

        self.raw = message.strip()
        self.basic_header = None
        self.application_header = None
        self.user_header = None
        self.text = None
        self.trailer = None

        self._boolean = False

        self._populate_by_parsing()

    def __str__(self):
        return self.raw

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self._boolean
    __nonzero__ = __bool__  # Python 2

    def _populate_by_parsing(self):

        if not self.raw:
            return

        m = self.MESSAGE_REGEX.match(self.raw)

        self._boolean = bool(m)

        if not m:
            return None

        self.basic_header = m.group("basic_header")
        self.application_header = m.group("application_header")
        self.user_header = m.group("user_header")
        self.trailer = m.group("trailer")

        self.text = Text(m.group("text") or "")


class Text(object):
    """
    With considerable help from:
    https://en.wikipedia.org/wiki/MT199 and
    https://gist.github.com/dmcruz/9940a6b217ff701b8f3e
    """

    REGEX = re.compile(
        "^"
        "(:20:(?P<transaction_reference>[^\s:]+)\s*)?"
        "(:21:(?P<related_reference>[^\s:]+)\s*)?"
        "(:79:(?P<narrative>.*?)\s*(?=(:\d\d)?))?"
        "$",
        re.DOTALL
    )

    def __init__(self, raw):

        self.raw = raw

        self.transaction_reference = None
        self.related_reference = None
        self.narrative = None
        self.details_of_charges = None
        self.date = None

        self._boolean = False

        self._populate_by_parsing()

    def __str__(self):
        return self.raw

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self._boolean
    __nonzero__ = __bool__  # Python 2

    def _populate_by_parsing(self):

        if not self.raw:
            return

        m = self.REGEX.match(self.raw)

        self._boolean = bool(m)

        if not m:
            return

        for k, v in m.groupdict().items():
            if v is None:
                continue
            setattr(self, k, v)


