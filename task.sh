yum install python3 -y
pip3 install gdown
gdown --id 1zYizjlBxR7X4SKmQMKB8rqEKibGpjymr --output jdk.rpm
gdown --id 1uv3HPKOQbVZVRJQsWKYAH-u5y2xFR0Os  --output hadoop.rpm
rpm -i jdk.rpm hadoop.rpm --force
