# PyFTPEx

## Overview

FTP/SFTP Connection example.  

## About .env file

This repository uses `.env` file (by python-dotenv).  
You need to write connection information in `.env` file:  

    HOST = example.com
    PORT = 22
    USERNAME = root
    PASSWORD = password

## Opensource Libraries

this repository uses some libraries shown below:

 - [paramiko](https://github.com/paramiko/paramiko/)
    SSH Library. This repository uses it for SFTP connection.

 - [python-dotenv](https://github.com/theskumar/python-dotenv)
    Environment variable management library. This repository uses it for Connection-Info management.
