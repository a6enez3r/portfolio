#!/bin/bash
set -xe

if [ $TRAVIS_BRANCH == 'master' ] ; then
  eval "$(ssh-agent -s)"
  ssh-add $HOME_DIR/.ssh/id_rsa

  cd $APP_DIR
  git pull origin master
else
  echo "Not deploying, since this branch isn't master."
fi
