## Install it
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
If you want the logs to be Backed up on Dropbox, create a `config.yaml` file at the root of the folder with your Dropbox token:
```
# config.yaml

token: <token>
```
[Here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/) is how to get a Dropbox token.

## Run it
```
cd daily
python daily.py
```

or add
```
alias daily="(cd ~/.daily && source env/bin/activate && python daily.py && deactivate)"
```
in your .bashrc / .zshrc and run
```
daily
```

## Todo
Add AWS backup capabilities
