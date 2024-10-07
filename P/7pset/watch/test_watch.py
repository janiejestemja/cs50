from watch import parse

def test_parse():
    assert parse("<iframe src=\"http://youtube.com/embed/something\"></iframe>") == "https://youtu.be/something"
    assert parse("<iframe src=\"https://youtube.com/embed/something\"></iframe>") == "https://youtu.be/something"
    assert parse("<iframe src=\"http://www.youtube.com/embed/something\"></iframe>") == "https://youtu.be/something"
    assert parse("<iframe src=\"https://www.youtube.com/embed/something\"></iframe>") == "https://youtu.be/something"