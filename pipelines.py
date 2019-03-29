# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from zhihuuser.models.es_type import ArticleType


class ZhihuuserPipeline(object):
    def process_item(self, item, spider):
        article = ArticleType()
        article.title = item['headline']
        article.url = item['url']
        article.answer_count = item['answer_count']
        article.articles_count = item['articles_count']
        article.commercial_question_count = item['commercial_question_count']
        article.favorite_count = item['favorite_count']
        article.favorited_count = item['favorited_count']
        article.follower_count = item['follower_count']
        article.following_columns_count = item['following_columns_count']
        article.following_count = item['following_count']
        article.pins_count = item['pins_count']
        article.question_count = item['question_count']
        article.thank_from_count = item['thank_from_count']
        article.thank_to_count = item['thank_to_count']
        article.thanked_count = item['thanked_count']
        article.vote_from_count = item['vote_from_count']
        article.vote_to_count = item['vote_to_count']
        article.voteup_count = item['voteup_count']
        article.following_favlists_count = item['following_favlists_count']

        article.save()
        return item
