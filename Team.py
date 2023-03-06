class Team:
    """
    A class representing a football team.
    """

    def __init__(self, name: str, stadium: str, city: str):
        """
     Team constructor with the given name, stadium and city

     :param name:  a string representing the name of the football team
     :param stadium: a string representing the name of the team's home ground
     :param city: a string representing the name of the team's home city
     """
        self.name = name
        self.stadium = stadium
        self.city = city

    def __repr__(self):
        """
        Return a string representation of the Team object.

        :return: a string of the format "name, stadium, city"
        """
        return f"{self.name},{self.stadium},{self.city}"


def parseTeamData(data):
    """
    Parse a string containing data for a team and return a Team object.

    :param data: a string containing data for a team in the format "team:stadium-area"
    :return: a Team object representing the team, stadium and city
    """
    data1 = data.split(":")
    team = data1[0]
    data2 = data1[1].split("-")
    stadium = data2[0]
    area = data2[1]
    return Team(team, stadium, area)


def load_teams_fr_file():
    """
    Load data from a file named "epl.txt" and return a list of Team objects.

    :return: a list of Team objects representing the data in the file
    """
    try:
        teams = []
        with open("epl.txt", "r") as my_file:
            for line in my_file:
                teams.append(parseTeamData(line))
    except FileNotFoundError:
        print("Please save the file!")
    except Exception as e:
        print("There was an error reading file:", e)
    else:
        return teams
    finally:
        my_file.close()
        return teams