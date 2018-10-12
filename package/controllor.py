import json

def open_file(fn):

    if fn.__name__ == "search":
        model = "r"
    else:
        model = "w"

    with open("/data/text_content.json", model, encoding="utf-8") as f:
        f.read()
        fn()
    

def get_string():
    return "fine三小啦 只是測試w"

def test_response():
    return "test"

@open_file
def add_string(str):
