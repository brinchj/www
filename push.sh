#!/bin/sh

WEB_PATH=/vol/www/hjemmesider/studerende/zerrez


echo "remove old version.."
rm -rf ../build/* 

python sitemap.py

echo "copy new version.."
for t in css js png html txt; do
    for i in `find . -iname "*.$t"`; do   
        mkdir -p ../build/`dirname $i`;
        if [ $t == "html" ]; then
            cat header.html >> ../build/$i;
            cat $i >> ../build/$i;
            cat footer.html >> ../build/$i;
        else
            cp $i ../build/$i;
        fi
    done
done

echo "upload new version.."
ssh brok.diku.dk "mkdir ~/www_new"
scp -r ../build/* brok.diku.dk:~/www_new/
ssh brok.diku.dk "rm -rf $WEB_PATH/* && mv ~/www_new/* $WEB_PATH && rmdir ~/www_new"


echo "disk usage:"
ssh brok.diku.dk "du -sh $WEB_PATH"