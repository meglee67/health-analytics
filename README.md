# health-analytics
this is a primer for HHA 504/507

# instructions for copying over a repo,saving changes and pushing to repo
-to be able to copy the repo over from github you need to do; git clone https://example.git
- steps for saving and pushing to github; cd fastapi_class11 to make sure you're in the right file
- gotta log into github first on the terminal, so you need to do; git config --global user.name "meglee67"
- then; git config --global user.email "exampleemail@gmail.comls"
- first you need to let github know you want to add changes so you do; git add .
- then you provide a commit message to let other people know what you changed; git commit -m 'update message'
- then you need to push it to github; git push
- it will ask you to login and you need to provide your username and a special key

# instructions for how to set up credentials so you don't need to cotinually login
- if you don't want to have to login over and over again, you can do; nano ~/ .git-credentials
- type this into the shell; https://meglee67:theuniquetokenexample@github.com
- then ctrl x to get out
- then git config --global credential.helper store
- you may need to restart the terminal
