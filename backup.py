"""用于对数据进行完全备份和增量备份"""
import os
import pickle
import hashlib
import tarfile
from time import strftime

#检查文件的MD5值函数
def check_md5(fname):
    md5data = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            md5data.update(data)
    return md5data.hexdigest()

#完全备份函数
def full_backup(src,dest,md5file):
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src),strftime('%Y%m%d'))
    fname = os.path.join(dest,fname)

    tar = tarfile.open(fname,'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for path,folders,files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)

    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

#增量备份函数
def incr_backup(src,dest,md5file):
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src),strftime('%Y%m%d'))
    fname = os.path.join(dest,fname)

    md5dict = {}
    for path,folders,files in os.walk(src):
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)             #新字典

    with open(md5file,'rb') as fobj:
        old_dict = pickle.load(fobj)                  #旧字典

    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if old_dict.get(key) != md5dict[key]:         #新旧值比较，不同则表明文件为新的或已经修改，加入tar包
            tar.add(key)
    tar.close()

    with open(md5file,'wb') as fobj:                  #保存新字典数据，以便下次对比
        pickle.dump(md5dict,fobj)

if __name__ == '__main__':
    src = '/etc/security'
    dest = '/tmptmp1/backup'
    md5file = '/tmptmp1/backup/md5.data'
    if not os.path.exists(dest):
        os.makedirs(dest)  #递归创建目录，若确定路径，可以使用os.mkdir(dest)

    if strftime('%a') == 'Mon':    #周一进行完全备份，其他时间进行增量备份
        full_backup(src,dest,md5file)
    else:
        incr_backup(src,dest,md5file)
