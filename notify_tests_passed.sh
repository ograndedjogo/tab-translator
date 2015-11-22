MESSAGE="Tabt+build+no+$TRAVIS_BUILD_NUMBER"
if [ -f 'testresults' ]; then
    TEST_MESSAGE=`cat testresults | tail -n 1`
    TEST_MESSAGE=${TEST_MESSAGE//=/}
    TEST_MESSAGE=${TEST_MESSAGE// /+}
    MESSAGE="$MESSAGE%3A$TEST_MESSAGE"
    echo $URL
else
    MESSAGE="$MESSAGE+finished+with+no+test+results"
fi

URL="https://smsapi.free-mobile.fr/sendmsg?user=10194111&pass=GC2q9I0YpfpbfK&msg=$MESSAGE"
wget -qO- $URL &> /dev/null
