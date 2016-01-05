import sys
import collections

HEADER = "{name:<40} {id:<10} {username:<40}".format(name = 'Name',
                                                    id = 'ID',
                                                    username = 'Username')
ID = 0
FORENAME = 1
MIDDLE_NAME = 2
SURNAME = 3
DEPARTMENT = 4

User = collections.namedtuple('User', "ID forename middlename surname department")
Users = []
Names = collections.defaultdict(int)

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print("Usage:\ngenerate_username.py file1 [file2 [...fileN]]")
        return
    users = []
    print_header()
    for filename in sys.argv[1:]:
        for line in open(filename):
            user = get_user(line)
            if user is not None:
                users.append(user)
    print_users(users)

def print_header():
    print(HEADER)
    header_down = "{0} {1} {2}".format('_'*40, '_'*10, '_'*20)
    print(header_down)

def get_user(line):
    information = line.split(':')
    # print(information)
    for i in range(len(information)):
        information[i].strip()
    user = User(information[ID], information[FORENAME], 
                information[MIDDLE_NAME], information[SURNAME],
                information[DEPARTMENT])
    return user

def print_users(users):
    names = list()
    for user in users:
        name = generate_name(user)
        if len(name) > 0:
            names.append(name)
    names = sorted(names)
    for name in names:
        print(name)

def generate_name(user):
    middlename = (' ' + user.middlename[0]) if len(user.middlename) > 0 else ''
    user_name = "{surname}, {forename}{middlename}".format(
        surname = user.surname,
        forename = user.forename,
        middlename = middlename)

    short_name = "{0}{1}{2}".format(
        middlename.lstrip().lower(),
        user.forename[0].lower(),
        user.surname.lower())
    Names[short_name] += 1
    name = "{0:.<40} {1:<10} {2}{3}".format(user_name,
                                        '(' + user.ID + ')', 
                                         short_name,
                                         Names[short_name])
    return name


main()
