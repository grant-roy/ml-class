# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False

import random
from random import randint
from libc.stdlib cimport malloc,free

cdef char * flip_coin(float p):
    cdef:
        char* head = 'h'
        char* tail = 't'
    return head if random.random() < p else tail

cdef struct v_bag:
       float v1
       float v_rand
       float v_min

cpdef v_bag[:] run_experiment(float num_flips,float num_coins_flipped,float num_experiments):

    cdef:
       int N=<int>num_experiments, M=<int>num_coins_flipped,i,j,l
       list flips
       float * h = <float *> malloc(M * sizeof(float))
       float[::1] head_count_coins = <float[:M]>h
       v_bag * v = <v_bag *> malloc(N * sizeof(v_bag))
       v_bag[::1] results  = <v_bag[:N]>v

    for i in range(N):
        for j in range(M):

            flips = [flip_coin(0.5) for k in range(<int>num_flips)]
            count = <float>(flips.count(b'h'))/num_flips
            head_count_coins[j]=count

        l = randint(0, 999)
        results[i]= v_bag(v1=head_count_coins[0],
                          v_rand=head_count_coins[l],
                          v_min=<float>min(head_count_coins))

    return results
