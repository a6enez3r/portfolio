#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  eval "$(ssh-agent -s)"
  ssh-add "$HOME_DIR"/.ssh/id_rsa

  cd "$PORTFOLIO_DIR"
  git pull origin master
  sudo systemctl restart portfolio
else
  echo "Not deploying, since this branch isn't master."
fi
