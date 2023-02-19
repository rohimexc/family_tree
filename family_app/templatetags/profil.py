from django import template
from django.contrib.auth.models import User
from family_app.models import Profile

register = template.Library()
@register.simple_tag(takes_context=True)
def get_user_profil(context):
    request = context['request']
    try:
        profile = Profile.objects.get(user=User.objects.get(username=request.user))
        photo='./media/' + profile.profil
    except:
        photo='./static/img_2/profile-img.jpg'
    return photo
    