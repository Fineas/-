#!/bin/bash

source ../../common.sh

make_input

AFL_PRELOAD=./libc-2.32.so run_all # ud-2.32.so run_all
