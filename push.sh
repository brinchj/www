echo "remove old version.."
rm -rf ../build/* 

python sitemap.py

echo "copy new version.."
for t in css js png html txt; do
    for i in `find . -iname "*.$t"`; do   
        mkdir -p ../build/`dirname $i`;
        cp $i ../build/$i
    done
done

echo "upload new version.."
ssh brok.diku.dk rm -rf /vol/www/hjemmesider/studerende/zerrez/*
scp -r ../build/* brok.diku.dk:~/www/