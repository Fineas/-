cd /root/libc_coverage/SHARED
echo `awk 'BEGIN {srand();printf( "tmp-%d", 10000*rand())}'` >> /tmp/id
mkdir /root/libc_coverage/SHARED/`cat /tmp/id`
gcov -f -b  /root/libc_coverage/libc_build/malloc/malloc.c
cp /root/libc_coverage/libc_build/malloc/malloc.gcda /root/libc_coverage/SHARED/`cat /tmp/id`
cp /root/libc_coverage/libc_build/malloc/malloc.gcno /root/libc_coverage/SHARED/`cat /tmp/id`
cp /root/libc_coverage/final_build/lib64/libc-2.32.so /root/libc_coverage/SHARED/`cat /tmp/id`

/root/libc_coverage/libc_build/malloc
gcov -f -b  ./malloc.c
cp /root/libc_coverage/libc_build/malloc/malloc.c.gcov /root/libc_coverage/SHARED/`cat /tmp/id`