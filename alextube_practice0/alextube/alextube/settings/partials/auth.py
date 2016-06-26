# Custom User model
AUTH_USER_MODEL = "users.Users"

LOGIN_URL = '/login/'

# messages snippet

LOGIN_SUCCESS_MESSAGE="Welcome! You have successfully logged in"
LOGIN_ERROR_MESSAGE="Sorry, something went wrong. Please try again."
SIGNUP_SUCCESS_MESSAGE="Welcome! Thank you for signing up. Now you can login with your account you just created."
LOGOUT_SUCCESS_MESSAGE="You have successfully logged out. Thanks for visiting and hope to see you again."

AUTHENTICATION_BACKENDS = [
        "social.backends.facebook.FacebookOAuth2",
        "social.backends.kakao.KakaoOAuth2",

        "django.contrib.auth.backends.ModelBackend",
        ]

SOCIAL_AUTH_FACEBOOK_KEY = "1560950074207034"
SOCIAL_AUTH_FACEBOOK_SECRET = "41038be3ad2bfb2e18a49ee26fb9750b"

SOCIAL_AUTH_KAKAO_KEY = "1001c75faef6ff9b04d984a16876a78f"
SOCIAL_AUTH_KAKAO_SECRET = "696a56e76fc6470e1260e5341dd6d325"


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/login/"
