from peewee import *

db = input("Give your database name: ")
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

    # When you run this method, then the db get the data.
    @staticmethod
    def add_story(data):
        for item in data:
            UserStory.create(story_title=item['Story Title'],
                             user_story=item['User Story'],
                             acceptance_criteria=item['Acceptance Criteria'],
                             business_value=item['Business Value'],
                             estimation=item['Estimation']
                             )
try:
    psql_db.create_table(UserStory)
    print("Table created.")
except ProgrammingError:
    pass
