from django.test import TestCase
import datetime
from .models import Post


class ModelFunctionTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Some Job I had", company="Google",
                            start_date=datetime.datetime.now() - datetime.timedelta(days=2 * 365),
                            end_date=datetime.datetime.now() - datetime.timedelta(days=365), active_post=False)

        Post.objects.create(title="Some Job I have right now", company="Alphabet",
                            start_date=datetime.datetime.now() - datetime.timedelta(days=2 * 365+1), active_post=True)

        Post.objects.create(title="Some Job I where I got fired", company="Microsoft",
                            start_date=datetime.datetime.now() - datetime.timedelta(days=365),
                            end_date=datetime.datetime.now() - datetime.timedelta(days=320), active_post=False)

    def test_month_diff(self):
        past_job = Post.objects.get(company="Google")
        current_job = Post.objects.get(company="Alphabet")
        fired_job = Post.objects.get(company="Microsoft")

        self.assertEqual(past_job.get_month_diff(past_job.start_date, past_job.end_date), 12)
        self.assertEqual(current_job.get_month_diff(current_job.start_date, datetime.datetime.now()), 24)

        self.assertEqual(fired_job.get_month_diff(fired_job.start_date, fired_job.end_date), 1)

    def test_month_diff_string(self):
        past_job = Post.objects.get(company="Google")
        current_job = Post.objects.get(company="Alphabet")
        fired_job = Post.objects.get(company="Microsoft")

        self.assertEqual(past_job.get_month_diff_string, "1 Year")
        self.assertEqual(current_job.get_month_diff_string, "2 Years")
        self.assertEqual(fired_job.get_month_diff_string, "1 Month")

    def test_get_longest(self):
        past_job = Post.objects.get(company="Google")

        self.assertEqual(past_job.get_longest_post(), 24)

    def test_relative_length(self):
        past_job = Post.objects.get(company="Google")
        current_job = Post.objects.get(company="Alphabet")
        fired_job = Post.objects.get(company="Microsoft")

        self.assertEqual(past_job.get_relative_length, 50)
        self.assertEqual(current_job.get_relative_length, 100)
        self.assertEqual(fired_job.get_relative_length, 18)
