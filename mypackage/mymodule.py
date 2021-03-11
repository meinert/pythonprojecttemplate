from datetime import datetime, timedelta


# Firebase guide
# https://morioh.com/p/a593f973aff0


class MyClass():
    def __init__(self, input):
        self.input = input
    # set	Write or replace data to a defined path, like messages/users/<username>
    # update	Update some of the keys for a defined path without replacing all of the data
    # push	Add to a list of data in the database. Every time you push a new node onto a list, your database generates a unique key, like messages/users/<unique-user-id>/<username>
    # transaction	Use transactions when working with complex data that could be corrupted by concurrent updates


class MySecondClass():

    def __init__(self, input):
        self.input = input