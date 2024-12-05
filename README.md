# 使用docker compose部署
1. 在服务器上新建/wwww文件夹,进入www.
2. 将本仓库pull到/www,使之成为/www/[...],[...]为本仓库的所有文件.  
3. 使用docker compose up 启动项目.  

# 前端项目地址  
[Android-photo](https://github.com/22222wly/Android-photo/tree/master)  

# 环境配置说明  
python环境:   
**conda create -n ImageEnhance python==3.12**    
django环境:  
**pip install django==5.1.3**   
**pip install pymysql==1.1.1(在init添加import)**     
**pip install djangorestframework(在setting添加组件)**    
**pip install django-shortuuidfield(配置全球唯一字符串)**  
**pip install pillow(图片文件校验)**  

# Authors
后端:  [Youkang Zheng](https://github.com/zyk326)    
前端:  [Leyan Wang](https://github.com/22222wly) | [Xian Qiu](https://github.com/qrisxsum)