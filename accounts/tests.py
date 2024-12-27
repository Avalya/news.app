from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "avalya20",  # No leading/trailing spaces
                "email": "kubatbekkyzydinara165@gmail.com",  # No leading/trailing spaces
                "password1": "avalya20",  # No space at the end
                "password2": "avalyo20",  # Passwords match
            },
        )

        # Ensure the response redirects after a successful signup
        self.assertEqual(response.status_code, 302)

        # Check that one user was created
        self.assertEqual(get_user_model().objects.all().count(), 1)

        # Verify the details of the newly created user
        user = get_user_model().objects.all()[0]
        self.assertEqual(user.username, "avalya20")  # Ensure no extra spaces
        self.assertEqual(user.email, "kubatbekkyzydinara165@gmail.com")  # Ensure no extra spaces

