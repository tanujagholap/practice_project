from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    print('logged in')
    

@receiver(user_login_failed)
def log_user_login_failed(sender, user=None, **kwargs):
    if user:
        print('login success')
    else:
        print('login failed')
        
        
@receiver(user_logged_out)
def log_user_logout(sender, user, **kwargs):
    print('logged out')
    
    