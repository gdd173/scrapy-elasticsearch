from elasticsearch_dsl import DocType,Nested,Date,Boolean,analyzer,Completion,Text,Keyword,Integer
from elasticsearch_dsl.connections import connections


connections.create_connection(hosts="192.168.20.43")
class ArticleType(DocType):
    title = Text(analyzer='ik_max_word')


    url = Keyword()
    url_token = Keyword()


    answer_count = Integer()
    article_count = Integer()
    connercial_question_count = Integer()
    favorite_count = Integer()
    favorited_count = Integer()
    follower_count = Integer()
    following_columns_count = Integer()
    following_count = Integer()
    pins_count = Integer()
    question_count = Integer()
    thank_from_count = Integer()
    thank_to_count = Integer()
    thanked_count = Integer()
    vote_from_count = Integer()
    vote_to_count = Integer()
    voteup_count = Integer()
    following_favlists_count = Integer()



    class Index:
        #数据库名称和表名称
        name = "zhihu"
        doc_type = 'dictionary'

if __name__ == '__main__':
    ArticleType.init()

