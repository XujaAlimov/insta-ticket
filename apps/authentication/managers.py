from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, email=None, phone_number=None, username=None, **extra_fields):
        if not email:
            pass
        if not phone_number:
            pass
        if not username:
            pass
        if email:
            email=self.normalize_email(email)
        user=self.model(email=email, username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, email=None, phone_number=None, username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( password,email, phone_number, username, **extra_fields)

    def create_superuser(self, password, email=None, phone_number=None, username=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)   
        extra_fields.setdefault('is_staff', True)  
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(password,email, phone_number, username, **extra_fields)