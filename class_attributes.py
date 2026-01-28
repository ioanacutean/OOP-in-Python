class User:
    active_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def activate(self):
        if not self.is_active():
            self.__class__.active_users.append(self)

    def deactivate(self):
        if self.is_active:
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users


me = User('Ioana', 'ioana@gmail.com')
me.name = 'Ioana Morosanu'
print(me.name)

print('Active:', me.is_active(), 'Active users:', User.active_users)
me.activate()
print('Active:', me.is_active(), 'Active users:', User.active_users)
me.deactivate()
print('Active:', me.is_active(), 'Active users:', User.active_users)

print('Active users of "me":', me.active_users, 'Class Level: ', User.active_users)
me.active_users = "Just me"
print('Active users of "me":', me.active_users, 'Class Level: ', User.active_users)