if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Helper-Botz/MINNALMURALI.git /MINNALMURALI
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MINNALMURALI
fi
cd /MINNALMURALI
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
