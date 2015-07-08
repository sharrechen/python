__author__ = 'sharon'

_formats = {
    'ymd': '{d.year}/{d.month}/{d.day}',
    'mdy': '{d.month}-{d.day}-{d.year}',
    'dmy': '{d.day}.{d.month}.{d.year}'
}


class DateTime:
    __slots__ = ['year', 'month', 'day']  # optimization tool
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return 'DateTime({0.year!r}, {0.month!r}, {0.day!r})'.format(self)

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


class Book:
    def __init__(self, name, author, publish_date):
        self.name = name
        self.author = author
        self.publish_date = publish_date

    def __repr__(self):
        return 'Book({0.name!r}, {0.author!r}, {0.publish_date!r})'.format(self)

    def __str__(self):
        return '{0.author!s} writes a book "{0.name!s}" published on {0.publish_date!s}'.format(self)

if __name__ == "__main__":
    publish_date = DateTime(2000, 12, 25)
    print(format(publish_date))
    print(format(publish_date, 'dmy'))
    print('Book published date is {:mdy}'.format(publish_date))
    book = Book('Merry Christmas Python!', 'Santa', publish_date)
    print('book is {0!r}'.format(book))
    print('book info : {0}'.format(book))