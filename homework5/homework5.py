# 1. Git vs GitHub: Git tracks changes in your code while GitHub is a site where you store and share your projects online
# 2. Terminal vs Command Line: The terminal is the app you open and the command line is where you type your commands
# 3. Local vs Remote Repository: A local repo is on your computer and a remote repo is online so you can back it up or share it
# 4. Version Control: A way to keep track of every change you make so you can go back or work with others easily
# 5. Staging Area: A waiting room where changes go after you add them but before you commit them
# 6. git add: Tells Git which files or changes you want to include in your next commit
# 7. git commit: Saves your staged changes with a short message about what you did
# 8. git push: Sends your commits from your computer to a remote repo like GitHub
# 9. git status: Shows what’s going on which files are changed staged or untracked
# 10. git pull: Brings the latest version of the project from the remote repo to your local one
# 11. pwd: Prints the folder you’re currently in
# 12. ls: Lists all files and folders in your current directory
# 13. cd: Moves you into a different folder
# 14. nano: Opens a simple text editor in the terminal
# 15. touch: Creates a new empty file or updates one that already exists
# 16. mv: Moves or renames a file or folder
# 17. rm: Deletes a file add -r to delete folders too
# 18. cat: Shows the contents of a file in the terminal

# You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
#   pwd
#The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
#   ls
# Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
#   cd .. cd brianna_repo git pull
# How would you move this new homework.py to the homework/ folder in your personal repository?
#       mv homework.py /python_decal/judy_decal/homework/
# How would you move yourself to the same repository as homework.py?
#   cd .. cd judy_decal cd homework
# You want to see the contents of homework.py in your terminal, how would you do this?
#   cat homework.py
#Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
#git add ., git commit -m"homework done!" git push origin main
#Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?) 
    #! [rejected] main -> main (fetch first)
    # error: failed to push some refs to ’https://github.com
    # /judy/judy_decal.git’
    # hint: Updates were rejected because the remote contains
    # work that you do
    # hint: not have locally. This is usually caused by another
    # repository pushing
    # hint: to the same ref. You may want to first integrate
    # the remote changes
    # hint: (e.g., ’git pull ...’) before pushing again.
    # hint: See the ’Note about fast-forwards’ in ’git push
    # --help’ for details.
# she should run git pull origin main to update her local repo, then run git push again to push her changes.
#What absolute path will allow you to move to Recents/?
#   cd Recents

def checkdatatype(data):
    return str(type(data))[6:len(str(type(data)))-1]

def evenOrOdd(int):
    if int%2==1:
        return "odd"
    else:
        return "even"

def sumWithLoop(numbers):
    sum = 0
    for i in numbers:
        sum+=i
    return sum

def duplicateList(list):
    newlist=[]
    for i in range(len(list)):
        newlist.append(list[i])
        newlist.append(list[i])
    return newlist

def square(num):    #error was no colon, fixed by adding colon
    return num * num

print(duplicateList(["a",2,5,67,"sixsevennnnn"]))

