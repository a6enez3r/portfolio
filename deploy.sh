#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  echo "$HOME_DIR"
  echo "$APP_DIR"
  eval "$(ssh-agent -s)"
  ssh-add "$HOME_DIR"/.ssh/id_rsa

  cd "$APP_DIR"
  git pull origin master
else
  echo "Not deploying, since this branch isn't master."
fi
