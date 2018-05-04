#!/usr/local/bin/python3

"""
    Use parse function to analyze the inputs.

    is_add_mac_legal function returns True when the data of "add mac" keywords thing are all correct,
    returns False when incorrect following by false data to be referenced.
"""

import re
import json

REGEXs = {
    'macs': r'([a-z0-9]+[:-]){5}[a-z0-9]{0,2}',
    'customer_id': r'[a-z][0-9]{9}',
    'chinese_characters': r'[\u4e00-\u9fff]+',
    'bad_words': r'(fuck|shit|fxxk|fxk|ass)'
}

REGEX_ITEMS = [x for x in REGEXs.keys()]
REGEX_PATTERNS = [y for y in REGEXs.values()]


#  TODO: check if id is legal.
def is_id_legal(id):
    pass


def is_mac_legal(mac):
    mac_regex = re.compile(r'([a-f0-9]{2}[:-]){5}[a-f0-9]{2}', re.IGNORECASE)
    return mac_regex.match(mac) and True or False


def __regex_match(regex, pattern, text_):
    text_ = text_ or ''  # if value is None covert to '' so that re.finditer won't go wrong.
    return {regex: tuple(x.group() for x in re.finditer(pattern, text_, re.IGNORECASE)) or None}


def parser(text_=None, regex=REGEX_ITEMS, pattern=REGEX_PATTERNS):
    # convert user inputs.
    text_ = {
        tuple: lambda x: ' '.join(str(i) for i in x),
        set: lambda x: ' '.join(str(i) for i in x),
        list: lambda x: ' '.join(str(i) for i in x),
        dict: lambda x: json.dumps(x),
        str: lambda x: x,
    }.get(type(text_), lambda x: str(text_))(text_)
    result = {}  # return dict

    # calling regular expression function and build up the return-value.
    for k, v in dict(zip(regex, pattern)).items():
        result = {**result, **__regex_match(k, v, text_)}

    # split the 'chinese_characters' values into meaningful named items.
    if len(result.get('chinese_characters') or '') == 3:
        for i, k in enumerate(('team_name', 'team_user', 'customer_name')):
            result[k] = result.get('chinese_characters')[i]

    # check mac legality.
    for mac in result.pop('macs') or '':
        if is_mac_legal(mac):
            # when is legal, put it back in the dict.
            result['macs'] = result.get('macs', tuple()) + (mac.lower(),)
        else:
            # when illegal, put it in the dict and name it "fake_mac".
            result['fake_macs'] = result.get('fake_macs', tuple()) + (mac.lower(),)

    # deduplicate macs
    result['macs'] = deduplicate(result.get('macs'))
    result['fake_macs'] = deduplicate(result.get('fake_macs'))

    return result


# deduplicate iterable, obvious.
def deduplicate(x):
    x = x or ()  # prevent NoneType object to be iterate
    r = []
    for i in x:
        if i not in r:
            r.append(i)
    return tuple(r) or None


def is_add_mac_legal(result):
    check_point = ()
    if len(result.get('chinese_characters') or '') != 3:
        check_point += 'name',
    if not result.get('customer_id'):
        check_point += 'id',
    if not result.get('macs'):
        check_point += 'mac',
    if result.get('fake_macs'):
        check_point += result.get('fake_macs')
    return (not check_point) and (True, None) or (False, check_point)


if __name__ == '__main__':
    pass


