# -*- coding: utf-8 -*-


from typing import Optional
from ...models.article import Article, Next


def getNextChapter(chapter: int, articles: list[Article]) -> Optional[Next]:
    for i in range(len(articles)):
        if articles[i]["chapter"] == chapter:
            if i + 1 < len(articles):
                next_article = articles[i + 1]
                return Next(
                    next_article["id"],
                    next_article["chapter"],
                    next_article["title"],
                )
            else:
                return None
    return None
