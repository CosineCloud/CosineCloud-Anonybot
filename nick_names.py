import random
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN)

a = int(random.randint(2,4))
def nick():
    return(person.first_name()[:a]+(person.first_name()[-a:]).lower())
    
#print(nick())