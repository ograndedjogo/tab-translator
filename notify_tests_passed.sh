if [ -f 'testresults' ]; then
    MESSAGE=`cat testresults | tail -n 1`
    MESSAGE=${MESSAGE//=/}
    MESSAGE=${MESSAGE// /+}
    MESSAGE="Tabt+build+no+$TRAVIS_BUILD_NUMBER%3A$MESSAGE"
    URL="https://smsapi.free-mobile.fr/sendmsg?user=10194111&pass=GC2q9I0YpfpbfK&msg=$MESSAGE"
    wget -qO- $URL &> /dev/null
fi
