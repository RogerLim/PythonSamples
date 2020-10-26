#!/usr/bin/python3

import ftplib
import os

with ftplib.FTP('ftp.cs.brown.edu') as ftp:
    print(ftp.getwelcome())
    try:
        ftp.login()
# Find current working directory
        wdir2 = ftp.pwd()
        print(wdir2)
# Display directory DIR
        files = []
        ftp.dir(files.append)
        for rows in files:
            print(rows)
# Change diretory to pub
        ftp.cwd('pub')
        wdir2 = ftp.pwd()
        print(wdir2)
# Display directory LIST
        files = []
        ftp.retrlines('LIST', files.append)
        for rows in files:
            print(rows)
# Download README text file in binary
        file_orig = '/pub/mntflop-2.3.tar.Z'
        file_copy = 'mntflop-2.3.tar.Z'

        with open(file_copy, 'wb') as fp:
            res = ftp.retrbinary('RETR ' + file_orig, fp.write)
            if not res.startswith('226'):
                print('Download failed')
                if os.path.isfile(file_copy):
                    os.remove(file_copy)
            print("\n" + res);

    except ftplib.all_errors as e:
        print('FTP error:', e)
        if os.path.isfile(file_copy):
            os.remove(file_copy)
