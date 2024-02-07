if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Helper-Botz/NASRANI.git /NASRANI
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /NASRANI
fi
cd /NASRANI
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
