import sys
if sys.version_info < (3, 0):
    UNKNOWN_PATTERN = r'# Unknown object type: (?P<t>.+)'
    INVALID_PATTERN = r'# Invalid object specification: \'(?P<t>.+)\''
    NOTFOUND_PATTERN = r'# (?P<t>\w+) (?P<r>\d+) does not exist.'
    NAMED_NOTFOUND_PATTERN = r'# No (?P<t>\w+) named (?P<r>\w+) exists.'
    NAN_PATTERN = r'# Objects of type (?P<t>\w+) must be specified by numeric id.'
    NOT_CREATED_PATTERN = r'# Could not create (?P<t>\w+).'
    NO_MATCHING_PATTERN = r'No matching results.'
    CREATED_PATTERN = r'# (?P<t>\w+) (?P<r>\d+) created.'
    UNAUTHORIZED_PATTERN = r'# You are not allowed to modify (?P<t>\w+) (?P<r>\w+).'
    HEADER_PATTERN = r'^RT/(?P<v>.+)\s+(?P<s>(?P<i>\d+).+)'
    COMMENT_PATTERN = r'^#\s+.+$'
    SECTION_PATTERN = r'^--'
else:
    UNKNOWN_PATTERN = br'# Unknown object type: (?P<t>.+)'
    INVALID_PATTERN = br'# Invalid object specification: \'(?P<t>.+)\''
    NOTFOUND_PATTERN = br'# (?P<t>\w+) (?P<r>\d+) does not exist.'
    NAMED_NOTFOUND_PATTERN = br'# No (?P<t>\w+) named (?P<r>\w+) exists.'
    NAN_PATTERN = br'# Objects of type (?P<t>\w+) must be specified by numeric id.'
    NOT_CREATED_PATTERN = br'# Could not create (?P<t>\w+).'
    NO_MATCHING_PATTERN = br'No matching results.'
    CREATED_PATTERN = br'# (?P<t>\w+) (?P<r>\d+) created.'
    UNAUTHORIZED_PATTERN = br'# You are not allowed to modify (?P<t>\w+) (?P<r>\w+).'
    HEADER_PATTERN = br'^RT/(?P<v>.+)\s+(?P<s>(?P<i>\d+).+)'
    COMMENT_PATTERN = br'^#\s+.+$'
    SECTION_PATTERN = br'^--'
