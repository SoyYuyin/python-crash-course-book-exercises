# Start with your work from Exercise 9-8 (page 173). Store the
# classes User, Privileges and Admin in one module. Create a
# separate file, make an Admin instance, and call show_privileges()
# to show that everything is working correctly.

import user

monbon = user.Admin('Mon', 'Ortuño', 'mon@gmail.com', 'Monbon', True)

monbon.describe_user()
monbon.privileges.privileges = ['can see content', 'can edit content']
monbon.privileges.show_privileges()
