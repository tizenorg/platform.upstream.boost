#!/bin/bash

BOOST_VERSION=$1
BOOST_PACKAGE_LIST=${2//,/ }

echo "Boost package list: [$BOOST_PACKAGE_LIST]"

TEST_LOG="/tmp/boost_test"
export TEST_LOG
rm -f ${TEST_LOG}

# Color
Color_Off='\e[0m'       # Text Reset

# Regular Colors
Red='\e[0;31m'          # Red
Green='\e[0;32m'        # Green
Cyan='\e[0;36m'         # Cyank

# Bold
BWhite='\e[1;37m'       # White


for ix in $BOOST_PACKAGE_LIST;
do
#    echo "Build [$ix] test case"
    pushd ./libs/${ix}/test
    ../../../b2 > /dev/null 2>&1
    popd

#    echo "Check [$ix] test result"
    pushd ./bin.v2/libs/${ix}/test
    for iy in `find . -name "*.output"`;
    do
        result=`cat $iy | grep "EXIT STATUS:" | awk '{print $3}'`
        if [ $result -eq 0 ]
        then
            echo -e "${Green}PASS${Color_Off}: [$ix] [${iy##*/}]"
            echo "TEST: PASS: [$ix] [${iy##*/}]" >> ${TEST_LOG}
        else
            echo -e "${Red}FAIL${Color_Off}: [$ix] [${iy##*/}]"
            echo "TEST: FAIL: [$ix] [${iy##*/}]" >> ${TEST_LOG}
        fi
    done
    popd
done


TOTAL_CNT=`grep "TEST:" ${TEST_LOG} | wc -l`
PASS_CNT=`grep "PASS:" ${TEST_LOG} | wc -l`
FAIL_CNT=`grep "FAIL:" ${TEST_LOG} | wc -l`
SKIP_CNT=`grep "SKIP:" ${TEST_LOG} | wc -l`


br='==================='; br=$br$br$br$br;

echo -e "${Green}$br ${Color_Off}"
echo -e "${Green}Testshite summary for Boost ${BOOST_VERSION}${Color_Off}"
echo -e "${Green}$br ${Color_Off}"
echo -e "#${BWhite} TOTAL: $TOTAL_CNT ${Color_Off}"
echo -e "#${Green} PASS${Color_Off} : $PASS_CNT"
echo -e "#${Red} FAIL${Color_Off} : $FAIL_CNT"
echo -e "#${Cyan} SKIP${Color_Off} : $SKIP_CNT"
echo -e "${Green}$br ${Color_Off}"

rm -f ${TEST_LOG}
exit 0

