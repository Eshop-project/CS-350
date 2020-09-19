from .models import NewUser


def add_user(user, name):
    return NewUser.objects.create(user=user, name=name)


def get_user(name):
    return NewUser.objects.get(name=name)


def delete_user(name):
    NewUser.objects.get(name=name).delete()


def list_user():
    return NewUser.objects.all()