from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    """@property
    def name(self):
        #print (self._name.value)
        return self._name

    @name.setter
    def name (self, val):
        if val.value.isalpha(): 
            val.value = val.value.capitalize()
            self._name = val
        else:
            raise Exception ("Wrong name")"""
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.search(r"\+\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}|\+\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}", new_value):
            self.__value = new_value
        else:
            raise TypeError("Invalid number phone")


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.search(r"\d{4}\-\d{2}\-\d{2}", new_value):
            self.__value = new_value
        else:
            raise TypeError("Your need enter year-month-day")


class Record(Name, Phone, Birthday):
    phones = []

    def __init__(self, name, phone, birthday):
        self._name = None
        self.name = name

        self.phone = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def name_name(self):
        self.value = Name

    def birt_day(self):
        self.value = Birthday

    def phone_phone(self):
        self.value = Phone

    def add_phone(self, phone):
        if not phone in self.phones:
            self.phones.append(phone)

    def chenge_phone(self, phone, ph):
        if phone in self.phones:
            ind = self.phones.index(phone)
            self.phones[ind] = ph

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def days_to_birthday(self, birthday):
        bir_list = []
        self.birthday = str(birthday).split("-")

        for el in self.birthday:
            el = int(el)
            bir_list.append(el)
        current_datetime = datetime.now()

        birth_data = datetime(year=current_datetime.year, month=bir_list[1], day=bir_list[2])
        now_data = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day)

        if bir_list[2] >= current_datetime.day and bir_list[1] >= current_datetime.month:

            difference = birth_data - now_data

        else:

            birth_data = datetime(year=current_datetime.year + 1, month=bir_list[1], day=bir_list[2])
            difference = birth_data - now_data

        return difference.days


class AddressBook(UserDict):
    quantity = 0
    N = 0

    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data.get(record.name.value)

    def __next__(self):
        if self.quantity >= self.N:
            raise StopIteration
        self.quantity += 1
        for user in self.data.values():
            return user.value

    def __iter__(self):
        return self