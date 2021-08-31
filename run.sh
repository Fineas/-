#!/bin/bash

source ../../common.sh

make_input

AFL_PRELOAD=/root/libc_coverage/final_build/lib64/libc-2.32.so run_all # ld-2.32.so run_all
