from parser.pe import ParseError

class Parser:
    def __init__(self):
        self.cache = {}

    def parse(self, text):
        self.text = text
        self.pos = -1
        self.len = len(text) -1
        rv = self.start()
        self.assert_end()
        return rv
    
    def assert_end(self):
        if self.pos < self.len:
            raise ParseError(
                self.pos + 1,
                'Expected end of string but got %s',
                self.text[self.pos + 1]
            )

    def eat_whitespace(self):
        while self.pos < self.len and self.text[self.pos + 1] in " \f\v\r\t\n":
            self.pos += 1
    
    def split_char_ranges(self, chars):
        try:
            return self.cache[chars]
        except KeyError:
            pass

        rv = []
        index = 0
        length = len(chars)

        while index < length:
            if index + 2 < length and chars[index + 1] == '-':
                if chars[index] >= chars[index + 2]:
                    raise ValueError("Bad character range")
                rv.append(chars[index:index + 3])
                index += 3
            else:
                rv.append(chars[index])
                index += 1
        self.cache[chars] = rv
        return rv
    
    def char(self, chars=None):
        if self.pos >= self.len:
            raise ParseError(
                self.pos + 1,
                'Expected %s but got end of string',
                'character' if chars is None else '[%s]' % chars
            )
        next_char = self.text[self.pos + 1]

        if chars == None:
            self.pos += 1
            return next_char
        
        for char_range in self.split_char_ranges(chars):
            if len(char_range) == 1:
                if next_char == char_range:
                    self.pos += 1
                    return next_char
            elif char_range[0] <= next_char <= char_range[2]:
                self.pos += 1
                return next_char
        raise ParseError(
            self.pos + 1,
            'Expected %s but got %s',
            'character' if chars is None else '[%s]' % chars,
            next_char
        )