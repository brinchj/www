#!/bin/zsh

WEB_PATH=/vol/www/hjemmesider/studerende/zerrez
BUILD=_build

HOST=zerrez@brok.diku.dk
TARGET="~/www_new"


echo ">> remove old version.."
rm -rf ${BUILD}
mkdir -p ${BUILD}

python sitemap.py

echo ">> copy new version.."
for t in css js png html txt; do
    for i in `find . -iname "*.$t"`; do
        mkdir -p ${BUILD}/`dirname $i`;
        if [ x"$t" = x"html" ]; then
            cat header.html >> ${BUILD}/$i;
            cat $i >> ${BUILD}/$i;
            cat footer.html >> ${BUILD}/$i;
        else
            cp $i ${BUILD}/$i;
        fi
    done
done

#echo ">> update zerrez @ appspot.."
#appcfg.py update --email zerrez@gmail.com --no_cookies gapp || exit -1

echo ">> update zerrez @ diku.."
ssh ${HOST} "mkdir ${TARGET}"
scp -r ${BUILD}/* ${HOST}:${TARGET}
ssh ${HOST} "rm -rf $WEB_PATH/* && mv ${TARGET}/* $WEB_PATH && rmdir ${TARGET}"
ssh ${HOST} "chmod -Rv uo+r ${WEB_PATH}"


echo ">> disk usage:"
ssh ${HOST} "du -sh $WEB_PATH"
