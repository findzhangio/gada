#!/bin/bash
cd /data/gada
# 获取镜像名称和版本号
image_name=$1
image_tag=$2

timestamp=$(date +%s)

# 读取docker-compose.yaml文件
cat docker-compose.yaml > tmp/docker-compose.${timestamp}

# 替换镜像
sed -i "s|$image_name:.*$|$image_name:$image_tag|g" tmp/docker-compose.${timestamp}

# 保存修改
cp -f tmp/docker-compose.${timestamp} docker-compose.yaml

# 重新启动服务
docker compose up -d