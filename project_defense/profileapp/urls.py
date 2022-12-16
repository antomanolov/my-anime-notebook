from django.urls import path, include

from project_defense.profileapp.views import SignUpView, SignInView, \
    SignOutView, ProfileDetails, ProfileEdit, ProfileDelete

urlpatterns = (
    path('signup/', SignUpView.as_view(), name='sign up page'),
    path('signin/', SignInView.as_view(), name='sign in page'),
    path('signout/', SignOutView.as_view(), name='sign out page'),
    path('profile/', include(
        [
            path('details/<int:pk>', ProfileDetails.as_view(), name='profile details page'),
            path('edit/<int:pk>', ProfileEdit.as_view(), name='profile edit page'),
            path('delete/<int:pk>', ProfileDelete.as_view(), name='profile delete page'),
        ]
    )),
)
