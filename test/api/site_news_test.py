import random

from moex_python_sdk.api import MoexApi
from moex_python_sdk.models.site_news import new_site_news_params

from test.api import check_content, check_all_content


def test_get_moex_news(moex_api: MoexApi):
    security_group_api = moex_api.site_news()

    params = new_site_news_params()
    news = security_group_api.get_all_news(params)["content"]

    check_all_content(news)

    _news_id = random.choice(news["site_news"]["data"])[0]
    new = security_group_api.get_one_news(
        _news_id,
    )["content"]["content"]

    check_content(new)
    assert len(new["data"]) > 0

