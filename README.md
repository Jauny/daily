## Install it
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

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
