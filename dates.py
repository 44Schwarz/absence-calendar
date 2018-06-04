# ask username
# write name to the first file
# ask dates (interval)
# write dates to the second file
# TODO function to get all entries for user
# TODO function to delete user from both tables (files)
# TODO function to delete user from the second file
# TODO function to delete exact line (by its id) from the second file

from datetime import datetime


def check_user():
    with open('Users.csv', 'r') as f:
        data = f.readlines()
        names = []
        for el in data:
            names.append(el[el.find(';') + 1:el.find('\n')].lower())
        print(names)
        if name.lower() not in names:
            add_user(len(data))


def add_user(id):
    try:
        with open('Users.csv', 'a') as f:
            f.write(str(id) + ';' + name.capitalize() + '\n')
    except:
        print('Error')
        return
    print("New user has been added to the database")
    return


def get_dates():
    start_date = input('Enter start date of your absence (dd-mm-yyyy): ')
    try:
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
    except ValueError:
        print('Wrong date format')
        return -1
    print(start_date)
    end_date = input('End date: ')
    try:
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
    except ValueError:
        print('Wrong date format')
        return -1

    try:
        if end_date < start_date:
            raise Exception('End date is before start date. Error, try again.')
    except Exception as e:
        print(e)
        return -1
    else:
        write_dates(start_date, end_date)
        return 0


def write_dates(date1, date2):
    # TODO get user_id from the first file
    # TODO add one line with 2 dates to the second file
    pass


def find_all_dates(name):
    # TODO get user_id from the first file
    # TODO get all entries by user_id from the second file and print them to the screen line by line
    pass

name = input("Username: ")
check_user()
if get_dates() < 0:
    exit(-1)


