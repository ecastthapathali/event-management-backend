from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , email = None , password = None , **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError("Email is Required")
        
        user = self.model(email=email , **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        
        return user    
        
        
        
           
    def create_superuser(self , email = None , password = None , **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        
        return self.create_user(email , password , **extra_fields)
        