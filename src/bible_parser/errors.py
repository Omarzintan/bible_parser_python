"""Custom exceptions for the bible_parser package."""


class BibleParserException(Exception):
    """Base exception for all bible_parser errors."""

    pass


class ParseError(BibleParserException):
    """Raised when parsing XML content fails."""

    pass


class FormatDetectionError(BibleParserException):
    """Raised when the Bible format cannot be automatically detected."""

    pass


class ParserUnavailableError(BibleParserException):
    """Raised when a parser for the specified format is not available."""

    pass
