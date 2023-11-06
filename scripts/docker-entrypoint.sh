#!/bin/bash

# Read environment variables from .env file
source .env

# Replace placeholders in init.sql with actual values
sed "s|\$\$MYSQL_PASSWORD|$MYSQL_PASSWORD|g" /docker-entrypoint-initdb.d/init.sql > /docker-entrypoint-initdb.d/init-modified.sql

# Call the original entrypoint script with the modified SQL file
/usr/local/bin/docker-entrypoint.sh mysqld --init-file=/docker-entrypoint-initdb.d/init-modified.sql
