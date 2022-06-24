from scripts import logger
from userapp.models import User
from userapp.serializers import UserSerializer
from storyapp.models import Story
from storyapp.serializers import StorySerializer
from storyapp.model_choices import StoryChoice
from faker import Faker
import random

class AddStory:

    user: User = None
    user_id = None
    
    def __init__(self, username:str):
        self.user = User.objects.filter(username=username).first()
        if not self.user:
            logger.error(f'User: {username} not found')
            self.user = User.objects.create(
                username=username,
                password = "Password123",
                email = f"{username}@gmail.com"
            )
        self.user_id = self.user.id

    def generate_story(self):
        fake = Faker()
        genre_list = [
            StoryChoice.comedy,
            StoryChoice.drama,
            StoryChoice.fable,
            StoryChoice.fairy_tale,
            StoryChoice.fantasy,
            StoryChoice.folklore,
            StoryChoice.historical_fiction,
            StoryChoice.horror,
            StoryChoice.legend,
            StoryChoice.mystery,
            StoryChoice.mythology,
            StoryChoice.parody,
            StoryChoice.romance,
            StoryChoice.saga,
            StoryChoice.science_fiction
        ]
        
        random.seed()
        
        title = fake.sentence(nb_words=12, variable_nb_words=True).title()
        description = fake.text(max_nb_chars=256)
        genre = random.choice(genre_list)
        body = fake.text(max_nb_chars=5000)
        author = self.user_id

        resp = {
            'title': title,
            'description': description,
            'genre': genre,
            'body': body,
            'author': author
        }
    
        return resp
    
    def add_story(self, n_entries:int=0):

        for i in range(n_entries):
            resp = self.generate_story()
            serialized = StorySerializer(data=resp)
            if serialized.is_valid():
                serialized.save()
            else:
                logger.error(f'Story serializer invalid: {serialized.errors}')
                raise Exception(f'Story serializer invalid: {serialized.errors}')
        
        return True


def main():
    add_story = AddStory('default_author')
    add_story.add_story(n_entries=2500)


if __name__ == '__main__':
    main()

