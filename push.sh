echo "remove old version.."
rm -vrf ../build/* 

echo "copy new version.."
cp -vr * ../build/

echo "upload new version.."
ssh brok.diku.dk rm -rf /vol/www/hjemmesider/studerende/zerrez/*
scp -r ../build/* brok.diku.dk:~/www/