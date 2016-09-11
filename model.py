from peewee import *

db = ''
psql_db = PostgresqlDatabase(db)
psql_db.connect()


# Define the base and user story class
class BaseModel(Model):
    class Meta:
        database = psql_db


class UserStory(BaseModel):
    story_title = CharField()
    user_story = CharField()
    acceptance_criteria = CharField()
    business_value = CharField()
    estimation = CharField()
    status = CharField()

    # When you run this method, then the db get the data.
    @staticmethod
    def add_story(data):
        for item in data:
            UserStory.create(story_title=item['story_title'],
                             user_story=item['user_story'],
                             acceptance_criteria=item['acceptance_criteria'],
                             business_value=item['business_value'],
                             estimation=item['estimation'],
                             status=item['status']
                             )
try:
    psql_db.create_table(UserStory)
    print("Table created.")
except ProgrammingError:
    pass
