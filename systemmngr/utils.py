def gen_role_related_user(users, users_role):
    for user in users:
        for user_role in users_role:
            user.checked = 'unchecked'
            if user_role.userid == user.id:
                user.checked = 'checked'
                break;
        yield user
          
