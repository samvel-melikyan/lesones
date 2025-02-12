class User:
   def __init__(self, login, password, name, email, role):
       self.login = login
       self.password = password
       self.name = name
       self.email = email
       self.role = role

   def create_task(self, project, description):
       project.add_task(self, description)

class Team:
   def __init__(self, name, members=[]):
       self.name = name
       self.members = members

   def add_member(self, user):
       self.members.append(user)

   def show_members(self):
       print(f'Team {self.name} members:')
       for i, user in enumerate(self.members):
           print(f'№{i + 1}, login: {user.login}, name: {user.name}')

   def get_team_size(self):
       return len(self.members)

class Task:
   def __init__(self, description):
       self.description = description


class Project:
   def __init__(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")

user1 = User("JohnD", "mloz512qyt", "John Doe", "john.doe@example.com", 'TechLead')
user2 = User("JaneD", "qw1lbz", "Jane Doe", "jane.doe@example.com", 'Python Developer')
user3 = User("BobS", "gnsJqw12", "Bob Smith", "bob.smith@example.com", 'Python Developer')

team = Team("Research Group")
team.add_member(user1)
team.add_member(user2)

team.show_members()

project = Project("UAV Detectron", team)

user1.create_task(project, "Find best model")
user2.create_task(project, "Setup Environment")
user3.create_task(project, "Optimization")
