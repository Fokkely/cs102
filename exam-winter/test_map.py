from map import decode_from_emoji, encode_to_emoji, wave

def test_decode_from_emoji():
    assert decode_from_emoji('☒') == -1
    assert decode_from_emoji('.') == 0
    assert decode_from_emoji('☺') == 0
    assert decode_from_emoji('☼') == 0


def test_encode_to_emoji():
    assert encode_to_emoji(-1) == '☒'
    assert encode_to_emoji(-2) == '☺'
    assert encode_to_emoji(-3) == '☼'
    assert encode_to_emoji(8) == '.'


def test_wave():
    assert wave(1, 1, 1, [[-1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, -1, 0, 0, -1], [-1, -1, 0, -1, 0, -1, -1], [-1, 0, 0, -1, 0, 0, -1], [-1, 0, -1, 0, -1, 0, -1], [-1, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1]]) == \
                          [[-1, -1, -1, -1, -1, -1, -1],
                          [-1, 1, 2, -1, 16, 17, -1],
                          [-1, -1, 3, -1, 15, -1, -1],
                          [-1, 5, 4, -1, 14, 13, -1],
                          [-1, 6, -1, 10, -1, 12, -1],
                          [-1, 7, 8, 9, 10, 11, -1],
                          [-1, -1, -1, -1, -1, -1, -1]]





