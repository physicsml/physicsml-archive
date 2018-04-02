the way to publish:

cd develop
fab build
cd ..
cp develop/output/* .
make
git add .
git push

