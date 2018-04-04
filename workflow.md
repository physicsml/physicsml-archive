the way to publish:

cd develop
fab build
cd ..
cp -r develop/output/* .
make
git add .
git commit -a -m "Message"
git push

