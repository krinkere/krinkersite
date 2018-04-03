# krinkersite
make html
make serve
check http://localhost:8000/

pelican content -s publishconf.py

git add .
git commit -m "message"
git push origin master

ghp-import output
git push -f origin gh-pages