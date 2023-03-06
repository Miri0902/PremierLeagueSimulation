class Managers:
    """
    A class representing a football club team and its manager.
    """
    def __init__(self, club: str, manager: str):
        """
        Initialise a Manager object with the given club and manager.

        :param club: a string representing the name of the club
        :param manager: a string representing the name of the manager
        """
        self.club = club
        self.manager = manager

    def __repr__(self):
        """
        Return a string representation of the Managers object.

        :return:  a string of the format "club, manager"
        """
        return f"{self.club}, {self.manager}"


def parseManagersData(data):
    """
    This function will parse data for a manager and return a Managers object.

    :param data: a string containing data for managers
    :return: a Managers object representing the club and manager
    """
    data1 = data.split(":")
    club = data1[0]
    manager = data1[1]
    return Managers(club, manager)


def load_managers_fr_file():
    """
    This function will load data from file "epl.managers.txt" and return list of Managers objects.

    :return: a list of Managers objects representing the data in the file
    """
    try:
        managers = []
        with open("epl.managers.txt", "r") as my_file:
            for line in my_file:
                managers.append(parseManagersData(line))
    except FileNotFoundError:
        print("File is not found!")
    except Exception as e:
        print("There was an error reading file:", e)
    else:
        return managers
    finally:
        my_file.close()