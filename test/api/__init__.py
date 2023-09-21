from typing import List, Dict


def check_content(content: Dict):
    assert isinstance(content["metadata"], Dict)
    assert isinstance(content["columns"], List)
    assert isinstance(content["data"], List)


def check_all_content(data):
    for i in data.keys():
        check_content(data[i])
        assert len(data[i]["data"]) > 0

