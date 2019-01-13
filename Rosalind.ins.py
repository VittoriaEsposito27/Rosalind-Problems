import math
import os
import random
import re
import sys

def insertion_sort(lst):
    swap=0
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j-=1
            swap+=1
        lst[j+1]=key
    print(lst)
    print(swap)


if __name__ == '__main__':
    arr = list(map(int, '-83640 -72096 52389 41222 -33271 86853 -13637 -85322 18354 -12997 -75119 34242 -44593 15888 76077 -50435 83787 -60521 -9 64967 44324 36145 -27021 32244 68790 75492 -20578 -36961 40645 33723 62184 -32746 -76950 -75535 29358 23270 -62002 79030 -40559 -49818 49335 -64610 4169 94778 60895 -64165 71070 54656 90552 17464 -16877 50304 83903 34342 -34322 40454 -98315 59007 44680 54729 -65109 -49737 49232 -21517 -80028 -71016 68152 60912 -75852 -24656 -10105 -63910 37356 -46510 -83361 -60090 77463 -91340 -89682 25644 42480 -24065 -99553 6497 54241 -65042 87625 31029 47488 34298 31751 81751 -34181 67446 3744 -75808 -46107 34536 -69964 84584 -2306 98658 33211 -67038 -52705 92865 -64873 -17642 29482 67136 -34602 62598 80483 57466 -42170 -6283 -99197 -45117 -37260 -85117 62175 38430 13621 53167 8326 -75417 33378 45052 55726 18382 84722 37227 70076 74275 -95610 13157 45612 37535 -62340 -62208 62479 -60156 -32860 86004 36823 -44195 -62525 -65593 -63650 45466 32468 83475 -42778 -1837 -10867 66968 -94592 -3235 -83191 8849 -20591 -37246 77005 -12144 99629 1444 94719 21769 9314 -70814 3286 -87604 77960 -86860 -81824 2047 87470 -52823 -78146 -77547 -86131 21931 -4156 96353 82601 24061 -10259 81977 69959 77533 44505 -93604 -43347 -81251 65607 -37090 -76852 50318 90860 -95372 -53302 -98085 96197 3870 49593 -71718 11709 66202 19392 18901 -36906 47183 -77964 -85392 96532 -22415 65815 -96693 -95933 -7697 51311 -36675 47 -18874 -42946 -74221 92840 -74777 66557 -30727 -57742 -94388 86975 -96328 -59197 -29247 20836 -74685 -92774 -83662 -98367 36739 -94273 4811 -77063 -96268 -82094 -37412 39905 -62549 -92798 47514 97409 78578 21892 87292 48767 67919 37799 -38279 35911 46812 62009 42337 -747 93345 -73626 75319 34714 74778 87952 22318 20443 -18861 61883 -42905 -30731 -54375 -50573 -50900 -77242 -93504 -6947 14669 -5112 6309 64855 98575 21367 -89041 -37847 50765 84458 -2321 -2812 -21328 42942 99018 -33302 -52349 -72779 -75160 -99326 75186 22449 28638 71208 20848 99569 98093 -77175 -73649 60791 -88664 -89883 77862 41329 -22268 -2829 -22948 -57502 42825 87598 -60485 20163 78675 -20424 -2548 20170 -59300 -80532 1715 25804 -2887 13277 44084 -41504 55471 -87730 -11937 -34741 58331 64754 21564 89408 -64731 -30127 -52649 47923 33467 -85943 -4164 15201 -90617 -30350 -78496 50951 55666 96145 64462 79016 -96045 -54260 26433 45098 -52808 40759 34454 18793 -51832 -28402 -82665 -19801 -18912 -33937 -99531 -29518 33289 -94425 -94287 -13858 -27237 90904 81381 73199 -85132 54562 27250 83008 -6375 -1226 44871 -12929 -55778 14470 -56891 57987 -89123 -48764 46489 50464 -49413 45816 -82717 -25514 21658 39445 -2244 70649 -21928 27542 56292 70090 27630 27500 -88943 -82940 71202 -64876 -13011 20603 -50657 -32496 29036 -40944 15045 -15482 -98117 78784 -58996 -11520 -98704 -12379 -79499 42288 62918 10851 73319 -17705 -9945 54377 60055 24065 -69990 -58017 -76210 -24945 52583 8467 -49094 84764 70711 -45112 7673 -94560 -88703 4194 35504 -13451 60521 24572 -52764 -38203 -84525 32280 -47429 -30578 -89421 48452 -37315 62709 -51427 -15794 -34660 78713 -79326 -3077 40062 -25853 95048 18482 48033 -89165 46205 64808 39534 -40304 87373 13362 30795 -91568 -62086 -47640 -35697 17696 -78115 -54265 -97163 -75505 -18883 81769 -29284 -57358 8419 42731 -3806 30992 -90750 -79815 77969 8004 10904 -67903 -70321 -26777 63432 -47060 99230 6100 43833 -79308 -67511 -35778 -19295 -11393 -74256 -8114 -73089 92786 -68123 71043 -68150 -82064 -48970 33761 9812 -24426 -58084 77889 -22714 53956 87466 9825 56702 69508 46387 19840 -18524 29013 81190 -11022 -70366 58137 6495 86396 -24651 27633 -77879 33577 -24398 98869 27562 16041 82957 66446 -31832 -37882 -96946 43193 -56989 -6070 -3580 -59430 -75554 68458 -76491 -9627 94584 64504 3841 48212 68852 -20742 53237 33173 -67383 -77320 7978 -81349 55589 28973 -57803 46872 21867 7541 86996 -73304 -49841 -16625 52243 -23691 -97937 -59210 -28334 79307 19779 -72526 18204 -58297 16494 38778 83433 53881 35088 38472 -57971 -49255 -23337 -18094 66490 95532 80795 34453 59439 -13013 41870 60137 92348 6136 -82203 -43976 -63317 23847 78471 -52845 -24448 -54832 -1342 82616 25351 -68395 -35253 -81273 -88309 30808 33062 61740 -70100 -64379 -71002 -61116 42443 77606 9579 97059 72565 -83738 4348 37627 -25834 37414 83561 87388 -76075 96401 12836 36076 11753 -74061 45448 -37993 -70089 75108 3643 -30176 -50169 -55638 28857 -35254 -85034 22919 92008 19517 11186 80478 51000 -16473 39791 87570 27250 -53838 98911 -57346 71701 -89181 47423 -89131 -40921 -15154 45406 -38807 74996 29159 12546 99247 1620 -80146 -68695 45722 74427 -82124 -61868 -10342 -8587 52999 6233 98404 15702 41700 -8295 -5526 -43886 58388 -34243 72094 2042 -93825 28437 38882 -13517 89579 29415 32436 61690 76017 -65287 24019 23589 -43057 32108 -29466 -41725 -97395 96262 -27291 16717 -47522 45854 64774 26894 36942 98519 10478 -51105 13500 -79616 27012 -68415 1744 -29719 45085 13756 14279 20523 83802 -66292 -35564 -47039 -92607 -58715 -47279 -81231 57800 87454 -71351 35431 -55262 74428 596 -84386 8807 -95559 9317 68563 94404 -27602 21305 -91802 33462 51324 -54564 -95402 -6935 -35552 -88815 -58524 -51514 40253 -1419 3222 83556 43913 -29901 -51799 40240 6307 9417 -36455 -71415 31512 87029 -35604 24173'.rstrip().split()))

    insertion_sort(arr)
