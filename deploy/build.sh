#!/usr/bin/env bash
name="ig-web-mobile"

rm -rf *.gz

#判断是否接收自定义版本号
if [ $# -eq 0 ]
  then
    tag='V_0.0.9_P'
  else
    tag=$1
fi

#先删除app文件夹再复制
rm -rf $name
cp -r ../$name .

#build docker image
echo '>>>building docker image'
docker build -t $name:$tag .

#删除app文件夹
rm -rf $name

#保存docker镜像到本地，并scp
echo '>>>saving docker image'
docker save $name:$tag | gzip > $name-$tag.tar.gz
scp -P 65535 $name-$tag.tar.gz admin@10.132.166.121:/data

