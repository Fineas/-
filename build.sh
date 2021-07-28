gcc -static -fprofile-arcs -ftest-coverage \
        -L ${SYSROOT}/usr/lib64 \
        -I ${SYSROOT}/usr/include \
        --sysroot=${SYSROOT} \
        -Wl,-rpath=${SYSROOT}/lib64 \
        -Wl,--dynamic-linker=${SYSROOT}/lib64/ld-2.32.so \
        -g -o malloc_cov_test malloc_cov_test.c ${SYSROOT}/usr/lib64/libc.a /usr/lib/gcc/x86_64-linux-gnu/9/libgcov.a