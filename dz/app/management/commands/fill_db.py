from django.core.management import BaseCommand
from faker import Faker

from app.models import Profile, QuestionLike, Tag, Question, Answer, TagQuestion, User, UserLike

fake = Faker()
class Command(BaseCommand):
    help = "Fills database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("num", type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        users = [ User(username =fake.unique.name(), first_name = fake.first_name(), 
                                      date_joined=str(fake.date_between(start_date='-20y', end_date='-1y')),
                                      email =   fake.unique.ascii_email() ) for _ in range (num)]
        print ('user data is ready')
       
        User.objects.bulk_create(users)
        users = User.objects.all()
        users_count = users.count()
        print('USERS DONE')
        profiles = [
            Profile(img = '',user = user) for user in users
        ]
        print ('profile data is ready')
        Profile.objects.bulk_create(profiles)
        profiles = Profile.objects.all()
        profiles_count = profiles.count()
        print('PROFILES DONE')
        questions = [
            Question(title = fake.unique.sentence(), text = fake.text(max_nb_chars=499),
                     author = users[fake.random_int(min=0, max=users_count - 1)],
                     creation_date = str(fake.date_between(start_date='-20y', end_date='-1y')) )
                       for _ in range(num*10)
        ]
        print('question data is ready')
        Question.objects.bulk_create(questions)
        questions = Question.objects.all()
        questions_count = questions.count()
        print('QUESTIONS DONE')
        answers = [
            Answer(
                text = fake.text(max_nb_chars = 499), is_correct = fake.random_int() % 2 == 0,
                question= questions[fake.random_int(min=0, max=questions_count - 1)],
                author = users[fake.random_int(min=0, max=users_count - 1)],
                creation_date = str(fake.date_between(start_date='-20y', end_date='-1y')) 
            )for _ in range(num*100)
        ]
        print('answer data is ready')
        Answer.objects.bulk_create(answers)
        print ("ANSWERS DONE")#fake.unique.word()
        #tag_names = fake.words(nb =500, unique = True)
        tags = [
            Tag(name =  fake.unique.word())for _ in range (500)
        ]
        print ('tag data is ready')
        Tag.objects.bulk_create(tags)
        tags = Tag.objects.all()
        tags_count = tags.count()
        print ('TAGS DONE')
        tqs = [
          TagQuestion(question = questions[fake.random_int(min=0, max=len(questions) - 1)], tag = tags[fake.random_int(min=0, max=tags_count- 1)])
          for _ in range(num*200)
            
        ]
        print ('tq data is ready')
        TagQuestion.objects.bulk_create(tqs)
        print ('TQS DONE')
        user_likes = [
            UserLike(from_user =users[fake.random_int(min=0, max=users_count - 1)], 
                     to_user = users[fake.random_int(min=0, max=users_count - 1)] )
                     for _ in range(num*100)
        ]
        print('userlike data ready')
        UserLike.objects.bulk_create(user_likes)
        print ('USERLIKE DONE')
        question_likes = [
             QuestionLike(user =users[fake.random_int(min=0, max=users_count - 1)], 
                     question = questions[fake.random_int(min=0, max=len(questions) - 1)])
                     for _ in range(num*100)
        ]
        print ('questionlike data ready')
        QuestionLike.objects.bulk_create(question_likes)
        print ('QUESTIONLIKE DONE')
        for user in users:
            user.set_password(user.username)
        print('user passwords are set')
        print ('ALL DONE')
     