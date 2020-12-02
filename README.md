# hunyuan
记录日常python使用的一些应用

# install RabbitMQ
# 1. yum -y update
# 2. yum -y install epel-release
# 3. curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash
# 4. yum -y install erlang socat
# 5. https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.5/rabbitmq-server-3.8.5-1.el7.noarch.rpm
# 6. rpm -ivh rabbitmq-server-3.8.5-1.el7.noarch.rpm
# 7. systemctl status rabbitmq-server
# 8. rabbitmqctl add_user hunyuan xxxxxxx
# 9. rabbitmqctl set_user_tags hunyuan administrator
# 10. rabbitmqctl set_permissions -p / hunyuan "." "." ".*"

# 防火墙配置
1、添加端口
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --add-port=8888/tcp --permanent
注意：添加后需要重新启动防火墙才能生效。

2、重新加载配置
firewall-cmd --reload

3、防火墙启动关闭
systemctl start firewalld.service
systemctl stop firewalld.service
systemctl enable firewalld.service

或者
service firewalld restart #重启
service firewalld start #开启
service firewalld stop #关闭

4、查看防火墙端口列表
firewall-cmd --permanent --list-port
firewall-cmd --list-all
