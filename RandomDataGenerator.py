import random

import UserClass


class RDG:

    def __init__(self):
        self.FirstNameList = ['Len', 'Shantay', 'Earnestine', 'Alexis', 'Alvin', 'Amanda', 'Hermila', 'Hollie', 'Annabelle',
                         'Anjelica', 'Courtney', 'Jeniffer', 'Marvis', 'Madelaine', 'Edwin', 'Sharleen', 'Syreeta',
                         'Minna', 'Marcell']

        self.LastNameList = ['Geoffrey', 'Seymour', 'Dannie', 'Greg', 'Darrick', 'Danny', 'Jordon', 'Lonnie', 'Abram',
                        'Jonah',
                        'Margarito', 'Sang', 'Buck', 'Rodrick', 'Mel', 'Will', 'Jeramy', 'Dallas', 'Cletus', 'Jarrett ']


    def createRandomUser(self):
        if self.FirstNameList.__len__() == 0 or self.LastNameList.__len__() == 0:
            return None

        firstName = self.FirstNameList.pop( random.randint(0, self.FirstNameList.__len__()) -1)
        lastName = self.LastNameList.pop(random.randint(0, self.FirstNameList.__len__()) -1)
        username = firstName + str(random.randint(1, 999))
        email = username + '.' + lastName + '@gmail.com'
        password = str(random.randint(1000, 9999))

        user = UserClass.User(firstName,lastName,username,password,email,None,None,None)

        return user
